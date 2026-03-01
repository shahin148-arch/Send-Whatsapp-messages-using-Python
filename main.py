from twilio.rest import Client
from datetime import datetime
import time
# Twilio credentials
account_sid = 'ACc7f53e1dcad1c174ea86e76d4239e703'
auth_token = 'cbc245eadcf5a61fb732f5e30f60d748'

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message):
    try:
        message = client.messages.create ( 
            from_= 'whatsapp:+14155238886',
            body = message,
            to = 'whatsapp:'+recipient_number
        )
        print(f'Message sent successfullly! Message SID{message.sid}')
    except Exception as e:
        print(f'Failed to send message: {str(e)}')

name = input("Enter the recipient name =")
recipient_number = input("Enter the recipient number (with country code) =")
message_body = input(f"Enter the message to send to {name} :")

date_str = input("Enter the date to send the message (YYYY-MM-DD) =")
time_str = input("Enter the time to send the message (HH:MM) =")

scheduled_datetime_str = f"{date_str} {time_str}"
scheduled_datetime = datetime.strptime(scheduled_datetime_str, "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_diff = (scheduled_datetime - current_datetime).total_seconds()

if time_diff > 0:
    print(f"Message scheduled to be sent at {scheduled_datetime_str}")
    time.sleep(time_diff)
    send_whatsapp_message(recipient_number, message_body)
else:
    print("Scheduled time is in the past. Please enter a future date and time.")

    time.sleep(time_diff)

    send_whatsapp_message(recipient_number, message_body)