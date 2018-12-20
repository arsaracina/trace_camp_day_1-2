from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from polls.models import Kickstarter

def get_kickstarter(request,kick_id):
    kick= Kickstarter.object.filter(id=kick_id)
    response= serializers.serialize("json",kick)
    return HttpResponse(response)


# Create your views here.
#from kick2.models import KickStarter

# Create your views here.
#def get_kickstarter(request, kick_id):
#    kick = KickStarter.objects.filter(id = kick_id)
#    response = serializers.serialize("json", kick)
#    return HttpResponse(response)
