from django.db import models

# Create your models here.
class Post(models.Model):
	"""docstring for Post"""
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField()
	text = models.TextField()


	def __unicode__(self):
		return self.title
		