# Orquestador de IAs + interfaz sencilla

Aplicación que integra múltiples APIs de modelos de lenguaje (Groq y OpenRouter) y decide automáticamente cuál utilizar según la complejidad de la consulta.

## Características

- Selección automática de modelo
- Modo de revisión cruzada entre IAs
- Interfaz gráfica simple con Tkinter

## Cómo usar

1. Crear un archivo `Keys.txt` en la raíz del proyecto con el siguiente contenido:

GROQ_API_KEY=tu_key
OPENROUTER_API_KEY=tu_key

2. Instalar dependencias:

pip install groq
pip install openai

3. Ejecutar la aplicación:

python interfaz.py

## Cómo funciona

- Consultas cortas → Groq (rápido)
- Consultas largas → OpenRouter (más completo)
- Modo revisión cruzada → compara respuestas entre ambos modelos
