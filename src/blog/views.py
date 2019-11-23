from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import BlogPosts

#CRUD

#GET  --> Retrieve / list
#POST --> Create / Update / DELETE

def blog_post_list_view(request):
	#List objects
	#could be search
	qs = BlogPosts.objects.all() #QuerySet  -> list of python objects
	template_name='blog_post_list.html'
	context = { 'object_list':qs}
	return render(request,template_name,context)

def blog_post_create_view(request):
	#Create object
	# ? use a form
	template_name='blog_post_create.html'
	context = { 'form':None}
	return render(request,template_name,context)	

def blog_post_detail_view(request,slug):
	#1 object -> detail view
	obj = get_object_or_404(BlogPosts,slug=slug)
	template_name = 'blog_post_detail.html'
	context = {"object":obj}
	return render(request,template_name,context)

def blog_post_update_view(request):
	obj = get_object_or_404(BlogPosts,slug=slug)
	template_name = 'blog_post_update.html'
	context = {"object":obj,'form':None}
	return render(request,template_name,context)

def blog_post_delete_view(request):
	obj = get_object_or_404(BlogPosts,slug=slug)
	template_name = 'blog_post_delete.html'
	context = {"object":obj}
	return render(request,template_name,context)
