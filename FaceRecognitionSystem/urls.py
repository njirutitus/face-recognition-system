from django import urls
import ExaminationMalpractice
from django.contrib import admin
from django.urls import path, include

# Change admin site title
admin.site.site_header = ("Site Administration")
admin.site.site_title = ("Face Recognition System Admin")

urlpatterns = [
    path('',include('ExaminationMalpractice.urls')),
    path('admin/', admin.site.urls),
]
