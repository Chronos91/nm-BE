from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def get_user_info(request):
    # Get the username and password from the request data
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return JsonResponse({'error': 'email and password required'}, status=400)
    print(email, password)
    return JsonResponse({'message': 'Login successful'}, status=200)
