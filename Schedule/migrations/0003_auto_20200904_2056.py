# Generated by Django 3.0 on 2020-09-04 11:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0002_auto_20200904_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='schedule',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='일정'),
        ),
    ]