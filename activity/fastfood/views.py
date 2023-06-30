from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from django.http import HttpResponse

# Create your views here.

"""
    Order form
    num_burger holds the number of burger ordered by the user
    num_fries holds the number of fries ordered by the user
    num_sodas holds the number of sodas ordered by the user
"""
class NewFastfoodForm(forms.Form):
    num_burger = forms.IntegerField(label="Enter the number of burgers")
    num_fries = forms.IntegerField(label="Enter the number of fries")
    num_sodas = forms.IntegerField(label="Enter the number of sodas")

"""
    Checkout form
    final_total holds the value for the total amount of the order
    money_rendered holds the value for the amount of rendered money by the user
"""
class NewCheckoutForm(forms.Form):
    final_total = forms.FloatField(label="Final Total: $")
    money_rendered = forms.FloatField(label="Enter amount tendered: ")

"""
    Loads the initial order page
"""
def index(request):
    context_dir = {
        "form": NewFastfoodForm(),
    }
    return render(request, 'fastfood/index.html', context= context_dir)

"""
    Loads the checkout page
"""
def checkout(request):
    if request.method == "POST":
        form = NewFastfoodForm(request.POST)
        if form.is_valid():
            num_burger = form.cleaned_data["num_burger"]
            num_fries = form.cleaned_data["num_fries"]
            num_sodas = form.cleaned_data["num_sodas"]
            before_tax = round(((num_burger * 1.69) + (num_fries * 1.09) + (num_sodas * 0.99)), 2)
            tax = round((before_tax * 0.065), 2)
            total = before_tax + tax
            checkout = NewCheckoutForm(initial={'final_total': total, 'money_rendered': 0})
            context_dict = {
                "before_tax": before_tax,
                "tax": tax,
                "total": total,
                "form": checkout
            }

            return render(request, "fastfood/checkout.html", context = context_dict)

"""
    Loads the payment page
"""
def payment(request):
    if request.method == "POST":
        form = NewCheckoutForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data["final_total"]
            money_rendered = form.cleaned_data["money_rendered"]
            change = money_rendered - total
            context_dict = {
                "final_total": total,
                "money_rendered": money_rendered,
                "change": change,
            }
            return render(request, "fastfood/payment.html", context = context_dict)

