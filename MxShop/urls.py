"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.documentation import include_docs_urls
from django.urls import path
from rest_framework.authtoken import views

from users.views import SmsCodeViewset

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')
router.register(r'categorys', CategoryViewSet, base_name='categorys')
router.register(r'codes', SmsCodeViewset, base_name='codes')
# router.register(r'priceRange', )


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 配置媒体文件路径
    url(r'docs/', include_docs_urls(title="MxShop doc")),
    url(r'^', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),  # drf 自带的token认证模式
    url(r'^login/', obtain_jwt_token),
]
