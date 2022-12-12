from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import MovesList, Move
from .forms import CreateNewList
from .datahora import Data, Tempo
from .pdf import htmlpdf
from django.views import View
from xhtml2pdf import pisa
import urllib.request
import os
import sys
from bs4 import BeautifulSoup as bs


# Create your views here.
def index(response, id):
    ls = MovesList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)

        if response.POST.get("newMove"):
            txt = response.POST.get("new")

            if float(txt) >= 0:
                ls.move_set.create(value=txt, data=Data(), hora=Tempo(), tipo=True).save()
                ls.totalLista = ls.totalLista + float(txt)
            else:
                print("invalid")

        elif response.POST.get("newMove2"):
            txt = response.POST.get("new")
            calc = 0.0
                
            for i in response.user.moveslist.all():
                calc+=i.totalLista

            if float(txt) >= 0 and calc>=float(txt):
                ls.move_set.create(value=txt, data=Data(), hora=Tempo(), tipo=False).save()
                ls.totalLista = ls.totalLista - float(txt)
            else:
                print("invalid")

        ls.save()
    

    return render(response, "main/list.html", {"ls":ls})

def home(response):
    usuario = str(response.user.username).capitalize()
    return render(response, "main/home.html", {"usuario":usuario})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = MovesList(name=n, totalLista=0)
            t.save()
            response.user.moveslist.add(t)
        
        return HttpResponseRedirect("/%i" %t.id)

    
    else:
        form = CreateNewList()
    
    return render(response, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html", {})

def saldo(response):
    calcular = 0
    for i in response.user.moveslist.all():
        calcular += i.totalLista

    saldo = {"saldo": calcular}
    
    return render(response, "main/saldo.html", {"Saldo": saldo})

def extrato(response):
    usuario = str(response.user.username).capitalize()
    data = Data()
    hora = Tempo()
    return render(response, "main/extrato.html", {"usuario":usuario, "data":data,"hora":hora})

def pdf(request):
    pdf = htmlpdf("main/extrato.html")
    return HttpResponse(pdf, content_type="application/pdf")


def mano(url, out_folder="/main/templates/"):
    soup = bs(urlopen(url))
    parsed = list(urlparse(url))

    for image in soup.findAll("img"):
        print("Image: %(src)s" % image)
        filename = image["src"].split("/")[-1]
        parsed[2] = image["src"]
        outpath = os.path.join(out_folder, filename)
        if image["src"].lower().startswith("http"):
            urlretrieve(image["src"], outpath)
        else:
            urlretrieve(urlunparse(parsed), outpath)

def _usage():
    print("usage: python dumpimages.py http://example.com [outpath]")
