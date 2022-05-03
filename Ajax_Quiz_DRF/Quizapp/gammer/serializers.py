from rest_framework import serializers
from django.db import models
from .models import QuestionChoice, Question
import random


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = '__all__'


class QuestionChoiceSerializerTest(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        my_lst = [instance.choice_1, instance.choice_2,
                  instance.choice_3, instance.choice_4]
        random.shuffle(my_lst)
        
        question_info={'title':instance.question.title,'description':instance.question.description}
        representation['question'] = [question_info]
        representation['options'] = my_lst
 
        return representation
