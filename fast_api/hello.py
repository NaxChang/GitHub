# 檔名 hello.py

from fastapi import FastAPI 

app = FastAPI() 

@app.get("/hi")
def greet():
    return "hello world"