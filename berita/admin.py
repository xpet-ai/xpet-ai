from django.contrib import admin
from berita.models import katagori, Artikal

# Register your models here.

admin.site.register(katagori)

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ['judul', 'katagori', 'author']
    search_fields = ['judul']
admin.site.register(Artikal, ArtikelAdmin)
