from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = ""
auth_token =""
client = Client(account_sid, auth_token)
twilio_number = your_twilio_number
tergat_no= YOUR_TARGET_NUMBER

client = Client(account_sid, auth_token)
massage = client.messages.create(
    body='Hello from Python!',
    from_=twilio_number,
    to=tergat_no
)
