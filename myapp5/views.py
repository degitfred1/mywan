from django.shortcuts import render
from .models import rap


def ban(request):
    who=rap.objects.filter(title='wish')
    return render(request,'index.html',{'who':who})