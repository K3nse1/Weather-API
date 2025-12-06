📌 Weather API

API REST creada con FastAPI que permite consultar, crear, actualizar y eliminar información meteorológica de distintas ciudades.
Proyecto inicial de práctica para aprender arquitectura básica de APIs, validaciones y manejo de errores.

⸻

📚 Tecnologías utilizadas
	•	Python 3.12+
	•	FastAPI
	•	Uvicorn
	•	Pydantic
	•	Mock data en memoria (sin base de datos por ahora)

⸻

▶️ Cómo ejecutar el proyecto en local

git clone https://github.com/K3nse1/Weather-API.git
cd Weather-API

python -m venv venv
source venv/bin/activate   # MacOS/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

uvicorn main:app --reload

📍 Documentación interactiva: http://127.0.0.1:8000/docs

⸻

🌦️ Endpoints disponibles

Método	URL	Descripción	Body	Response
GET	/	Health-check	❌	JSON
GET	/weather	Devuelve el tiempo de una ciudad	Query param	Weather
GET	/weather/all	Lista todas las ciudades	❌	List[Weather]
POST	/weather	Crea una nueva ciudad	JSON	Weather
PUT	/weather	Actualiza el clima de una ciudad	JSON	Weather
DELETE	/weather	Elimina una ciudad	JSON	MessageResponse


⸻

🧱 Modelos

Weather

{
  "city": "Madrid",
  "temperature": "5ºC",
  "description": "Clear sky"
}

CityCreate (Body para POST/PUT)

{
  "city": "Berlin",
  "temperature": 2,
  "description": "Cloudy"
}

CityDelete (Body para DELETE)

{
  "city": "Moscow"
}

MessageResponse (Respuesta del DELETE)

{
  "detail": "Moscow has been removed successfully."
}


⸻

❗Validaciones implementadas
	•	Ciudad no puede repetirse en creación (POST)
	•	Ciudad debe existir en edición/eliminación (PUT/DELETE)
	•	Temperatura debe estar entre -40 y 50
	•	Longitud mínima y máxima para strings
	•	Gestión de errores consistente con HTTPException

⸻

🚀 Mejoras futuras
	•	Persistencia real → Base de datos (SQLite/PostgreSQL)
	•	Dockerización del proyecto
	•	Autenticación (JWT)
	•	Tests automáticos
	•	Deploy en la nube

⸻

✨ Autor

👤 Raúl Santos

Proyecto de aprendizaje y mejora continua ❤️