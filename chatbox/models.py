from django.db import models

# Create your models here.
class Message(models.Model):
	title = models.CharField(max_length=30)
	message = models.TextField(max_length=500)
	post_time = models.DateTimeField(auto_now_add=True)
	poster_name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.title