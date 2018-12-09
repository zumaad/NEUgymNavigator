from django.shortcuts import render, redirect
from django.http import HttpResponse
from marinoApp.models import *


# Create your views here.

def home_page(request):
    if request.method == 'POST':
        return render(request, 'home.html')
    return render(request, 'home.html')


#returns an instances of LocationEquipment with equipment that works out the given bodypart
def button_queries(bodypart):
    equipment_for_bodypart = EquipmentBodyPartsTargeted.objects.filter(body_parts_targeted__name=bodypart)
    equipment_set = {entry.equipment.name for entry in equipment_for_bodypart}
    filtered_query_list = []
    for entry in LocationEquipment.objects.all():
        if entry.equipment.name in equipment_set:
            filtered_query_list.append(entry)
    return filtered_query_list



def navigation(request):
    all_equipment = Equipment.objects.all()

    return render(request, 'navigation.html',
                  {'all_equipment':all_equipment})


def retrieve(request):
    if request.method == 'GET':
        return redirect('/navigation')
    else:
        bodypart = request.POST['bodypart']
        Equipment_for_bodypart = EquipmentBodyPartsTargeted.objects.filter(body_parts_targeted__name=bodypart)


        return render(request,'renderingUniques.html',
                      {'Equipment_for_bodypart':Equipment_for_bodypart,
                       'bodypart':bodypart})

def all(request):
    if request.method == 'GET':
        return redirect('/navigation')
    else:
        equipment_name = request.POST['equipmentName']
        all_instances_equipment = LocationEquipment.objects.filter(equipment__name=equipment_name)
        if len(all_instances_equipment) < 1:
            return HttpResponse("<p> you searched: " + equipment_name + "</p>" + "<p>" + equipment_name + " is not in the database</p>")
        return render(request,'renderingDuplicates.html',
                      {'equipment_name':equipment_name,
                       'all_instances_equipment':all_instances_equipment})

