from django.db import models
# Create your models here.

class Settings(models.Model):
    Icon = models.ImageField(null=True, blank=True, verbose_name='İcon')
    Logo = models.ImageField(null=True, blank=True, verbose_name='Logo')
    Title = models.CharField(max_length=200, verbose_name='Şirket Adı')
    Description = models.TextField(verbose_name='Sayfa Açıklaması')
    Keywords = models.TextField(verbose_name='Anahtar Kelimeler')


class Slider(models.Model):
    Name = models.CharField(max_length=200, verbose_name='Slider Adı')
    Description = models.CharField(max_length=200,  verbose_name='Açıklama')
    Link = models.CharField(max_length=200, verbose_name='Buton Link',null=True)
    Photo = models.ImageField(null=True, blank=True)


class Section1(models.Model):
    Title = models.CharField(max_length=200, verbose_name='Başlık')
    Text = models.TextField(verbose_name='Metin')


class Section2(models.Model):
    Photo = models.ImageField(null=True, blank=True, verbose_name='Fotoğraf')
    Title = models.CharField(max_length=200, verbose_name='Başlık')
    Text = models.TextField(verbose_name='Metin')


class Section3(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(verbose_name='Metin')


class Section4(models.Model):
    Photo = models.ImageField(null=True, blank=True)
    Text = models.TextField(verbose_name='Metin')


class Section5(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(verbose_name='Metin')


class Footer(models.Model):
    CompanyName = models.CharField(max_length=200,verbose_name='Firma Adı', null=True)
    CompanyLink = models.CharField(max_length=150, verbose_name='Şirket Linki', null=True)
    Text = models.TextField(verbose_name='Adress')
    Mail = models.CharField(max_length=150, verbose_name='Mail Adresi', null=True)
    Phone = models.CharField(max_length=100, verbose_name='Telefon Numarası', null=True)
    
class Message(models.Model):
    Name = models.CharField(max_length=200,verbose_name='Ad SoyAd', null=True)
    Mail = models.CharField(max_length=200, verbose_name='Mail', null=True)
    Messaged = models.TextField(verbose_name='Mesaj')
    def __str__(self):
        return self.Name