from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "your sid here"
# Your Auth Token from twilio.com/console
auth_token  = "your auth token here"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+yournumber", 
    from_="+twilionumber",
    body='your message here')

print(message.sid)
