from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def course(request):
    return render(request, 'course.html')


def gallery(request):
    return render(request, 'gallery.html')


def faculty(request):
    return render(request, 'faculty.html')


def contact(request):
    return render(request, 'contact.html')


def quizportal(request):
    return render(request, 'quizportal.html')
