from django.shortcuts import render


def base(request):
    return render(request, 'home.html', {'title': 'Vasu Thopuri'})


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def skills(request):
    return render(request, 'skills.html', {'title': 'Skills'})


def contact(request):
    return render(request, 'contact.html', {'title': 'contact'})
