from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/send_mensage/{number}/{mensage}")
def send_mensage(number: str, mensage: str):
    return {"numero": number, "mensagem": mensage}