from django.db import models

from django.core.urlresolvers import reverse


class Pullup (models.Model):
    pullups = models.IntegerField()
