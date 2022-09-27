from tinkoff.invest import Client

TOKEN = 'token'

with Client(TOKEN) as client:
    print(client.users.get_accounts())