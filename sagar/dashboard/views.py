from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'AboutUs.html')

def error_404_handler(request,exception):
    print("*********")
    return render(request,'error404.html')