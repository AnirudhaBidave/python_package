import requests

class AccessTokenError(Exception):
    pass

def access_token(tenentID, clientID, clientSecrate):

    token_endpoint = f'https://login.microsoftonline.com/{tenentID}/oauth2/token'
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
      'grant_type': 'client_credentials',
      'client_id': clientID,
      'client_secret': clientSecrate,
      'resource': 'https://management.azure.com'
    }

    try:
        response = requests.post(token_endpoint, headers=headers, data=data)
        response.raise_for_status()
        access_token = response.json()['access_token']

        if access_token:
            return access_token
        else:
            raise AccessTokenError("Access token not found in response.")
        
    except requests.exceptions.RequestException as e:
        raise AccessTokenError(f"Error during request: {e}")
    
    except Exception as e:
        raise AccessTokenError(f"Unexpected error: {e}")
    