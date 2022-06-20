from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from flightservices.models import FlightDetailsModel, PassengerDetailsModel, ReservationModel
from flightservices.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer

"""Defining Viewsets"""

@api_view(['POST', 'GET'])
def findFlights(request):
    flights = FlightDetailsModel.objects.filter(flightDestination=request.data['flightDestination'], flightDepartureTime=request.data['flightDepartureTime'])
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer)

class FlightViewSet(viewsets.ModelViewSet):
    serializer_class = FlightSerializer
    queryset = FlightDetailsModel.objects.all()


class PassengerViewSet(viewsets.ModelViewSet):
    serializer_class = PassengerSerializer
    queryset = PassengerDetailsModel.objects.all()


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = ReservationModel.objects.all()