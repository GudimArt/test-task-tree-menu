from django.shortcuts import render

def home(request):
    return render(request, 'home.html', locals())


def order(request, url_to_process):
    return render(request, 'order.html', locals())