# Generated by Django 4.1.6 on 2023-08-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contestoverviwes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_img', models.ImageField(upload_to='contest')),
                ('con_name', models.CharField(max_length=120)),
                ('con_des', models.CharField(max_length=500)),
                ('entry_fees', models.IntegerField(max_length=20)),
                ('winng_prize', models.IntegerField(max_length=30)),
                ('start_con', models.DateField(max_length=30)),
                ('end_con', models.DateField(max_length=30)),
            ],
        ),
    ]
