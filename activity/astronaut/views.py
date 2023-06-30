from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from django.http import HttpResponse

# Create your views here.

class NewAstronautForm(forms.Form):
    name = forms.CharField(label="Name")
    height = forms.IntegerField(label="Height", min_value=100, max_value=300)

def index(request):
    form = NewAstronautForm(request.POST)
    context_dict = {"form": form}

    return render(request, 'astronaut/index.html', context={'form': NewAstronautForm()})

def results(request):
    # context_dict = {
    #     "name": name,
    #     "height": height,
    # }

    if request.method == "POST":
        form = NewAstronautForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            height = form.cleaned_data["height"]
            context_dict = {
                "name": name,
                "height": height,
                "below": height <= 160,
                "above": height >= 190,
                "correct": height > 160 and height < 190,
            }
            return render(request, 'astronaut/results.html', context = context_dict)
    
    