from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html',)


def about(request):
    return render(request, 'main/about.html',)


def about_prices(request):
    return render(request, 'main/about_prices.html',)


def abstract(request):
    return render(request, 'main/abstract.html',)


def authors(request):
    return render(request, 'main/authors.html',)


def basket(request):
    return render(request, 'main/Basket.html',)


def bookinisted(request):
    return render(request, 'main/BOOKINISTED.html',)


def cd_and_dvd(request):
    return render(request, 'main/CDandDVD.html',)


def contacts(request):
    return render(request, 'main/contacts.html',)


def feedback(request):
    return render(request, 'main/feedback.html',)


def month(request):
    return render(request, 'main/month.html',)


def order(request):
    return render(request, 'main/order.html',)


def subscription(request):
    return render(request, 'main/subscription.html',)


def tags(request):
    return render(request, 'main/tags.html',)


def theonlyone(request):
    return render(request, 'main/THEONLYONE.html',)

