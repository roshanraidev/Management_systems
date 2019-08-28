from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView ,PasswordChangeForm

from django.conf.urls import url
# from project.editproject import views

app_name = 'editproject'


urlpatterns = [
     url(r'^$', LoginView.as_view(template_name= 'editproject/login.html'),name ='login'),

    #  url(r'^index/$',views.index)
     path('index.html',views.index,name =' index'),url(r'^register_view/$',views.register_view, name ='register'),
   
       
    # url(r'^$', LoginView.as_view(template_name='login.html'), name='login')

    # url(r'^login/$', login, {'templates': 'editproject/login.html'}),
    # path('register.html',views.register,name = 'register'),
    # path('change_password.html',views.change_password,name =' change_password'),
    # url(r'^$',views.register,name ='register'),
    path('userdetails.html',views.userdetails,name =' userdetails'),
    #  url(r'^change_password/$', views.change_password, name ='change_password')

    # url(r'^password/$', views.change_password, name='change_password'),
    path('change_password.html',views.change_password,name ='change_password'),
    path('delete/<int:id>/', views.delete, name ='delete'),
    path('register.html',views.register_view, name = 'register_view'),
     path('login.html',views.login, name = 'login'),

] 