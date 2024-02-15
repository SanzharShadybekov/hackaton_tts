from django.urls import path
from . import views
from .views import translate_text

urlpatterns = [
    path('image/', views.ImageUploadView.as_view()),
    path('translate/', translate_text, name='translate'),
]
