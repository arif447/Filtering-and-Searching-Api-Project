from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(Ingredient)
admin.site.register(CustomerDetail)