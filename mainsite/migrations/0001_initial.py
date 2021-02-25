# Generated by Django 3.1.7 on 2021-02-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(blank=True, null=True)),
                ('fname', models.TextField(blank=True, db_column='fName', null=True)),
                ('cname', models.TextField(blank=True, db_column='cName', null=True)),
                ('ename', models.TextField(blank=True, db_column='eName', null=True)),
                ('sname', models.TextField(blank=True, db_column='sName', null=True)),
                ('gname', models.TextField(blank=True, db_column='gName', null=True)),
                ('aname', models.TextField(blank=True, db_column='aName', null=True)),
                ('stem', models.TextField(blank=True, null=True)),
                ('leaf', models.TextField(blank=True, null=True)),
                ('flower', models.TextField(blank=True, null=True)),
                ('fruit', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'plants',
                'managed': False,
            },
        ),
    ]
