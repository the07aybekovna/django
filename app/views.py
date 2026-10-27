from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    return HttpResponse('<h1>Main Page</h1>')

def users(request):
    name = request.GET.get('name')
    surname = request.GET.get('surname')
    age = request.GET.get('age')
    return HttpResponse(
        f'<h1>Users</h1>'
        f'<h3>Name: {name}</h3>'
        f'<h3>Surname: {surname}</h3>'
        f'<h3>Age: {age}</h3>'
    )

def IDfields(request):
    id = request.GET.get('id')
    return HttpResponse(
        f'<h1>IDfields</h1>'
        f'<h3>ID: {id}</h3>'
    )

def address(request):
    address = request.GET.get('address')
    return HttpResponse(
        f'<h1>Address</h1>'
        f'<h3>Address: {address}</h3>'
    )

def email(request):
    email = request.GET.get('email')
    return HttpResponse('<h1>Email</h1>'
                        f'<h3>Email: {email}</h3>'
    )

def phone(request):
    phone = request.GET.get('phone')
    return HttpResponse('<h1>Phone</h1>'
                        f'<h3>Phone: {phone}</h3>')