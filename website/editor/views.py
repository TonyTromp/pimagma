from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import *
from django.views.generic import View

# Create your views here.
def index(request):
    template = loader.get_template('index.html');
    L1_entries = L1StrategicalThreat.objects.all()
    context = {
        'text': 'Hello World',
        'l1': L1_entries
    }
    return HttpResponse( template.render(context, request) );

def get_strategical_objects(request, *args, **kwargs):
    dictionaries = [ obj.as_dict() for obj in L1StrategicalThreat.objects.all() ]
    return JsonResponse( dictionaries, safe=False );

def get_tactical_objects(request, *args, **kwargs):
    dictionaries = [ obj.as_dict() for obj in L2TacticalThreat.objects.all() ]
    return JsonResponse( dictionaries, safe=False );

def get_operational_objects(request, *args, **kwargs):
    dictionaries = [ obj.as_dict() for obj in L3OperationalThreat.objects.all() ]
    return JsonResponse( dictionaries, safe=False );

class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})