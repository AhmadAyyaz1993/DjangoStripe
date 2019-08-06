# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(['POST'])
def charge(request):
    if request.method == 'POST':
        try:
            currency  = request.data.get('currency')
            amount  = request.data.get('amount')
            token = request.data.get('token')
            description = request.data.get('description')


            # convert amount var above into integer,
            # multiply by 100, then make it a string again
            # Stripe servers expects the amount param to be a string
            # Multiplying it to 100 because with usd currency it takes amount in cents so we needed to convert it to dollars
            charge = stripe.Charge.create(
               #accepting amount as cents
               #amount=str(int(amount*100)),
               #accepting amount as cents
                amount=amount,
                currency=currency,
                description=description,
                source=token
            )
            return Response({
                "code": 200,
                "charge": charge
            })
        except Exception as e:
            return Response({
                "code":400,
                "error": str(e)
            })

        return Response({
                "code": 10000
            })
        
