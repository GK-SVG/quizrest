from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from .serializers import SubSerializer
from .models import Subject,Class

class Quiz(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubSerializer

class Quizc(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubSerializer

    # def perform_create(self,serializer):
    #     serializer.save(user=self.request.user)

class Quizr(RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubSerializer

class Quizu(UpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubSerializer

class Quizru(RetrieveUpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubSerializer

class Quizd(DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubSerializer


import requests
import json
from django.http import HttpResponse

def quizs(request):
    url = "http://127.0.0.1:8000/?format=json"
    res = requests.get(url)
    data = res.text
    pdata = json.loads(data)

    return HttpResponse(pdata[0]['title'])