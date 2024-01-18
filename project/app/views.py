from django.shortcuts import render,redirect
from .forms import UrlForm,shortend_url
from .shorten import Shortener

def shorten_url(request):
    form = UrlForm(request.POST)
    token = None

    if request.method == 'POST':
        if form.is_valid():
            new_url = form.save(commit=False)
            token = Shortener().generate_token()
            new_url.short_url = token
            new_url.save()
    else:
        form = UrlForm
        token = "invalid token"
    return render(request,'home.html',{'form':form,'token':token})

def redirect_to_original(request,token):
    long_url = shortend_url.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)
