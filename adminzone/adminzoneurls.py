from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^adminhome',views.adminhome,name='adminhome'),
    url(r'^jobseeker',views.jobseeker,name='jobseeker'),
    url(r'^enquiries',views.enquiries,name='enquiries'),
    url(r'^changepassword',views.changepassword,name='changepassword'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^adminchangepwd',views.adminchangepwd,name='adminchangepwd'),
    url(r'^add',views.add,name='add'),
]