from django.shortcuts import render
# -*- coding: utf-8 -*-
# Create your views here.

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': [
        'Якщо залишились питання задавйте',
        '***-***-**-**',
        'myemail@e-mail.com'
    ]})
