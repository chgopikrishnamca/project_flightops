from rest_framework import serializers
from flightservices.models import FlightDetailsModel, PassengerDetailsModel, ReservationModel

class FlightSerializer(serializers.ModelSerializer):
    """ Flight Serializer"""
    class Meta:
        model = FlightDetailsModel
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    """ Passenger Serializer"""
    class Meta:
        model = PassengerDetailsModel
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationModel
        fields = '__all__'
