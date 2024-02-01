from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import ApiUser, Room, Booking, Hotel
from api.serializers import UserSerializer, RoomSerializer, BookingSerializer, HotelSerializer


# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'path', 'get']
    serializer_class = UserSerializer


class HotelModelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    # @action(detail=True)
    # def rooms(self, request, pk=None):
    #     hotel = get_object_or_404(Hotel.objects.all(), id=pk)
    #     free_rooms = hotel.rooms.filter(bookings_isnull=True)
    #     return Response(
    #         RoomSerializer(free_rooms, many=True).data
    #     )
    @action(detail=True)
    def rooms(self, request, pk=None):
        hotel = get_object_or_404(Hotel.objects.all(),id=pk)
        free_rooms = hotel.rooms.filter(bookings=None)
        return Response(RoomSerializer(free_rooms, many=True).data)


class RoomModelViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingModelViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
