from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, CreateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        # Check if data coming from frontend is in correct format
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            #trying to match if host id is already present in DB
            queryset = Room.objects.filter(host=host)
        # if above host id already exist then update the fields for that ID
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                # returning response to frontend that existing details is updated
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                # if host id does not matches then create new room ID using Room model.
                room = Room(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save()
                # returning response to frontend
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
        # return error response if backend validations are failed  
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
    
class GetRoom(APIView):
    serializer_class = RoomSerializer
    # below line is written to url parameter sent from frontend
    lookup_url_kwarg = 'code'

    def get(self, request, format=None):
        # get code sent from frontend in code variable
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None:
            #find room in DB using .filter
            room = Room.objects.filter(code=code)
            if len(room) > 0:
                data = RoomSerializer(room[0]).data
                #adding one more key to data sent to frontend 
                data['is_host'] = self.request.session.session_key == room[0].host
                return Response(data, status=status.HTTP_200_OK)
            # if room not found return msg that room not found
            return Response({'Room Not Found': 'Invalid Room Code.'}, status=status.HTTP_404_NOT_FOUND)
        #if code is not passed send bad request error
        return Response({'Bad Request': 'Code paramater not found in request'}, status=status.HTTP_400_BAD_REQUEST)
