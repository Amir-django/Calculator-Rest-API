from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 


class calc(APIView):
    def post(self, request):
        serializer = calculatorserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            val1=serializer.data['value1']
            val2=serializer.data['value2']
            oper=str(serializer.data['operation'])
            if oper == '+':
                result = val1+val2
            elif oper == '-':
                result = val1-val2
            elif oper == '/':
                result = val1/val2
            elif oper == '*':
                result = val1*val2
            return Response({'result':result})
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args):
        val1=int(request.query_params['value1'])
        val2=int(request.query_params['value2'])
        oper=str(request.query_params['operation'])
        if oper == ' ':
            result = val1+val2
        elif oper == '-':
            result = val1-val2
        elif oper == '/':
            result = val1/val2
        elif oper == '*':
            result = val1*val2
        return Response({'result':result})
