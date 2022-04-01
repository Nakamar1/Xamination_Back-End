"""Xamination URL Configuration

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
from django.urls import path, include
from .views import home, about, mapel, mtk, bing, bindo, ipa
from soal import views

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('mapel/', mapel, name='mapel'),
    path('mapel/mtk', mtk, name='mapel_mtk'),
    path('mapel/b_ing', bing, name='mapel_bing'),
    path('mapel/b_indo', bindo, name='mapel_bindo'),
    path('mapel/ipa', ipa, name='mapel_ipa'),
    path('mapel/mtk/soal', views.soal_mtk, name='soal_mtk'),
    path('mapel/ipa/soal', views.soal_ipa, name='soal_ipa'),
    path('mapel/b_ing/soal', views.soal_ing, name='soal_ing'),
    path('mapel/b_indo/soal', views.soal_indo, name='soal_indo'),
    path('mapel/mtk/hasil', views.jawaban_mtk, name='hasil_mtk'),
    path('mapel/ipa/hasil', views.jawaban_ipa, name='hasil_ipa'),
    path('mapel/b_ing/hasil', views.jawaban_ing, name='hasil_ing'),
    path('mapel/b_indo/hasil', views.jawaban_indo, name='hasil_indo'),
    path('admin/', admin.site.urls),
]
