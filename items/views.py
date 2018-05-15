from django.shortcuts import render
from dev_best10.settings import *
# Create your views here.


# Home Page
def item_list(request):
    print(BASE_DIR)
    return render(request,'items/item_list.html')
