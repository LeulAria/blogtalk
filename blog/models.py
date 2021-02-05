from django.db import models
from django.contrib.auth.models import User

STATUS = ( (0, "Draft"), (1, "Publish") )

class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    tags = models.ManyToManyField("Tag", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    class Meta:
        ordering = ['tag_name']

    def __str__(self):
        return self.tag_name
