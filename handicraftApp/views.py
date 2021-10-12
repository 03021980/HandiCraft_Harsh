from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def login(request):
    return render(request,'login.html')

def logindata(request):
    uname = request.POST['uname']
    psw = request.POST['psw']
    data=registermodel.objects.all()
    for d in data:
        if d.username==uname and d.password==psw:
            return render(request,'home.html')
    return render(request,'login.html',{'error':'invalid data'})   

def register(request):
    return render(request,'register.html')

def registering(request):
    RData = registermodel(username=request.POST['username'],phNum=request.POST['phNum'],email=request.POST['email'],password=request.POST['password'],confpswd=request.POST['confpswd'])
    RData.save()
    data=registermodel.objects.all()
    confpswd = request.POST['confpswd']
    for d in data:
        if d.password==confpswd:
            return render(request,'login.html')    
    return render(request,'register.html')

def homeView(request):
    return render(request,'home.html')

def HdecorViews(request):
    return render(request,'hdecor.html')

def formdetailViews(request):
    return render(request,'formd.html')

def wallHangingViews(request):
    return render(request,'wallhanging.html')

def dreamcViews(request):
    return render(request,'dreamcatch.html')

def showPViews(request):
    return render(request,'showpiece.html')

def photofViews(request):
    return render(request,'photoframes.html')

def handbagViews(request):
    return render(request,'handbags.html')

def sbagViews(request):
    return render(request,'shBags.html')

def clutcherViews(request):
    return render(request,'clutch.html')

def potViews(request):
    return render(request,'pottery.html')

def clothViews(request):
    return render(request,'clothing.html')

def kanjivaramViews(request):
    return render(request,'kanjivaram.html')

def banarasiViews(request):
    return render(request,'banarasi.html')

def patolaViews(request):
    return render(request,'patola.html')

def bandhaniViews(request):
    return render(request,'bandhani.html')

def footwareViews(request):
    return render(request,'footware.html')

def kolhapuriViews(request):
    return render(request,'kolhapuri.html')

def jaipuriViews(request):
    return render(request,'jaipuri.html')

def jewelleryViews(request):
    return render(request,'jewellery.html')

def earringsViews(request):
    return render(request,'earrings.html')

def banglesViews(request):
    return render(request,'bangles.html')

def necklaceViews(request):
    return render(request,'necklace.html')

def paintViews(request):
    return render(request,'paint.html')

def pViews(request):
    return render(request,'painting.html')

def bpaintViews(request):
    return render(request,'bottlep.html')

def offer199Views(request):
    return render(request,'offer199.html')

def offer299Views(request):
    return render(request,'offer299.html')

def offer499Views(request):
    return render(request,'offer499.html')

def offer599Views(request):
    return render(request,'offer599.html')

def cartViews(request):
    proddata=Pdetailsmodel.objects.all()
    return render(request,'cart.html',{'Data':proddata})

def pdetailsView(request):
    PData = Pdetailsmodel(pname=request.POST['pname'],pquantity=request.POST['pquantity'],cname=request.POST['cname'],caddress=request.POST['caddress'],cphnum=request.POST['cphnum'],cemail=request.POST['cemail'])
    PData.save()
    return render(request,'formd.html')

def editViews(request):
    id=request.GET['id']
    user=Pdetailsmodel.objects.get(id=id)
    return render(request,'edit.html',{'i': user})

def updateValueViews(request):
    updateobj=Pdetailsmodel.objects.get(id=request.POST['id'])
    updateobj.pname = request.POST['PRODName']
    updateobj.pquantity = request.POST['PRODquan']
    updateobj.caddress = request.POST['CUSadd']
    updateobj.cphnum = request.POST['CUSphn']
    updateobj.cemail = request.POST['CUSemail']
    updateobj.save(update_fields=['pname','pquantity','caddress','cphnum','cemail'])
    updateobj.save()
    proddata=Pdetailsmodel.objects.all()
    return render(request,'cart.html',{'Data':proddata})

def deleteViews(request):
    deletee=request.GET['del']
    Pdetailsmodel.objects.filter(id=deletee).delete()
    proddata=Pdetailsmodel.objects.all()
    return render(request,'cart.html',{'Data':proddata})