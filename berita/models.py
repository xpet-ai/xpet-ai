import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
x = datetime.datetime.now()

class katagori(models.Model):
    nama= models.CharField(max_length=100)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "1. katagori"

class Artikal(models.Model):
    judul = models.CharField(max_length=225)
    isi = models.TextField(blank=True, null=True)
    katagori = models.ForeignKey(katagori, on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    thumbnail = models.ImageField(upload_to='artikal', blank=True, null=True) 

    create_at = models.DateTimeField(auto_now_add=True)
    slug =models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.judul
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{x.year}-{x.month}-{x.day}-{self.judul}")
        super(Artikal, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "2. Artikel"