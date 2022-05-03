from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    correct_answers = models.CharField(max_length=60)
    
class QuestionChoice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_1 = models.CharField(max_length=60)
    choice_2 = models.CharField(max_length=60)
    choice_3 = models.CharField(max_length=60)
    choice_4 = models.CharField(max_length=60)
    
class UserPoint(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Completed_Ans = models.JSONField()
    Correct_Count = models.IntegerField(default=0)
    Incorrect_Count = models.IntegerField(default=0)