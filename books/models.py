from django.db import models

# Create your models here.
class Books(models.Model):
	"""docstring for books"""
	id = models.AutoField(primary_key=True)
	image = models.URLField()
	name = models.CharField(max_length=50)
	profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

class Profile(models.Model):
	"""docstrinprice = modelsg for profile"""
	price = models.PositiveSmallIntegerField()
	count = models.PositiveSmallIntegerField()