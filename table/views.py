import random

from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'table/task1.html', {})


def get_data(request, size):
    data = [{"id": "Идентификатор", "name": "Название", "price": "Стоимость", "quantity": "Количество"}]

    letters = 'abcdefghijklmnopqrstuvwxyz'

    if size == 'big':
        for i in range(1,71):
            data.append([i, random.choice(letters), i * i, i])

    elif size == 'small':
        for i in range(1,6):
            data.append([i, random.choice(letters), i * i, i])
    elif size == 'custom':
        for i in range(1,21):
            data.append([i, random.choice(letters), i * i, i])

    return JsonResponse({"data": data})
