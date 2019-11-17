from django.conf import settings
from django.shortcuts import render
# from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP


def home(request):
    return render(request, 'home.html')

# from django.shortcuts import render
# from django.http import HttpResponse
#
# from .models import Greeting
#
# # Create your views here.
# def index(request):
#     return HttpResponse('Noemie & Ruizhi - Coming soon!')
#     return render(request, "index.html")
#
#
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
