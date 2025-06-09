from .models import Booking,Menu
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields="__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=['name','no_of_guests','booking_date']