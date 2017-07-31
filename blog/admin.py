from django.contrib import admin
from blog.models import Member
from blog.models import Author,Books

admin.site.register(Member)

admin.site.register(Author)
admin.site.register(Books)