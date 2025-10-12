from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "center", "total_amount", "status", "created_at")
    list_filter = ("status", "center")
    inlines = [OrderItemInline]

# Register your models here.
