from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    # CHOICES = (
    #     ('A', 'Statue'),
    #     ('B', 'Tower'),
    # )
    # type = models.CharField(max_length=100, choices=CHOICES, default='A', help_text='Type of your structure')

    # on_delete options: 1.models.CASCADE 2.models.SET_NULL 3.models.SET_DEFAULT 4.models.PROTECT 5.models.DO_NOTHING
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ManyToManyField(Category)

    title = models.CharField(max_length=200, unique=True, null=False, blank=False, help_text='Title of your post',
                             unique_for_date='pub_date')

    content = models.TextField()

    image = models.ImageField(upload_to="images/posts", db_column='image', null=False, blank=False,
                              help_text='Image of your post')

    created = models.DateTimeField(auto_now_add=True, editable=False)

    updated = models.DateTimeField(auto_now=True)

    pub_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title
