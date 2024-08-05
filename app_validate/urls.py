from django.urls import path
from .views import validate_email_view

urlpatterns = [
    path('validate-email', validate_email_view, name='validate_email'),
]
