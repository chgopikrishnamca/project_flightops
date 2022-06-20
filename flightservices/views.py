from django.shortcuts import render
from rest_framework import viewsets
from flightservices.models import FlightDetailsModel, PassengerDetailsModel, ReservationModel
from flightservices.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer

"""Defining Viewsets"""

class FlightViewSet(viewsets.ModelViewSet):
    serializer_class = FlightSerializer
    queryset = FlightDetailsModel.objects.all()


class PassengerViewSet(viewsets.ModelViewSet):
    serializer_class = PassengerSerializer
    queryset = PassengerDetailsModel.objects.all()


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = ReservationModel.objects.all()