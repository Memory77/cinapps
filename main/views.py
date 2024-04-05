from django.shortcuts import render
from .functions import multiplicate_by_5
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os
import json

def home_page(request):
    return render(request, 'main/home_page.html')

@login_required
def chiffre_page(request):
    return render(request, 'main/chiffre_page.html')

@login_required
def archive_page(request):
    return render(request, "main/archive_page.html")
