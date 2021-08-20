from rest_framework.decorators import api_view
from rest_framework.response import Response

import api
from .serializers import MenuSerializer
from .models import Menu
from api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
    {
        'Endpoint': '/menuItems/',
        'method': 'GET',
        'i1': None,
        'i2': None,
        'i3': None,
        'i4': None,
        'i5': None,
        'i6': None,
        'i7': None,
        'i8': None,
        'updated': None,
        'eta': None,
        'description': 'Returns all the menu items'
    },
    {
        'Endpoint': '/menuItems/id',
        'method': 'GET',
        'i1': None,
        'i2': None,
        'i3': None,
        'i4': None,
        'i5': None,
        'i6': None,
        'i7': None,
        'i8': None,
        'updated': None,
        'eta': None,
        'description': 'Returns a single menu item'
    },
    {
        'Endpoint': '/menuItems/create',
        'method': 'POST',
        'i1': {'i1':""},
        'i2': {'i2':""},
        'i3': {'i3':""},
        'i4': {'i4':""},
        'i5': {'i5':""},
        'i6': {'i6':""},
        'i7': {'i7':""},
        'i8': {'i8':""},
        'updated': {'updated':""},
        'eta': {'eta':""},
        'description': 'Creates a new menu item with data sent in post request',
    },
    {
        'Endpoint': '/menuItems/id/update',
        'method': 'PUT',
        'i1': {'i1':""},
        'i2': {'i2':""},
        'i3': {'i3':""},
        'i4': {'i4':""},
        'i5': {'i5':""},
        'i6': {'i6':""},
        'i7': {'i7':""},
        'i8': {'i8':""},
        'updated': {'updated': ""},
        'eta': {'eta':""},
        'description': 'Updates an existing menu item',
    },
    {
        'Endpoint': '/menuItems/id/update',
        'method': 'DELETE',
        'i1': {'i1':""},
        'i2': {'i2':""},
        'i3': {'i3':""},
        'i4': {'i4':""},
        'i5': {'i5':""},
        'i6': {'i6':""},
        'i7': {'i7':""},
        'i8': {'i8':""},
        'updated': {'update':""},
        'eta': {'eta':""},
        'description': 'Deletes an existing menu item',
    },
    ]
    return Response(routes)

@api_view(['GET'])
def getMenus(request):
    menus = Menu.objects.all()

    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMenu(request, pk):
    menu = Menu.objects.get(id=pk)

    serializer = MenuSerializer(menu, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createMenu(request):
    data = request.data

    menu = Menu.objects.create(
        i1 = data['i1'],
        i2 = data['i2'],
        i3 = data['i3'],
        i4 = data['i4'],
        i5 = data['i5'],
        i6 = data['i6'],
        i7 = data['i7'],
        i8 = data['i8'],
        updated = data['updated'],
        eta = data['eta']
    )

    serializer = MenuSerializer(menu,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateMenu(request, pk):
    data = request.data

    menu = Menu.objects.get(id=pk)

    serializer = MenuSerializer(menu,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMenu(request,pk):
    menu = Menu.objects.get(id=pk)
    menu.delete()
    return Response('Menu was deleted')
