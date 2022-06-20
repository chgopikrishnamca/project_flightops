from django.db import models
from rest_framework.response import Response


def ValidateFields(passengerPhone):
    if len(passengerPhone)!=10:
        return Response("Conatct Number Invalid")

class FlightDetailsModel(models.Model):
    """ Flight Details Model"""
    flightNum = models.IntegerField()
    flightService = models.CharField(max_length=30)
    flightArrivalTime = models.DateTimeField()
    flightDepartureTime = models.DateTimeField()
    flightSource = models.CharField(max_length=20)
    flightDestination = models.CharField(max_length=20)
    flightTravelDuration = models.IntegerField(default=2)

class PassengerDetailsModel(models.Model):
    """ Passenger Details Model"""
    passengerName = models.CharField(max_length=30)
    passengerEmail = models.EmailField()
    passengerPhone = models.IntegerField()

class ReservationModel(models.Model):
    flight = models.OneToOneField(FlightDetailsModel, on_delete=models.CASCADE)
    passenger = models.OneToOneField(PassengerDetailsModel, on_delete=models.CASCADE)
