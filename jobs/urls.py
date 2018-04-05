"""DCGroup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from jobs import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='jobs/templates/index.html') ),
    path('jobs/', views.home),
    path('APC/', TemplateView.as_view(template_name='jobs/templates/APC.html')),
    path('EATON/', TemplateView.as_view(template_name='jobs/templates/EATON.html')),
    path('EATON/9315', TemplateView.as_view(template_name='jobs/templates/9315.html')),
    path('EATON/9315/capsandfans', TemplateView.as_view(template_name='jobs/templates/9315capsandfans.html')),
    path('EATON/9315/capsandfans/100_160', views.eaton_9315_100_160_caps),
]
