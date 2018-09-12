from django.db import models
from django.utils import timezone

class Domain(models.Model):
    dName = models.CharField(default='', max_length=200, verbose_name='主域名')
    ctime = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    brute = models.BooleanField(default=True)

    def __str__(self):
        return self.dName

class SubDomain(models.Model):
    dName = models.CharField(default='', max_length=200, verbose_name='主域名')
    sdName = models.CharField(default='', max_length=200, verbose_name='子域名')
    ip = models.CharField(default='', max_length=500, verbose_name='解析地址')
    ctime = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    def __str__(self):
        return self.sdName
