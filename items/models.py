from django.db import models

# Create your models here.
class Item(object):

    def __init__(self):
        self.title = ""
        self.image_url = ""
        self.item_url  = ""

    def get_item_list(self):

        pass
