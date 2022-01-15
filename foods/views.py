from django.shortcuts import render
from datetime import datetime
from foods.models import Menu

# Create your views here.
def index(request):
    context = dict()
    today = str(datetime.today().date())
    context['date'] = today
    menus = Menu.objects.all()
    context['menus'] = menus
    return render(request, 'foods/index.html', context = context)

def detail(request,pk):
    menu = Menu.objects.get(id = pk)
    context = {'menu' : menu}
    return render(request, 'foods/detail.html', context = context)