from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to first django projects</h1>')