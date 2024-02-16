from django.urls import path
from . import views

urlpatterns = [
    path('image/', views.ImageUploadView.as_view()),
    path('translate/', views.TranslateView.as_view()),
]
