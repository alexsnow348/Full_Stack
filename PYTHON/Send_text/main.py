from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+601128174379",
    from_="+17067395816",
    body="Hi, Wut. I LOVE YOU!")

print(message.sid)
