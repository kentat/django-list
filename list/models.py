from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(verbose_name='氏名',max_length=20)
    kana = models.CharField(verbose_name='ひらがな',max_length=20)
    #age = models.IntegerField(default=0)
    age = models.IntegerField()
    birth_date = models.DateField('生年月日')
    sex = models.CharField(verbose_name='性別',max_length=8,blank=True)
    blood_type = models.CharField(max_length=2)
    email = models.EmailField(blank=False, null=True, default='')
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    zip_code = models.CharField(verbose_name='郵便番号',max_length=8,blank=True)
    address = models.CharField(verbose_name='住所',max_length=40,blank=True)
    company = models.CharField(verbose_name='会社',max_length=40,blank=True)
    credit_card = models.CharField(verbose_name='クレジットカード',max_length=19,blank=True)
    expired = models.CharField(verbose_name='期限',max_length=8,blank=True)
    mynumber = models.CharField(verbose_name='マイナンバー',max_length=12,blank=True)

    def __str__(self):
        return str(self.name)
