from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	url = models.CharField(max_length=50,default='SOME STRING')
	isi = RichTextField(blank=True,null=True)
	tanggal = models.DateTimeField(auto_now_add=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})