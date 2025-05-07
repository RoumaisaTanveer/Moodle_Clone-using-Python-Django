# web/moodle_clone/urls.py
from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  
    path('courses/', include('core.urls')),  # This should point to course-related URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Handles authentication
]
