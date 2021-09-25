import secrets
import subprocess

from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException
from fastapi import status

from credentials import TOKEN, COMMAND

app = FastAPI()


@app.post('/')
def run(token=Header(None)):
    if not secrets.compare_digest(token, TOKEN):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='access denied: invalid token')

    code = subprocess.run(COMMAND, check=False).returncode
    if code == 0:
        return {'status': 'success'}
    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, f'command failed with exit code: {code}')
