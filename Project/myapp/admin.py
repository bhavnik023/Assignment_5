from django.contrib import admin
from . models import ProductMaster, ProductSubCategory

# Register your models here.
admin.site.register(ProductMaster)
admin.site.register(ProductSubCategory)