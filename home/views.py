from django.shortcuts import render, HttpResponse

def home_view(request):
    # return render(request, 'home.html', {'isim': 'Barış'})
    if request.user.is_authenticated():
        context = {
            'isim': 'Duygu',
        }
    else:
        context = {
            'isim': 'Misafir',
        }
    return render(request, 'home.html', context)