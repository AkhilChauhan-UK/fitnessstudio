from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
import datetime  # Make sure you have this for datetime filtering

@api_view(['GET'])
def get_classes(request):
    classes = FitnessClass.objects.filter(date_time__gte=datetime.datetime.now())
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_class(request):
    class_id = request.data.get('class_id')
    client_name = request.data.get('client_name')
    client_email = request.data.get('client_email')

    try:
        fitness_class = FitnessClass.objects.get(id=class_id)
    except FitnessClass.DoesNotExist:
        return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)

    if fitness_class.available_slots <= 0:
        return Response({'error': 'No slots available'}, status=status.HTTP_400_BAD_REQUEST)

    booking = Booking.objects.create(
        fitness_class=fitness_class,
        client_name=client_name,
        client_email=client_email
    )
    fitness_class.available_slots -= 1
    fitness_class.save()

    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_bookings(request):
    email = request.GET.get('email')
    if not email:
        return Response({'error': 'Email parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    bookings = Booking.objects.filter(client_email=email)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)