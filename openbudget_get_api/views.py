from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse


# Create your views here.

def home(request):
    return render(request, "home.html")

def exam(request):
    print("salom1111")
    if request.method == 'POST':
        application = request.POST.get('application')
        phone = request.POST.get('phone')
        print(application)
        print(phone)

        endpoint = "https://admin.openbudget.uz/api/v1/user/validate_phone/"
        data = {
            "application": application,
            "phone": phone
        }
        get_response = requests.post(endpoint, json=data, verify=False)

        print(get_response.json(), get_response.status_code)

        df = get_response.json()
        df['code'] = get_response.status_code

        response = JsonResponse(df)

    return response


def home1(request):
    print("salom11112222")
    if request.method == 'POST':
        application = request.POST.get('application')
        phone = request.POST.get('phone')
        otp = request.POST.get('otp')
        token = request.POST.get('token')
        print(application)
        print(phone)

        endpoint = "https://admin.openbudget.uz/api/v1/user/temp/vote/"
        data = {
            "application": "124483",
            "otp": otp,
            "phone": phone,
            "token": token
        }
        get_response = requests.post(endpoint, json=data, verify=False)

        print(get_response.json(), get_response.status_code)

        df = get_response.json()
        df['code'] = get_response.status_code

        response = JsonResponse(df)

    return response
