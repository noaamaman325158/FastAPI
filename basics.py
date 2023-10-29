from fastapi import FastAPI

app = FastAPI()


@app.get('/hello')
def hello():
    return {"hello": "world"}


@app.get("/")
def hello_post():
    return {"Success": "You Posted"}


@app.get('/something')
def something():
    return {"Data": "Something"}
