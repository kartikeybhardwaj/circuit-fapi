from google.oauth2 import id_token
from google.auth.transport import requests

from constants.secret import CLIENT_ID

class GoogleAuth:
    
    def __init__(self):
        super().__init__()
    
    def getUser(self, idToken: str) -> dict:
        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(idToken, requests.Request(), CLIENT_ID)
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            # ID token is valid. Return the user's Google Account details
            return {
                "username": idinfo["email"],
                "displayname": idinfo["name"],
                "email": idinfo["email"]
            }
        except Exception as ex:
            return None
