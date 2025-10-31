import os
import threading
from flask import Flask
import discord
from discord.ext import commands
import config
import traceback

# === Configurar Flask ===
app = Flask(__name__)

@app.route('/')
def home():
    return "El bot de Discord está corriendo correctamente 🚀"

def run_flask():
    try:
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)
    except Exception as e:
        print("⚠️ Error en el servidor Flask:")
        traceback.print_exc()  # Muestra el tipo de error y el traceback

# === Configurar Discord ===
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ping(ctx, *args):
    try:
        respuesta = ' '.join(args)
        await ctx.send(respuesta)
    except Exception as e:
        print("⚠️ Error en el comando 'ping':")
        traceback.print_exc()

@bot.event
async def on_ready():
    print(f'✅ Bot activo como {bot.user}')

# === Ejecutar Flask y Discord ===
if __name__ == "__main__":
    try:
        # Iniciar el servidor Flask en un hilo separado
        flask_thread = threading.Thread(target=run_flask)
        flask_thread.start()

        # Iniciar el bot de Discord
        bot.run(config.TOKEN)

    except Exception as e:
        print("⚠️ Error general al iniciar el bot o Flask:")
        traceback.print_exc()
