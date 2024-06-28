from django.shortcuts import render
from berita.models import Artikal, katagori

def home(request):
    template_name = "halaman/index.html"
    Katagori = request.GET.get('Katagori')
    if Katagori == None:
        print("ALL")
        data_artikel = Artikal.objects.all()
        menu_aktif = "ALL"
    else:
        print("Bukan ALL")
        try:
            get_Katagori = katagori.objects.get(nama=Katagori)
            data_artikel = Artikal.objects.filter(katagori=get_Katagori)
            menu_aktif = Katagori
        except:
            menu_aktif = "ALL"
            data_artikel = []

    data_katagori = katagori.objects.all()
    context ={
        'title':'Selamat datang',
        'data_artikel': data_artikel ,
        'data_katagori': data_katagori,
        'menu_aktif': menu_aktif

    }
    return render(request, template_name, context)

def about(request):
    template_name = "halaman/about.html"
    context ={
        'title':'Selamat datang',
        'umur': 20
    }
    return render(request,template_name, context)   

def contact(request):
    template_name = "halaman/contact.html"
    context ={
        'title':'Selamat datang',
        'umur': 20
    }
    return render(request,template_name, context) 

def detail_artikel(request, slug):
    template_nama = 'halaman/detail_artikel.html'
    artikel = Artikal.objects.get(slug=slug)
    print(artikel.author)
    context = {
        'title': artikel.judul,
        'artikel': artikel   
    }
    return render(request, template_nama, context)