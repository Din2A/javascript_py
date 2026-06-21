import requests
import time
from peliculas_database import peliculas

API_KEY = "TU_API_KEY"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"


def buscar_poster(nombre):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": API_KEY,
        "query": nombre,
        "language": "es-ES",
    }
    respuesta = requests.get(url, params=params)
    datos = respuesta.json()

    if datos.get("results"):
        poster_path = datos["results"][0].get("poster_path")
        if poster_path:
            return f"{IMAGE_BASE}{poster_path}"
    return None


for pelicula in peliculas:
    poster_url = buscar_poster(pelicula["nombre"])
    pelicula["imagen"] = poster_url

    if poster_url:
        print(f"✅ {pelicula['nombre']}: encontrada")
    else:
        print(f"⚠️  {pelicula['nombre']}: NO encontrada, revisar a mano")

    time.sleep(0.3)
