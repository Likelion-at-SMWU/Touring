# Generated by Django 3.0 on 2020-08-30 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourPlan', '0003_plan_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='title',
            field=models.CharField(default='제목', max_length=200),
        ),
    ]