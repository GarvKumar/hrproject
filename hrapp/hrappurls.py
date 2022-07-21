from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^aboutus',views.aboutus,name='aboutus'),
    url(r'^registration',views.registration,name='registration'),
    url(r'^login',views.login,name='login'),
    url(r'^contactus',views.contactus,name='contactus'),
    url(r'^saveenq',views.saveenq,name='saveenq'),
    url(r'^regcode', views.regcode, name='regcode'),
    url(r'^validateuser',views.validateuser,name='validateuser'),

]