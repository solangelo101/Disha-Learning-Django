from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('course/', views.course),
    path('contact/', views.contact),
    path('faculty/', views.faculty),
    path('gallery/', views.gallery),
    path('quizportal/', views.quizportal),
]