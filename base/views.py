from django.shortcuts import render

# home --01
def home(request):
    context = {}
    return render(request, 'base/home.html', context)

# about --02 
def about(request):
    context = {}
    return render(request, 'base/about.html', context)

# services --03
def services(request):
    context = {}
    return render(request, 'base/services.html', context)

# services --04
def service(request):
    context = {}
    return render(request, 'base/service.html', context)

# teams --05
def teams(request):
    context = {}
    return render(request, 'base/teams.html', context)

# frequently asked questions --06
def faqs(request):
    context = {}
    return render(request, 'base/faqs.html', context)

# blogs --07
def blogs(request):
    context = {}
    return render(request, 'base/blogs.html', context)

# blog --08
def blog(request):
    context = {}
    return render(request, 'base/blog.html', context)

# contacts --09
def contacts(request):
    context = {}
    return render(request, 'base/contacts.html', context)