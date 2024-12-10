from fastapi import FastAPI, HTTPException, status
import requests
import redis
import json

app = FastAPI()

# clave api
KEY_API = "7U5JH7X6WU9XLKCKAMXJ3HL66"

# conexion redis
redis_conexion = redis.Redis(host="localhost", port=6379, db=0)


# ruta
@app.get("/time")
async def get_weather(location: str):

    # verificacion de datos redis
    cache_redis = redis_conexion.get(location)

    # si todo esta valido almacenamos los datos en formato json
    if cache_redis:
        return json.loads(cache_redis)

    # url de la api
    URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={KEY_API}"
    
    # llamamos a la api
    response = requests.get(URL)

    # si la api esta funcionado correctamente llamos de formarto json
    if response.status_code == 200:
        data = response.json()

        # Descripción general del clima
        data.get("description", "Descripción no disponible.")

        # Extraer datos de los días
        datos = [
            {
                "fecha": day.get("datetime", "No disponible"),
                "descripcion": day.get("description", "No disponible"),
                "temperatura_maxima": day.get("tempmax", "No disponible"),
                "temperatura_minima": day.get("tempmin", "No disponible")
            }
            for day in data.get("days", [])
        ]


        redis_conexion.setex(location, # bogota - barranquilla por ejemplo
                             3600, #tiempo 
                             json.dumps(datos) # convertir en cadena json
                             )
        
        return datos
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No se pudo obtener la información del clima.")




# docker exec -it redis redis-cli
