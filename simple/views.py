from django.shortcuts import render

from .serializer import *
from rest_framework.response import Response
from rest_framework import viewsets


class Data_view(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def list(self, request, *args, **kwargs):
        data = Data.objects.all()
        for i in data:
            data = []
            d = {
                "id": i.id,
                "name": i.name,
                "height": i.height,
                "message": i.description,
            }
            data.append(d)
            datas= {
                'status:':i.status,
                'data:':data,
                'lang:':i.lang.lang
            }
        return Response(datas)
