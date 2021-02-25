# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Plants(models.Model):
    url = models.URLField(blank=True, null=True)
    fName = models.TextField(db_column='fName', blank=True, null=True)  # Field name made lowercase.
    cName = models.TextField(db_column='cName', blank=True, primary_key=True, default='')  # Field name made lowercase.
    eName = models.TextField(db_column='eName', blank=True, null=True)  # Field name made lowercase.
    sName = models.TextField(db_column='sName', blank=True, null=True)  # Field name made lowercase.
    gName = models.TextField(db_column='gName', blank=True, null=True)  # Field name made lowercase.
    aName = models.TextField(db_column='aName', blank=True, null=True)  # Field name made lowercase.
    stem = models.TextField(blank=True, null=True)
    leaf = models.TextField(blank=True, null=True)
    flower = models.TextField(blank=True, null=True)
    fruit = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cName

    class Meta:
        db_table = 'plants'
