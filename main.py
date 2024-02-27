# import package

from fastapi import FastAPI, Request, HTTPException, Header
import pandas as pd

#isi headers
# informasi metadat
# format fiilie harus berupa apa
# ngasih tahu request/response berasal dari mana
# untuk otentikasi
# untuk melakukan request -> masukin username & password
# 


app = FastAPI()

API_KEY = 'secret123'

@app.get('/')
def getHome():
    return {
        "message":"Hello Worlddd"
            } 

@app.get('/see-headers')
def readHeader(request: Request):
    headers = request.headers

    print(headers.items)

    return {
        "message": "isi header",
        "headers": headers.get('User-Agent'),
        "headers accept": headers.get("Accept")
    }

@app.get('/secret')
def getSecret(api_key: str = Header(None)):
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail= "Invalid API Key")
    
    return {
        "message": "this is top secret"
    }
