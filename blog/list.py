from blog.models import Author,Books
from django.shortcuts import render_to_response

def index(req):
    authors = Author.objects.all()
    return render_to_response('list.html',{'authors':authors})