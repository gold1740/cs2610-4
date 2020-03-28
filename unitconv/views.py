from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from unitconv.models import Unit
# Create your views here.

def convert(request):
	get = request.GET.copy()
	if ('from' in get):
		get['start'] = get.pop('from')
	if ('to' in get):
		get['end'] = get.pop('to')
	if(not ('start' in get and 'end' in get and 'value' in get)):
		return JsonResponse({'error': 'Insufficient data provided'})
	if type(get['end']) is list:
		get['end'] = get['end'][0] 
	if type(get['start']) is list:
		get['start'] = get['start'][0] 

	if get['end'] == "T":
		get['end'] = "tons"
	elif get['end'] == "g":
		get['end'] = "grams"
	elif get['end'] == "t_oz":
		get['end'] = "troy ounces"
	elif get['end'] == "kg":
		get['end'] = "kilograms"
	elif get['end'] == "lb":
		get['end'] = "pounds"
	elif get['end'] == "oz":
		get['end'] = "dry ounces"

	if get['start'] == "T":
		get['start'] = "tons"
	elif get['start'] == "g":
		get['start'] = "grams"
	elif get['start'] == "t_oz":
		get['start'] = "troy ounces"
	elif get['start'] == "kg":
		get['start'] = "kilograms"
	elif get['start'] == "lb":
		get['start'] = "pounds"
	elif get['start'] == "oz":
		get['start'] = "dry ounces"

	if type (get['value']) is list:
		value = get['value'][0]
	else:
		value = get['value']
	
	start = None
	end = None
	for unit in Unit.objects.all():
		if (unit.name == get['start']):
			start = unit.conversion_rate
			break
	
	for unit in Unit.objects.all():
		if (unit.name == get['end']):
			end = unit.conversion_rate
			break
	if (start == None or end == None):
		return JsonResponse({'error': 'Invalid units'})
	return JsonResponse({'conversion':float(value) * float(start / end), 'units': get['end']})


