# from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    responseData = {
        'id': 1,
        'name': 'Nolan',
        'passord': 'not yet defined'
    }
    return JsonResponse(responseData)

