from dotenv import load_dotenv
load_dotenv()
from tgtg import TgtgClient
import os
from twilio.rest import Client

email = os.getenv("TGTG_EMAIL")
password = os.getenv("TGTG_PASSWORD")
access_token = os.getenv("TGTG_ACCESS_TOKEN")
user_id = os.getenv("TGTG_USER_ID")
account_sid = os.getenv("TWI_ACCOUNT_SID")
auth_token = os.getenv("TWI_AUTH")

if(access_token == None or user_id ==None):
    client = TgtgClient(email=email, password=password)
else:
    client = TgtgClient(access_token=access_token, user_id=user_id)

sms_client = Client(account_sid, auth_token)

favs = client.get_items()
number_available = favs[0]["items_available"] 
if number_available == 1:
    print('Empty')
else:
    to_number = os.getenv("TO_NUMBER")
    sms_client.messages.create(
                body=('Antall fra BB Sletten: ' + str(number_available)),
                from_='Elon Musk',
                to=to_number
            )

