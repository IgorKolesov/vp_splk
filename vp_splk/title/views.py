from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'title/index_page.html')



