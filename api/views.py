from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

#@api_view(['GET','PUT','POST','DELETE'])
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint':'/notes/id',
            'method':'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

@api_view(["GET"])
def getNotes(request):
    #notes consists of python objects
    notes = Note.objects.all()
    #serializes, turns python object to JSON, 
    #the many arg means we want to serialize more than one object
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getNote(request,pk):
    #notes consists of python objects
    notes = Note.objects.get(id=pk)
    #serializes, turns python object to JSON, 
    #the many arg means we want to serialize more than one object
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)