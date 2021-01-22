from django.shortcuts import render

from django.http import HttpResponse
from faker import Faker

# Create your views here.

fake = Faker()


def name(request):
    return HttpResponse(fake.name())


def address(request):
    return HttpResponse(fake.address())
