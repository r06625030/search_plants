# Generated by Django 3.1.7 on 2021-02-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20210224_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plants',
            name='id',
        ),
        migrations.AlterField(
            model_name='plants',
            name='cname',
            field=models.TextField(blank=True, db_column='cName', default='', primary_key=True, serialize=False),
        ),
    ]
