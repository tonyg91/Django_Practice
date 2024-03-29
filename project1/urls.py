"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
## or from routes.views import HelloWorld
import routes.views as routesviews

urlpatterns = [
    path('admin/', admin.site.urls),
    ## or path('hello/', HelloWorld)
    path('hello/', routesviews.HelloWorld),
    path('todo/', routesviews.index),
    path('journals/', routesviews.jindex),
    path('supply/', routesviews.sindex)
]
