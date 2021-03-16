from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
	konteks = {
		'kirim':Post.objects.all().order_by('-tanggal'),
		'title':'Home'
	}
	return render(request,'blog/home.html',konteks)

def about(request):
	return render(request,'blog/about.html',{'title':'About'})