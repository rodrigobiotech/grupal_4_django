# Generated by Django 4.2.3 on 2023-08-02 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='pais',
            field=models.CharField(default='Chile', max_length=50),
        ),
    ]
