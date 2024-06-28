from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from berita.models import katagori, Artikal
from berita.forms import ArtikalForm

# Create your views here.
def is_operator(user):
    if user.groups(name='Operator').exists():
        return True
    else:
        return False



@login_required
def dashboard(request):
    template_name = "dashboard/index.html"
    context ={
        'title':'Selamat datang',
    }
    return render (request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/authentikasi/logout')
def katagori_list(request):
    template_name = "dashboard/snippets/katagori_list.html"
    try: 
        Katagori = katagori.objects.all()
    except:
        return redirect(katagori_list)
    print(Katagori)
    context ={
        'title':'halaman katagori',
        'Katagori': Katagori
    }
    return render (request, template_name, context)

@login_required
def katagori_add(request):
    template_name = "dashboard/snippets/katagori_add.html"
    if request.method == "POST":
        nama_imput = request.POST.get('nama_katagori')
        if nama_imput != None or nama_imput != "":
            katagori.objects.create(
                nama = nama_imput
            )    
            return redirect(katagori_list)
         
    context = {
        'title':'tambah katagori'
    }
    return render(request, template_name, context) 

@login_required
def katagori_update(request, id_katagori):
    template_nama ="dashboard/snippets/katagori_update.html"
    Katagori = katagori.objects.get(id=id_katagori)
    if request.method == "POST":
        nama_imput = request.POST.get('nama_katagori')
        Katagori.nama = nama_imput
        Katagori.save()
        return redirect(katagori_list)
    context ={
        'title':'update katagori',
        'Katagori' : Katagori
    }
    return render(request, template_nama, context)

@login_required
@user_passes_test(is_operator, login_url='/authentikasi/logout')
def katagori_delete(request, id_katagori):
    try: 
        katagori.objects.get(id=id_katagori).delete()
    except:
        pass
    return redirect(katagori_list)

@login_required
def artikel_list(request):
    template_name = "dashboard/snippets/artikel_list.html"
    if request.user.groups.filter(name='Operator'):
        artikel = Artikal.objects.all()
    else:
        artikel = Artikal.objects.filter(author=request.user)
    print(artikel)
    context = {
        'title':'daftar artikel',
        'artikel': artikel
    }
    return render(request, template_name, context)

@login_required
def artikel_add(request):
    template_name = "dashboard/snippets/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikalForm(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
        else:
            print(forms.error_class)
    forms = ArtikalForm()
    context = {
        'title':'tambah artikel',
        'forms':forms
    }
    return render(request, template_name,context)

@login_required
def artikel_delete(request, id_artikel):
    try:
        Artikal.objects.get(id=id_artikel).delete()
    except:pass
    return redirect(artikel_list)

@login_required
def artikel_detail(request, id_artikel):
    template_name = "dashboard/snippets/artikel_detail.html"
    artikel = Artikal.objects.get(id=id_artikel)
    context = {
        'title': artikel.judul,
        'artikel':artikel
    }
    return render(request, template_name, context)

@login_required
def artikel_update(request, id_artikel):
    template_name = "dashboard/snippets/artikel_forms.html"
    artikel = Artikal.objects.get(id=id_artikel)
    forms = ArtikalForm(instance=artikel)

    if request.user.groups.filter(name='Operator'):
        pass
    else:
       if  artikel.author != request.user:
            return redirect('/')

    if request.method == "POST":
        forms = ArtikalForm(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub =  forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
    context = {
        'title':'tambah artikel',
        'forms':forms
    }
    return render(request, template_name, context)
