from django.db import models

# Create your models here.

class Articles(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']