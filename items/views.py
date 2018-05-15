from django.shortcuts import render
from dev_best10.settings import *
from .amazon_models import Item


# Home Page
def item_list(request):
    item = Item()
    search_result = item.get_items(q_word='startup')
    context = {
        "item_list": search_result
    }
    return render(request,'items/item_list.html', context)
