from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("contact_us/", views.contact_us, name="Contact us"),
    path("about_us/", views.about_us, name="about_us"),
    path("tracker/", views.tracker, name="tracker"),
    path("prod_view/<int:myid>", views.prod_view, name="prod_view"),
    path("search/", views.search, name="search"),
    path("checkout/", views.checkout, name="checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
