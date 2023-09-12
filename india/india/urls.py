"""
URL configuration for india project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from lucknow import views as v1
from agra import views as v2
from gorakhpur import views as v3
from kanpur import views as v4
from rajasthan import views as v5
from goa import views as v6
# from static import views as v7
urlpatterns = [
    path('admin/', admin.site.urls),
    path('lko/',v1.lko),
    path('agra/',v2.agraa),
    path('gorakhpur/',v3.gorakh),
    path('kanpur/',v4.kan),
    path('rajasthan/',v5.rajas),
    path('goa/',v6.go),
]
