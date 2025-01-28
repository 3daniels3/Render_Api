
from fastapi import FastAPI
from routes import products, users,users_db # importamos las rutas de los ficheros
from fastapi.staticfiles import StaticFiles # importa libreria para manejo de imagenes
app = FastAPI()

#routes
app.include_router(products.router)  # importacion de rutas
app.include_router(users.router)    
app.include_router(users_db.router)   
app.mount("/static",StaticFiles(directory="static"), name="static") # listo, ahora solo escribe el hash de la ubicacion


@app.get("/")
async def root():
    return "hola Daniels"

@app.get("/saludo")
async def dicts():
    return {
        'Nombre': 'Daniels',
        'Edad':22,
        'lenguajes':['Node.js','Python'],
        'cosa favorita': 'Mamas solteras'
    }


@app.get("/url")
async def url():
    return {"url":"youtube.com"}

