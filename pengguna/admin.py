from django.contrib import admin
from pengguna.models import Biodata

# Register your models here.
class BiodataAdmin(admin.ModelAdmin):
    list_display = ['user', 'alamat', 'telpon']
    search_fields = ['user_username']
admin.site.register(Biodata, BiodataAdmin)