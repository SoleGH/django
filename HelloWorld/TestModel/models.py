from django.db import models

# Create your models here.
class Test(models.Model): #class 对应数据库中的一个表
    name = models.CharField(max_length=20) #calss的属性与表属性意义对应

