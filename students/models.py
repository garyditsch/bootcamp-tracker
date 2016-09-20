from django.db import models
from django.core.urlresolvers import reverse


class Student (models.Model):
    last_name = models.CharField(max_length = 200)
    first_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse ("students:detail", kwargs={"id":self.pk})


