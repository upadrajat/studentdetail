from __future__ import unicode_literals
from django.db import models
import datetime as dt


mdate= dt.datetime.now()
dur=dt.datetime.now()+dt.timedelta(days=730)

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=20)
    sage=models.IntegerField()
    sgender=models.CharField(max_length=20,default='black')
    

