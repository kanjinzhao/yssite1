from django import forms
from django.http import  HttpResponse
from django.shortcuts import render_to_response

class UserForm(forms.Form):
    name = forms.CharField()
    passwd = forms.CharField()
    headImg = forms.FileField()

def index(req):
    if req.method == 'POST':
        form = UserForm(req.POST,req.FILES)

        if form.is_valid():
            print form.cleaned_data
            fp = file('/home/lmb/yssite/upload/'+form.cleaned_data['headImg'].name,'wb')
            s = form.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
            return HttpResponse('OK')

    else:
        form = UserForm()
    return  render_to_response('reg.html',{'form':form})