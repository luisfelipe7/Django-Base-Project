'''
Created by Luis Felipe Castro Sanchez
Universidad Nacional de Costa Rica 
GitHub User luisfelipe7
'''

from django.contrib import admin
# This import is necessary for the url
from django.conf.urls import url, include
from django.urls import path
# We need to import for the view, the point means that includes all the views from the file
from . import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),  # http://127.0.0.1:8000/
    # url(r'^courses/', include(('courses.urls', 'courses'), namespace='courses')),
]
