# Generated by Django 5.0.3 on 2024-03-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0002_rename_good_snsmodel_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snsmodel',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='snsmodel',
            name='read',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='snsmodel',
            name='readtext',
            field=models.TextField(blank=True, default='a', null=True),
        ),
    ]
