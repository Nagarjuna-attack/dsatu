from django.shortcuts import render

# Create your views here.

posts = [
	{
		'author':'Muh Ahfandi H',
		'title': 'Blog Post',
		'content':'Ini Adalah Post Pertama',
		'tanggal':'15 February 2021'
	},
	{
		'author':'Muh Ahfandi H',
		'title': 'Blog content',
		'content':'Ini Adalah Post Kedua',
		'tanggal':'16 February 2021'
	},
	{
		'author':'Muh Ahfandi H',
		'title': 'Blog about',
		'content':'Ini Adalah Post Ketiga',
		'tanggal':'17 February 2021'
	}
]

def home(request):
	konteks = {
		'kirim':posts
	}
	return render(request,'blog/home.html',konteks)

def about(request):
	return render(request,'blog/about.html',{'title':'About'})