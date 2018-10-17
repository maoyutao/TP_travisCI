"""WeChatTicket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from wechat.views import CustomWeChatView
from WeChatTicket.views import StaticFileView
from django.views.static import serve

urlpatterns = [
    url(r'^wechat/?$', CustomWeChatView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^api/u/', include('userpage.urls')),
    url(r'^api/a/', include('adminpage.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^', StaticFileView.as_view()),
]
