from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0dadb0ce3f1db887ecf2cc5209932676"
# Your Auth Token from twilio.com/console
auth_token  = "7eb9f55beeb3cfea278ccc183cf0f46a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+601128174379",
    from_="+17067395816",
    body="Hi, Wut. I LOVE YOU!")

print(message.sid)
