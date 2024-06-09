from django.urls import path
from .views import submit_complaint, success

urlpatterns = [
    path('submit_complaint/', submit_complaint, name='submit_complaint'),
    path('success/', success, name='success'),
]
