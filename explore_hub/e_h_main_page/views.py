from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

import random

# Create your views here.
def home(request):
    numbers = [0, 1, 2, 3, 4, 5]
    value = numbers[random.randint(0, 5)]
    print(value)
    return render(request, 'e_h_main_page/e_h_main_page.html', {
        'magic_number': value
    })