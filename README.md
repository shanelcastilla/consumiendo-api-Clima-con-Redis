# Weather API con FastAPI y Redis

Este proyecto es una API desarrollada con **FastAPI** que permite obtener información meteorológica de una ubicación específica, utilizando la API de Visual Crossing. Para optimizar el rendimiento y reducir llamadas externas, los datos se almacenan temporalmente en **Redis** como caché.

## Características

- Recupera datos meteorológicos de Visual Crossing API.
- Almacena la información en Redis para reducir solicitudes repetitivas.
- Soporte para peticiones rápidas y eficientes con caché de una hora.
- Gestión de errores mediante HTTPException en caso de fallos al obtener datos.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.9 o superior
- Redis (puede ejecutarse en un contenedor Docker)

### Instalación de Dependencias

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/weather-api.git
   cd weather-api
