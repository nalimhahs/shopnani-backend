from django.urls import path, include
from . import views

# Added the get result view to the list of valid url paths

urlpatterns = [
  path('', views.GetResultView.as_view()),
]