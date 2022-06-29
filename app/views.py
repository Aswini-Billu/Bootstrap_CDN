from django.shortcuts import render

# Create your views here.
def bootstrap(request):
    return render(request,'bootstrap-cdn.html')
def bootstrap_download(request):
    return render(request,'bootstrao_download.html')
