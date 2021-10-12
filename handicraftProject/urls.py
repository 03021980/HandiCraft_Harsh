"""handicraftProject URL Configuration

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
from django.contrib import admin
from django.urls import path
from handicraftApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register),
    path('login/',views.login),
    path('LoginData/',views.logindata),
    path('registerData/',views.registering),
    path('home/',views.homeView),
    path('hdecor/',views.HdecorViews),
    path('formdetail/',views.formdetailViews),
    path('wallhanging/',views.wallHangingViews),
    path('dcatcher/',views.dreamcViews),
    path('showpiece/',views.showPViews),
    path('photoframes/',views.photofViews),
    path('handbag/',views.handbagViews),
    path('shoulderbags/',views.sbagViews),
    path('clutch/',views.clutcherViews),
    path('pot/',views.potViews),
    path('clothing/',views.clothViews),
    path('kanjivaram/',views.kanjivaramViews),
    path('banarasi/',views.banarasiViews),
    path('patola/',views.patolaViews),
    path('bandhani/',views.bandhaniViews),
    path('footware/',views.footwareViews),
    path('kolhapuri/',views.kolhapuriViews),
    path('jaipuri/',views.jaipuriViews),
    path('jewellery/',views.jewelleryViews),
    path('earrings/',views.earringsViews),
    path('bangles/',views.banglesViews),
    path('necklace/',views.necklaceViews),
    path('painting/',views.paintViews),
    path('paint/',views.pViews),
    path('bpaint/',views.bpaintViews),
    path('offer199/',views.offer199Views),
    path('offer299/',views.offer299Views),
    path('offer499/',views.offer499Views),
    path('offer599/',views.offer599Views),
    path('cart/',views.cartViews),
    path('Pdetails/',views.pdetailsView),
    path('edit/',views.editViews),
    path('updateValues/',views.updateValueViews),
    path('delete/',views.deleteViews),
]
