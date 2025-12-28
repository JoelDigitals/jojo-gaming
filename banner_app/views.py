from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

def banner_view(request):
    return render(request, "banner.html")   