from django.db import models
from django.forms import ModelForm

# Create your models here.
class Message(models.Model):
	title = models.CharField(max_length=30)
	message = models.TextField(max_length=500)
	post_time = models.DateTimeField(auto_now_add=True)
	poster_name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.title
		
class MessageForm(ModelForm):
     class Meta:
         model = Message