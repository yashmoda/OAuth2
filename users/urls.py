from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register),
    path("token/", views.get_tokens),
    path("token/refresh/", views.refresh_token),
    path("token/revoke/", views.revoke_token),
]