from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from fastapi import HTTPException, status

SECRET_KEY = "mysecretkey123"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes = ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {
         "exp" : expire
        }
    )

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt 

def hash_password(password: str):

    password = password[:72]

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
):

    plain_password = plain_password[:72]

    return pwd_context.verify(plain_password,hashed_password)

def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )