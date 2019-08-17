from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(request):
    data = {
        "title": "Create"
    }
    return render(request, "index.html", data)

def post_detail(request):
    data = {
        "title": "Detail"
    }
    return render(request, "index.html", data)

def post_list(request):
    if request.user.is_authenticated:
        data = {
            "title": "List and user is logged in"
        }
    else:
        data = {
            "title": "List and user is logged out"
        }

    return render(request, "index.html", data)

def post_update(request):
    data = {
        "title": "Update"
    }
    return render(request, "index.html", data)

def post_delete(request):
    data = {
        "title": "Delete"
    }
    return render(request, "index.html", data)