from django.conf.urls import url
from .views import RegistUser, AppLogin
from . import views

urlpatterns = [
    url('regist_user', views.RegistUser.as_view(), name='regist_user'),
    url('app_login', AppLogin.as_view(), name='app_login')
]