from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("filter/", views.get_by_name, name="filter"),
]