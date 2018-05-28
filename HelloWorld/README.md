# python django 使用
## 创建新项目 __projectName__
```
$ django-admin startproject ProjectName #自动生成项目基本文件
```

## 添加model并生成数据库表
## 添加model
```
$ python manage.py startapp ModelName #在manage.py同目录下生成ModelName文件夹及相应的文件
```
* 在 __ModelName/__ 文件夹中的 __models.py__
```
from django.db import models

# Create your models here.
class Test(models.Model): #class 对应数据库中的一个表
    name = models.CharField(max_length=20) #calss的属性与表属性意义对应

```
### 将 `ModelName` 添加到配置文件 __settings.py__
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ModelNmae',               # 添加生成的ModelName（默认通文件夹名）
)
```

### 根据已有 `model` 生成数据库表指令
```
$ python manage.py migrate #创建Django默认表
$ python manage.py makemigrations modelName #告知django MODEL已经变更
$ python manage.py migrate modelName # 创建model对应的数据库表
```