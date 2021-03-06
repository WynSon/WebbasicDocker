"""webblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

from app import views
from myprofile import views as myprofile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.websec_view , name='home'),
    path('/owasptop10',views.home_view , name='index'),
    path('about/',views.about_view, name='about'),
    path('accounts/', include('django.contrib.auth.urls') ),
    path('login/' , myprofile_views.Login_view.as_view(), name='login'),
    path('register/' , myprofile_views.Register_view.as_view(), name='register'),
    path('profile/' , myprofile_views.myprofile_view.as_view(), name='profile'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)