from django.db import models

# Create your models here.


class BlogPosts(models.Model):
	title = models.TextField()
	slug  = models.SlugField(unique=True)
	content = models.TextField(null = True, blank = True)


