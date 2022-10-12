from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
def home():
    return {"Hello": "FastAPI"} 


@app.get("/echo")
def echo(name:str):
    return f"hola: {name}"
