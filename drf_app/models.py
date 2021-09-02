from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)


class Seminar(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    users = models.ManyToManyField(User)


class Section(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    seminar = models.ForeignKey(Seminar, on_delete=models.DO_NOTHING)


class SubSection(models.Model):
    TEXT = 'TXT'
    VIDEO = 'VID'
    CONTENT_CHOICES = [
        (TEXT, 'Text'),
        (VIDEO, 'Video'),
    ]
    content_type = models.CharField(
        max_length=3,
        choices=CONTENT_CHOICES,
    )
    content = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
