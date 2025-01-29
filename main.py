
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
      return [
       {"Message": "Hola, bienvenido a la Api crud FastApi"},
        {"Message":"Ingrese a '/docs' para documentacion de paths de la api"},
        {"Info":"Database : MongoDB Atlas y FastApi: Render"}
             ]
    
        

  


@app.get("/url")
async def url():
    return {"url":"youtube.com"}

