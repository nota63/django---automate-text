from django.http import HttpResponse
from django.shortcuts import render
import pyautogui as pg
import time


def automate(request):
    warning = ''
    if request.method == 'POST':
        respone = request.POST.get('msg')
        warning = "your programme would be start in 5 seconds"
        time.sleep(5)
        for i in range(1000):
            pg.write(respone)
            time.sleep(0.5)
            pg.press("Enter")

    return render(request, 'automate.html', {'warning': warning})
