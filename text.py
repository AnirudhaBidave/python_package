from azurerm import access_token, cost_rep

tenantId='ce0576f1-a4d1-40a5-895e-39f37c308e24'
client_id='2c85eb60-87a2-4574-91c2-b6ebfc180844'
client_secret='lR.8Q~nRQ391aaI-ejUCWtMFzd563DC5PaElKapU'

print(access_token(tenantId, client_id, client_secret))

