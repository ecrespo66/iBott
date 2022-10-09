"""iBott URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog.views import *
from iBott import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index),
                  path('blog/<str:url>/', single_post),
                  path('services/', services),
                  path('product/', product),
                  path('contact/', contact),
                  path('blog/', blog),
                  path('new_post', new_post),
                  path('uploadi/', csrf_exempt(uploadi)),
                  path('uploadf/', csrf_exempt(uploadf)),
                  path('linkfetching/', upload_link_view),
                  path('<str:url>/', site_pages)
              ] + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                      document_root=settings.MEDIA_ROOT)
