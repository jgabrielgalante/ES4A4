import re

from django.db import models

def gen_slug(title):
    p = re.compile('\W', re.IGNORECASE)
    return p.sub('-', title).lower().strip()

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        ret = None
        try:
            ret = Thread.objects.get(slug=self.slug)
        except Thread.DoesNotExist:
            ret = super().save(*args, **kwargs)
        return ret

class Comment(models.Model):
    author_email = models.EmailField()
    content = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

