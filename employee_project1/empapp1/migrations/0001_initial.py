# Generated by Django 4.0.6 on 2022-08-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=50)),
                ('empcontact', models.BigIntegerField()),
                ('deptemail', models.EmailField(max_length=50)),
            ],
        ),
    ]