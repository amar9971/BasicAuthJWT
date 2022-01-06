from django.urls import path
from .views import RagisterView, LoginView, UserView, LogoutView

urlpatterns = [

    path('ragister', RagisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

]
