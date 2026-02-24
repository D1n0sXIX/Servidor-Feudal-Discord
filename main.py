import discord
import os
from dotenv import load_dotenv

# Preparamos el entorno para crear el bot
# 1. Cargamos las variables de entorno desde el archivo .env y obtenemos el token de autenticación del bot
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# 2. Creamos una instancia del bot de discord con los intents necesarios para
# Recibir eventos de mensajes y otros eventos relacionados
# EXTRA - Intents es una forma de especificar qué eventos queremos que el bot reciba, lo que puede mejorar el rendimiento y la seguridad del bot
# Limitando la cantidad de eventos que procesa
intents = discord.Intents.all() # Crear una instancia de Intents
client = discord.Client(intents=intents) # Creamos una instancia del bot de Discord con los intents

# Funciones del bot
@client.event # Decorador para indicar que esta función se ejecutará cuando el bot esté listo
async def on_ready(): # Función que se ejecuta cuando el bot está listo
    print(f'El bot se ha iniciado como {client.user}')

@client.event
# Función que se ejecuta cada vez que se recibe un mensaje
async def on_message(message):
    # Si el mensaje fue enviado por el bot, no hacer nada
    if message.author == client.user:
        return
    # Si el mensaje comienza con 'hola', responder con 'Hola!'
    if message.content.startswith('hola'):
        await message.channel.send('Hola!')

# Main de prueba
# Iniciar el bot con el token de autenticación
client.run(DISCORD_TOKEN)
