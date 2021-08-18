from django.http import JsonResponse

def getRoutes(request):
    routes = [
    {
        'Endpoint': '/menuItems/',
        'method': 'GET',
        'body': None,
        'description': 'Returns all the menu items'
    },
    {
        'Endpoint': '/menuItems/id',
        'method': 'GET',
        'body': None,
        'description': 'Returns all the menu items'
    },
    {
        'Endpoint': '/menuItems/',
        'method': 'GET',
        'body': None,
        'description': 'Returns all the menu items'
    },

    ]
    return JsonResponse()