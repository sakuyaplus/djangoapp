from django.shortcuts import render
import random
import time
# Create your views here.
def index(request):
    nowtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    day=int(time.strftime("%Y%m%d"))
    random.seed(day)
    print(nowtime)
    randomnumber=random.randint(1,100)
    return render(request, 'index.html', {'item': randomnumber, 'time': nowtime})