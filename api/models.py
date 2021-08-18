from django.db import models

# Create your models here.
class Menu(models.Model):
    body = models.TextField(blank=True,default='Cur Null',editable=True)
    updated = models.TextField(blank=True,default='0000',editable=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-created']