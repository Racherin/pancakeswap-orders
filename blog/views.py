from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        "myword": "Saat 21:24:42",
        "title": "Anasayfa"
    }
    return render(request, "index.html", context=context)
