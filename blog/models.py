from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=10)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=80, null=False)
    excerpt = models.CharField(max_length=250, null=False)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True,
                            null=False, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
