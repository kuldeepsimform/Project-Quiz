from django.urls import path
from .views import index,QuestionChoiceView
urlpatterns = [
    path('', index,name='index'),
    path('t', QuestionChoiceView.as_view(),name='main'),
]