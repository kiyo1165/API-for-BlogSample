from django.db import models
from auth_api.models import User


def upload_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['images', str(instance.title) + str(".") + str(ext)])

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Blog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=300)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    image = models.ImageField(blank=True, null=True, upload_to=upload_image_path, default='estlove.jpeg')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # default = 'estlove.jpeg'