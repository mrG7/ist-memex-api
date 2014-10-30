from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

import json
import settings

@api_view(['GET'])
def index(request):
    response = {"version":settings.MEMEX_API_VERSION}
    return Response(response)

def debug(request):
    response = {
    }
    return HttpResponse(json.dumps(response, indent=2), content_type="application/json")

class LogList(APIView):
    def get(self, request, format=None):
        response = {'type':'GET'}
        return Response(response)
    def post(self, request, format=None):
        response = {'type':'POST'}
        return Response(response)
        
class LogItem(APIView):
    def get(self, request, key, format=None):
        response = {'type':'GET'}
        return Response(response)
    def put(self, request, key, format=None):
        response = {'type':'PUT'}
        return Response(response)
    def patch(self, request, key, format=None):
        response = {'type':'PATCH'}
        return Response(response)
    def delete(self, request, key, format=None):
        response = {'type':'DELETE'}
        return Response(response)

class LogSearch(APIView):
    def get(self, request, index, value=None, prefix=None, start=None, end=None, format=None):
        response = {'type':'GET'}
        return Response(response)
