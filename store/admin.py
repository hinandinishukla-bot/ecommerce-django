from django.contrib import admin
from .models import Category, Medicine, Supplier, Customer, Purchase, Sale

admin.site.register(Category)
admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Sale)
