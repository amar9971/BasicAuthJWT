
from django.urls import path
from .views import RagisterView,LoginView
urlpatterns = [

    path('ragister', RagisterView.as_view()),
    path('login', LoginView.as_view()),

    ]