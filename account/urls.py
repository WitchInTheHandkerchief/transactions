from django.urls import path

from account import views

urlpatterns = [
    path("create-account/", views.CreateAccountAPIView.as_view(), name="create_account")
]
