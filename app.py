from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from weather import get_weather
from creds import account_sid, auth_token

app = Flask(__name__)

client = Client(account_sid, auth_token)

# Replace with your actual WhatsApp phone number
your_whatsapp_number = '+14155238886'

def send_whatsapp_message(to, message):
    message = client.messages.create(
        body=message,
        from_='whatsapp:' + your_whatsapp_number,
        to=to
    )
    return message.sid

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    city = request.values.get('Body', None)
    sender_number = request.values.get('From')

    # Handle incoming messages here
    # city = "Received: " + incoming_message

    # Send a reply
    weather = get_weather(city)
    send_whatsapp_message(sender_number, weather)

    return "Message sent."


if __name__ == '__main__':
    app.run(debug=True)