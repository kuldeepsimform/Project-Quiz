from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,QuestionChoice
from .serializers import QuestionChoiceSerializer,QuestionChoiceSerializerTest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
import random
# Create your views here.


def index(request):
    choices = QuestionChoice.objects.all().order_by('?')
    dic={}
    for i in range(len(choices)):           
        l=[]
        
        l.append(choices[i].choice_1)
        l.append(choices[i].choice_2)
        l.append(choices[i].choice_3)
        l.append(choices[i].choice_4)
        
        new_l=[]
        while l:
            c=random.choice(l)
            new_l.append(c)
            l.remove(c)
        dic[choices[i]] = new_l    
         

    for i in dic.keys():
        print(i.question.title)
    return render(request, 'index.html',{'dic':dic})


class QuestionChoiceView(APIView):
    def get(self,request):
        questionchoice = QuestionChoice.objects.all().order_by('?')        
        serializer = QuestionChoiceSerializerTest(questionchoice,many=True)
        
        return Response(serializer.data)
