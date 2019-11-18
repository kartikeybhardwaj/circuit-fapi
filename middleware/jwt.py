import jwt
import datetime
from constants.secret import jwtSecret

class JWT:

    __exp = 24 * 60 * 60

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def encode(self, payload):
        payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT.__exp)
        return jwt.encode(payload, jwtSecret, algorithm="HS256")

    def decode(self, encoded_jwt):
        decoded_jwt = None
        try:
            decoded_jwt = jwt.decode(encoded_jwt, jwtSecret, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            # Signature has expired
            pass
        return decoded_jwt
