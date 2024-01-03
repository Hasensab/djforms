from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def form(request):
    EDFO=Djform()
    d={'EDFO':EDFO}
    if request.method=='POST':
        DFDO=Djform(request.POST)
        if DFDO.is_valid():
            return HttpResponse(str(DFDO.cleaned_data))
        else:
            return HttpResponse('Data is not valid')
    return render(request,'djform.html',d)