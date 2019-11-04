from django.shortcuts import render
from django.http import JsonResponse

def dashboard_page(request):
  return render(request, "dashboard/dashboard.html",{},)

def dashboard_api(request):

  temp_average = request.POST.get("temp_average")
  press_average = request.POST.get("press_average")
  co2_average = request.POST.get("co2_average")
  tvoc_average = request.POST.get("tvoc_average")
  humidity_average = request.POST.get("humidity_average")


  return JsonResponse({
       "temp_average": temp_average,
       "press_average":press_average,
       "co2_average":co2_average,
       "tvoc_average":tvoc_average,
       "humidity_average":humid_average,

  })
