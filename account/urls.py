from django.urls import path, include
from . import views
# from .views import signup, MyLoginView
# from django.contrib.auth.views import LogoutView

# app_name = 'account' #app이 여러개일 때, 어느 앱의 url name인지 헷갈리니까 URLconf에 이름공간(namespace)을 추가하자.

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
]