# Generated by Django 3.1.1 on 2020-09-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webburguer_app', '0003_auto_20200915_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burgueruser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]