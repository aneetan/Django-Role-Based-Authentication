from django.shortcuts import render

def userPage(request):
    context = {}
    return render(request, 'user.html')