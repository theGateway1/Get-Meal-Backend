from django.db import models

# Create your models here.
class Menu(models.Model):
    i1 = models.TextField(blank=True,default='Cur Null',editable=True)
    i2 = models.TextField(blank=True,default='Cur Null',editable=True)
    i3 = models.TextField(blank=True,default='Cur Null',editable=True)
    i4 = models.TextField(blank=True,default='Cur Null',editable=True)
    i5 = models.TextField(blank=True,default='Cur Null',editable=True)
    i6 = models.TextField(blank=True,default='Cur Null',editable=True)
    i7 = models.TextField(blank=True,default='Cur Null',editable=True)
    i8 = models.TextField(blank=True,default='Cur Null',editable=True)
    updated = models.TextField(blank=True,default='0000',editable=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.i1[0:50]

    class Meta:
        ordering = ['-created']