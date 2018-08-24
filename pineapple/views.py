from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from .models import Orders
from django.core.serializers import serialize
import json

def index(request):
    return HttpResponse("Hello, world.")


def order(request, order_id):
    try:
        order = Orders.objects.get(internal_id=order_id)
        order_record = serialize('json', [order, ])
        return HttpResponse(order_record, content_type="application/json")
    except ObjectDoesNotExist as e:
        return HttpResponseNotFound(f'Record with internal id {order_id} does not exist')
