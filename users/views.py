import json

import requests
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

CLIENT_ID = "n4c4bVXAP2xKjpm8nhd7PZmaqbuL7q4juxXEpwRp"
CLIENT_SECRET = "vPcrx1YEdboDlHAtAHIU2QihYDksL9Wu2u8etSeFVgNANE4Mp8NQx6R2sOZJgZz90x03vQjfanj97zNvEf8Ox3jw84ui5T3h4XRR80DDLZUZehZcJlXy1ZxTkEKaDKLn"


@require_http_methods(["POST"])
@csrf_exempt
def register(request):
    user_name = request.POST.get('user_name')
    email_address = request.POST.get('email_address')
    password = request.POST.get('password')

    user_instance = User(username=user_name, email=email_address)
    user_instance.set_password(password)
    user_instance.save()

    payload = "grant_type=password&client_secret=" + CLIENT_SECRET + "&client_id=" + CLIENT_ID + "&username=" + user_name \
              + "&password=" + password
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
    }

    url = 'http://192.168.0.101:8000/o/token/'

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response)

    return JsonResponse(json.loads(response.content), safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def get_tokens(request):
    payload = "grant_type=password&client_secret=" + CLIENT_SECRET + "&client_id=" + CLIENT_ID + "&username=" + \
              request.POST['user_name'] \
              + "&password=" + request.POST['password']
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
    }

    url = 'http://192.168.0.101:8000/o/token/'

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response)

    return JsonResponse(json.loads(response.content), safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def refresh_token(request):
    payload = "grant_type=refresh_token&client_secret=" + CLIENT_SECRET + "&client_id=" + CLIENT_ID + "&refresh_token=" \
              + request.POST["refresh_token"]
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
    }
    url = 'http://192.168.0.101:8000/o/token/'
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response)

    return JsonResponse(json.loads(response.content), safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def revoke_token(request):
    payload = "client_secret=" + CLIENT_SECRET + "&client_id=" + CLIENT_ID + "&token=" + request.POST["token"]
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
    }
    url = 'http://192.168.0.101:8000/o/revoke_token/'
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response)
    return JsonResponse(json.loads(response.content), safe=False)
