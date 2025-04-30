from django.contrib import admin
from django.urls import path, include
from appTP2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appTP2/', include('appTP2.urls')),
    path('', views.liste, name='home'),
]
