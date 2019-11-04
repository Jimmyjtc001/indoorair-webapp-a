from django.shortcuts import render
from django.http import JsonResponse

def create_page(request):
    return render(request, "instrument/create.html",{},)

def retrieve_page(request):
    return render(request, "instrument/retrieve.html",{},)

def update_page(request):
    return render(request, "instrument/update.html",{},)

def list_page(request):
    return render(request, "instrument/list.html",{},)


def create_api(request):

  return JsonResponse({

       })
def retrieve_api(request):

  return JsonResponse({

       })
def update_api(request):

  return JsonResponse({

       })
def list_api(request):

  return JsonResponse({

       })
