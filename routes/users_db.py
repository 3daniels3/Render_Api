#user DB Api

from fastapi import APIRouter, HTTPException,status
from db.models.user import User
from db.client import db_client
from db.schema.user import user_schema, users_schema
from bson import ObjectId # para poder llamar precisamente al objeto id de las json guardados

router = APIRouter(prefix="/userdb", #prefijo /products para facilitar manejo de hash
                   tags=["UserDb"], # un tag para documentacion
                   responses={404: {"description": "Not found"}}, )




#Get trae todos los usuarios
@router.get("/")
async def user():
    users = db_client.users.find()
    return users_schema(users)


    # users = db_client.local.users.find()
    # list_user = [user_schema(user) for user in users]
    # return [User(**user)for user in list_user]


    

@router.get("/{id}") #pad
async def user(id: str):
    return search_user("_id", ObjectId(id))


@router.get("/") #query
async def user(id: str):
    return search_user("_id",ObjectId(id))
   


#### POST

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED) #codigo por si sale bien
async def user(user:User):
    # el parametro sera igual al modelo o entidad anterior
    if type(search_user("email",user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    
    user_dict = dict(user)
    del user_dict["id"]
     # guarda
    id = db_client.users.insert_one(user_dict).inserted_id
     # muestra lo guardado
    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)




###PUT
#Editar
@router.put("/", response_model=User)
async def user(user:User):
    user_dict = dict(user)
    del user_dict["id"]
    try:
        db_client.users.find_one_and_replace({"_id":ObjectId(user.id)},user_dict)

    except:
        return {"Error": "No se ha actualizado"}
    
    return search_user("_id",ObjectId(user.id))


  
    




@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id:str):
    found = db_client.users.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        return{"Error": "No se elimino el usuario"}





#filtra una funcion atravez de una funcion y un itrable
def search_user(fiel:str,key):
        
        
        try:
            user=db_client.users.find_one({fiel:key})
           
            return User(**user_schema(user))
            
        except: 
            return {"Messange": "Error no se encontro el usuario"}
 
