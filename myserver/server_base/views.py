from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth import authenticate
import json
# Create your views here.

last_session = ""

def cookies_view(request: WSGIRequest):
  global last_session
  print(request.session.get('sessionid'))

  print(request.session.session_key)
  print(request.session.serializer)
  prev = last_session
  a = json.dumps({"sessionid": prev})
  last_session = request.session.session_key
  response = HttpResponse(f"{a}")
  response['Access-Control-Allow-Credentials'] = "true"
  return response