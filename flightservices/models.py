from django.db import models
from rest_framework.response import Response

def calculateTime(flightDepartureTime, flightArrivalTime):
    """ To Calculate the number of hours and days between the given dates and times. For now, giving manual value."""
    flightTravelDuration = 2
    return flightTravelDuration

def ValidateFields(passengerPhone):
    if len(passengerPhone)!=10:
        return Response("Conatct Number Invalid")


class FlightDetailsModel(models.Model):
    """ Flight Details Model"""
    flightNum = models.IntegerField(max_length=10)
    flightService = models.CharField(max_length=30)
    flightArrivalTime = models.DateTimeField()
    flightDepartureTime = models.DateTimeField()
    flightSource = models.CharField(max_length=20)
    flightDestination = models.CharField(max_length=20)
    flightTravelDuration = calculateTime(flightDepartureTime, flightArrivalTime)

class PassengerDetailsModel(models.Model):
    """ Passenger Details Model"""
    passengerName = models.CharField(max_length=30)
    passengerEmail = models.EmailField(Null=False)
    passengerPhone = models.IntegerField(max_length=10)

class ReservationModel(models.Model):
    flight = models.oneToOneField(FlightDetailsModel, on_delete=models.CASCADE)
    passenger = models.OneToOneField(PassengerDetailsModel, on_delete=models.CASCADE)
