from fastapi import FastAPI

app = FastAPI() 

@app.get("/echo")
def read_item(name:str):
    return f"name:{name}"

@app.get("/suma")
def read_item(primero:int, segundo:int):
    return f"suma : {primero + segundo}"