import secrets

from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException
from fastapi import status

from credentials import TOKEN

app = FastAPI()


@app.get("/")
async def root(token=Header(None)):
    if not secrets.compare_digest(token, TOKEN):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='access denied: invalid token',)
    return {'response': 'hello', 'token': token}
