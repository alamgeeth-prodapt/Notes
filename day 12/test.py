# from fastapi import FastAPI, UploadFile, File
# app = FastAPI()
# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):

#     return {
#         "name": file.filename,
#         "content_type": file.content_type
#     }


# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.security import HTTPBasic, HTTPAuthorizationCredentials
# import secrets

# from fastapi.security.http import HTTPBasicCredentials

# app = FastAPI()
# security = HTTPBasic()

# @app.get("/login")
# def login(cred: HTTPBasicCredentials = Depends(security)):
#     username = secrets.compare_digest(
#         cred.username,"admin"
#     )

#     password = secrets.compare_digest(
#         cred.password,"admin"
#     )

#     if not (username and password):
#         raise HTTPException(401)

#     return {
#         "message":"authorised"
#     }

# from fastapi import FastAPI,Security, HTTPException
# from fastapi.security.api_key import APIKeyHeader

# app = FastAPI()

# api_key_header = APIKeyHeader(name="GTG")
# API_KEY = "secret_key"

# @app.get("/secure")
# def secure(api_key: str = Security(api_key_header)):
#     if api_key != API_KEY:
#         raise HTTPException(403)

#     return {
#         "message":"Access Granted"

# from datetime import datetime, timedelta
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# app = FastAPI()
# SECRET_KEY = "mysecretkey123456789"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# pwd_context = CryptContext(
#     schemes=["bcrypt"],
#     deprecated="auto"
# )
# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="token"
# )
# fake_users_db = {
#     "john": {
#         "username": "john",
#         "full_name": "John Smith",
#         "email": "john@test.com",
#         "hashed_password": pwd_context.hash("12345"),
#     }
# }
# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(
#         plain_password,
#         hashed_password
#     )

# def authenticate_user(username, password):

#     user = fake_users_db.get(username)

#     if not user:
#         return None

#     if not verify_password(
#         password,
#         user["hashed_password"]
#     ):
#         return None

#     return user
# def create_access_token(data: dict):

#     to_encode = data.copy()

#     expire = datetime.utcnow() + timedelta(
#         minutes=ACCESS_TOKEN_EXPIRE_MINUTES
#     )

#     to_encode.update(
#         {"exp": expire}
#     )

#     return jwt.encode(
#         to_encode,
#         SECRET_KEY,
#         algorithm=ALGORITHM
#     )
# @app.post("/token")

# def login(
#     form_data: OAuth2PasswordRequestForm = Depends()
# ):

#     user = authenticate_user(
#         form_data.username,
#         form_data.password
#     )

#     if not user:

#         raise HTTPException(
#             status_code=401,
#             detail="Invalid username/password"
#         )

#     access_token = create_access_token(
#         data={
#             "sub": user["username"]
#         }
#     )

#     return {
#         "access_token": access_token,
#         "token_type": "bearer"
#     }


# # -----------------------------------------
# # Current User
# # -----------------------------------------

# def get_current_user(
#     token: str = Depends(oauth2_scheme)
# ):

#     credentials_exception = HTTPException(
#         status_code=401,
#         detail="Could not validate credentials"
#     )

#     try:

#         payload = jwt.decode(
#             token,
#             SECRET_KEY,
#             algorithms=[ALGORITHM]
#         )

#         username = payload.get("sub")

#         if username is None:
#             raise credentials_exception

#     except JWTError:
#         raise credentials_exception

#     return fake_users_db.get(username)


# # -----------------------------------------
# # Protected API
# # -----------------------------------------

# @app.get("/profile")

# def profile(
#     current_user=Depends(get_current_user)
# ):

#     return current_user
