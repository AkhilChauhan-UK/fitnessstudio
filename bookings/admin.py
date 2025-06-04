# bookings/admin.py
from django.contrib import admin
from .models import FitnessClass, Booking

@admin.register(FitnessClass)
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_time', 'instructor', 'available_slots')
    search_fields = ('name', 'instructor')
    list_filter = ('date_time', 'instructor')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'fitness_class', 'booked_at')
    search_fields = ('client_name', 'client_email', 'fitness_class__name')
    list_filter = ('fitness_class', 'booked_at')
