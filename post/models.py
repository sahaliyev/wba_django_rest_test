from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by_user')
    title = models.CharField(max_length=200)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    slug = models.SlugField(unique=True, max_length=200, editable=False)
    image = models.ImageField(upload_to='post', null=True, blank=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='modified_by_user')

    def get_slug(self):
        replace_dict = {'ə': 'e', 'ı': 'i', 'ö': 'o', 'ğ': 'g', 'ş': 's'}
        for item in replace_dict.keys():
            if item in self.title:
                self.title = self.title.replace(item, replace_dict.get(item))

        if self.id:
            return self.slug

        if not self.id:
            slug = slugify(self.title)
            unique = slug

            number = 1
            while Post.objects.filter(slug=unique).exists():
                unique = f"{slug}-{number}"
                number += 1
            return unique

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()

        self.modified = timezone.now()
        self.slug = self.get_slug()
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
