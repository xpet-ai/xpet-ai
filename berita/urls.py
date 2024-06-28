from django.urls import path
from berita.views import (
    dashboard, 
    katagori_list, katagori_add,katagori_update,katagori_delete,
    artikel_list, artikel_add, artikel_detail, artikel_update, artikel_delete,
    )

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('Katagori/list', katagori_list, name="katagori_list"),
    path('Katagori/add', katagori_add, name="katagori_add"),
    path('Katagori/update/<int:id_katagori>', katagori_update, name="katagori_update"),
    path('Katagori/delete/<int:id_katagori>', katagori_delete, name="katagori_delete"),

    path('artikel/list', artikel_list, name="artikel_list"),
    path('artikel/add', artikel_add, name="artikel_add"),
    path('artikel/detail/<int:id_artikel>', artikel_detail, name="artikel_detail"),
    path('artikel/update/<int:id_artikel>', artikel_update, name="artikel_update"),
    path('artikel/delete/<int:id_artikel>', artikel_delete, name="artikel_delete"),
]