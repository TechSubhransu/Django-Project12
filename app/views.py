from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")

def register_with_model_form(request):
    SMFO = StudentModelForm()
    d = {'SMFO': SMFO}
    if request.method == 'POST':
        SDO = StudentModelForm(request.POST)
        if SDO.is_valid():
            SDO.save()
            return HttpResponse('DOne........')
        return HttpResponse('Invalid Data')
    return render(request, 'register_with_model_form.html', d)
