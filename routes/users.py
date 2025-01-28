from fastapi import APIRouter, HTTPException

from pydantic import BaseModel


router = APIRouter()

# usar un path de la url como parametro de funcion
@router.get('/items/{item_id}')
async def root(item_id:int):
    return {"item_id":item_id}

# Entidad User



# ejemplo de user json manual, mala practica
@router.get("/usersjson")
async def usersjson():
    return [{"name":"Daniel","surname":"Sanchez","url": "https://youtube.com","age":22},
            {"name":"juan","surname":"paternina","url": "https://twiter.com","age":40},
            {"name":"miguel","surname":"martinez","url": "https://hakkon.com","age":15} ]



#get de usuarios haciendo uso de BaseModel
@router.get("/users")
async def user():
    return users_fake_db


# Entidad User
class User(BaseModel):
    id:int
    name:str
    surname: str
    url: str
    age: int

users_fake_db = [ 
            User(id =1,name="Daniel",surname="Sanchez",url="https://youtube.com",age=22),
            User(id =2,name="juan",surname="paternina",url="https://twiter.com",age=40),
            User(id=3,name="miguel",surname="martinez",url= "https://hakkon.com",age=15)]

## Peticiones por path
# get para traer usuario especifico
@router.get("/user/{id}")
async def user(id:int):
    return search_id(id)

    



@router.get("/userquery")
async def user(id:int):
    #filtra una funcion atravez de una funcion y un itrable
    user = filter(lambda user: user.id == id ,users_fake_db) # valida con una funcion lambda y lo mezcla con el objeto
    try:
        return list(user)[0]
    except: 
        return {"Messange": "Error no se encontro el usuario"}



# uso de query
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("/itemquery/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]



#### POST
# como vas a agregar haces referencia a la misma que trae
@router.post("/user/", status_code=201) #codigo por si sale bien
async def user(user:User): # el parametro sera igual al modelo o entidad anterior
    if type(search_id(user.id))== User:
        raise HTTPException(status_code=204,detail="El usuario ya existe") # Error personalizado importando httpexception
        return {"Error": "Ya existe este usuario"}
    else:
        users_fake_db.append(user)
        return user


###PUT
#Editar
@router.put("/user/")
async def user(user:User):
    for index, saved_user in enumerate(users_fake_db):
        if saved_user.id == user.id:
            users_fake_db[index] = user
    return user




@router.delete("/user/{id}")
async def delete_user(id:int):
    for index, saved_user in enumerate(users_fake_db):
        if saved_user.id == id:
           del users_fake_db[index]
           return {"Message": "elimino"}




#filtra una funcion atravez de una funcion y un itrable
def search_id(id:int):
        
        user = filter(lambda user: user.id == id ,users_fake_db) # valida con una funcion lambda y lo mezcla con el objeto
        try:
            return list(user)[0]
        except: 
            return {"Messange": "Error no se encontro el usuario"}
