

# Register your models here.

# Register your models here.
from django.contrib import admin
from .models import Menu, Booking


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'price', 'inventory')
    # Add search functionality
    search_fields = ('title',)
    # Add filters in the sidebar
    list_filter = ('price', 'inventory')
    # Order results by title
    ordering = ('title',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_of_guests', 'bookingDate')
    search_fields = ('name',)
    list_filter = ('bookingDate', 'no_of_guests')
    ordering = ('bookingDate',)
