from django.urls import path

from . import views

app_name = 'fastfood'
urlpatterns = [
    path("", views.index, name="index"),
    path("checkout", views.checkout, name="checkout"),
    path("payment", views.payment, name="payment"),
]