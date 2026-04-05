from google import genai

# 1. Conectamos con tu llave
mi_llave = "AIzaSyAUZFVIZINsHWcGMKI6idW8CmyIWX6bsOU"
client = genai.Client(api_key=mi_llave)

# 2. Elegimos un modelo estable y rápido de tu lista
modelo_elegido = 'gemini-2.5-flash' 

# 3. Nuestro prompt sobre neurociencia
mi_pregunta = "Explicame en un párrafo corto qué es el paradigma P300 en estudios de EEG."

print("Enviando la pregunta a Google... ⏳")

# 4. Llamada a la API
respuesta = client.models.generate_content(
    model=modelo_elegido,
    contents=mi_pregunta
)

# 5. Imprimir respuesta
print("\n--- RESPUESTA DE LA IA ---")
print(respuesta.text)