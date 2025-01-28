from fastapi import APIRouter

router = APIRouter(prefix="/products", #prefijo /products para facilitar manejo de hash
                   tags=["Products"], # un tag para documentacion
                   responses={404: {"description": "Not found"}}, ) # response es un mensaje por si algo malo llega a pasa y prefix el prefijo de laruta

products_lisa = ["producto 1", "producto 2", "producto 3", "producto 4"]


@router.get("/")
async def products():
    return["producto 1", "producto 2", "producto 3", "producto 4"]



@router.get("/{id}")
async def products(id:int):
    return products_lisa[id]