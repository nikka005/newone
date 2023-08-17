from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class contesthome(models.Model):
    s_img1 = models.ImageField(upload_to="contest")
    s_img2 = models.ImageField(upload_to="contest")
    s_img3 = models.ImageField(upload_to="contest")

    con_name = models.CharField(max_length=120)
    con_des = models.TextField(max_length=500)
    entry_fees = models.IntegerField()
    winng_prize = models.IntegerField()
    start_con = models.DateField(max_length=30,)
    end_con = models.DateField(max_length=30,)



# class Jioncontest(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
#     img_frist = models.ImageField(upload_to='jioncontest')
#     img_Second = models.ImageField(upload_to='jioncontest')
#     img_Thrid = models.ImageField(upload_to='jioncontest')
#     img_four = models.ImageField(upload_to='jioncontest')
#     img_five = models.ImageField(upload_to='jioncontest')
#     jion_des = models.TextField(max_length=500)



# class Wallet(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)



