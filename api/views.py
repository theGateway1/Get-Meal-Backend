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
        'body': None,
        'updated': None,
        'description': 'Returns all the menu items'
    },
    {
        'Endpoint': '/menuItems/id',
        'method': 'GET',
        'body': None,
        'updated': None,
        'description': 'Returns a single menu item'
    },
    {
        'Endpoint': '/menuItems/create',
        'method': 'POST',
        'body': {'body':""},
        'updated': {'updated':""},
        'description': 'Creates a new menu item with data sent in post request',
    },
    {
        'Endpoint': '/menuItems/id/update',
        'method': 'PUT',
        'body': {'body':""},
        'updated': {'updated': ""},
        'description': 'Updates an existing menu item',
    },
    {
        'Endpoint': '/menuItems/id/update',
        'method': 'DELETE',
        'body': None,
        'updated': None,
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
        body = data['body'],
        updated = data['updated']
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
