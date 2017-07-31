from django.db import models


# Create your models here.
sex_choices=(
    ('f','famale'),
    ('m','male'),
)

class Member(models.Model):
    name = models.CharField(max_length=30)
    sex  = models.CharField(max_length=1, choices=sex_choices)
    headImg = models.FileField(upload_to='/home/kjw/yssite/upload/')

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author)
    bookImg = models.FileField(upload_to='/home/kjw/yssite/upload/')

    def __unicode__(self):
        return self.name