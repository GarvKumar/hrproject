from django.contrib import admin
from . models import Enquiry
from . models import JobSeeker
from . models import AdminLogin
# Register your models here.
admin.site.register(Enquiry)
admin.site.register(JobSeeker)
admin.site.register(AdminLogin)