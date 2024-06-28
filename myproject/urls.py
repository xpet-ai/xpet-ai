from django.contrib import admin
from django.urls import path, include


############################### ini menampilkan gambar yang sudah di upload pada folder ###############################
from django.conf import settings
from django.conf.urls.static import static


from myproject.views import home, about, contact, detail_artikel
from myproject.authentikasi import akun_login, akun_registrasi, akun_logout

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('artikel/<slug:slug>', detail_artikel, name="detail_artikel"),
    

    path('dashboard/', include("berita.urls")),


    path('authentikasi/login', akun_login, name="akun_login"),
    path('authentikasi/registrasi', akun_registrasi, name="akun_registrasi"),
    path('authentikasi/logout', akun_logout, name="akun_logout"),

]



###################### ini unutk menampilkkan gambar yang sudah di upload pada folder media ###########################
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)