from django.shortcuts import render
from .models import Item
from django.http import HttpResponse
# Create your views here.

def item_list(request):
    context={
        "items":Item.objects.all()
    }
    # context='Hello'
    return render(request, "home-page.html", context)

# def item_list(request):
#     html='Nitin'
#     return HttpResponse(html)