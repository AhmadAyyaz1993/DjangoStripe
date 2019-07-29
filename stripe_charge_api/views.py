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

            charge = stripe.Charge.create(
                amount=str(int(amount*100)),
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
        
