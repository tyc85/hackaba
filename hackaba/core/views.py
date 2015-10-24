from django.shortcuts import render, redirect

# Create your views here.
def task(request):
    return render(request, 'core/task.html')

def landing_page(request):
    return render(request, 'core/landing_page.html')