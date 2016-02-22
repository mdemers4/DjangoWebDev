from __future__ import unicode_literals

from django.db import models
"""
Models: databases tables represented in python code
your handle to:
	create the necessary tables
	generate the SQL to create/read/update/delete databases
	ORM- object relational mapper
importanly:
a model class == databases table.
a model instance == a database table row
"""

class Line(models.Model):
	text = models.CharField(max_length=255) # this stores 255 char

#django will give you an auto primary key if you dont

#python manage.py makemigrations
#python manage.py migrate