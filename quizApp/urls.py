from django.urls import path
from . import views
urlpatterns = [
    path('', views.Quiz.as_view(),name='quiz'),
    path('quizs', views.quizs,name='quizs'),
    path('<int:pk>/',views.Quizr.as_view(),name='quizr'),
    path('<int:pk>/d',views.Quizd.as_view(),name='quizd'),
    path('<int:pk>/u',views.Quizu.as_view(),name='quizu'),
    path('<int:pk>/ru',views.Quizru.as_view(),name='quizru'),
    path('create',views.Quizc.as_view(),name='quizc'),
]