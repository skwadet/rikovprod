from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, default='Video')
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return 'Tag N: {id}, name: {text}'.format(id=self.id, text=self.name)


class Video(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = AutoSlugField(populate_from='title')
    tag = models.ManyToManyField(Tag, related_name='videos')
    embedded_url = models.URLField(max_length=200)
    preview_image = models.FileField(upload_to='previews/')

    def __str__(self):
        return 'Video N: {id}, title: {title}'.format(id=self.id, title=self.title)


class Photo(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, default=None)
    image = models.FileField(upload_to='photos/')

    def __str__(self):
        return 'Photo N: {id}, title: {title}'.format(id=self.id, title=self.title)


class VacantDate(models.Model):
    date = models.DateField(default=timezone.now, null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.date)


CALLEDSTATUTES = [
    ('c', 'called'),
    ('n', 'notcalled'),
]


class Session(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    # I'm so sorry for this thing, but it was only way to make unique sessions
    freedate = models.ForeignKey(VacantDate, related_name='sessions', unique=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(default=None, null=True, blank=False)
    is_busy = models.BooleanField(default=True)
    callstatus = models.CharField(default='n', max_length=1, choices=CALLEDSTATUTES)

    def __str__(self):
        return 'Session N: {id}, for: {title}'.format(id=self.id, title=self.name)
