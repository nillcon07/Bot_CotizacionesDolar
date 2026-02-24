import os
import requests
import datetime
import pytz
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv() # Carga las variables de entorno desde el archivo .env

TOKEN = os.getenv("TELEGRAM_TOKEN")
API_BASE_URL = "https://dolarapi.com/v1/dolares"

def get_dolar_data(endpoint_name: str):
    """Obtiene los datos del dólar desde la API."""
    try:
        response = requests.get(f"{API_BASE_URL}/{endpoint_name}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {endpoint_name}: {e}")
        return None

def format_cotizacion(data) -> str:
    """Formatea la respuesta JSON en un string legible."""
    if not data:
        return "❌ Error al obtener la cotización. Intenta de nuevo más tarde."
    
    nombre = data.get("nombre", "Desconocido")
    compra = data.get("compra", 0)
    venta = data.get("venta", 0)
    
    mensaje = f"💵 *Dólar {nombre}*\n"
    mensaje += f"🔹 *Compra:* ${compra}\n"
    mensaje += f"🔸 *Venta:* ${venta}\n"
    return mensaje

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mensaje de bienvenida."""
    welcome_message = (
        "¡Hola! 👋 Soy tu bot de cotizaciones del dólar argentino.\n\n"
        "Comandos disponibles:\n"
        "/oficial - Cotización Dólar Oficial\n"
        "/blue - Cotización Dólar Blue\n"
        "/mep - Cotización Dólar MEP (Bolsa)\n"
        "/cripto - Cotización Dólar Cripto\n"
        "/tarjeta - Cotización Dólar Tarjeta\n"
        "/todos - Todas las cotizaciones juntas"
    )
    await update.message.reply_text(welcome_message)

async def dolar_oficial(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_dolar_data("oficial")
    await update.message.reply_text(format_cotizacion(data), parse_mode="Markdown")

async def dolar_blue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_dolar_data("blue")
    await update.message.reply_text(format_cotizacion(data), parse_mode="Markdown")

async def dolar_mep(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_dolar_data("bolsa")
    await update.message.reply_text(format_cotizacion(data), parse_mode="Markdown")

async def dolar_cripto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_dolar_data("cripto")
    await update.message.reply_text(format_cotizacion(data), parse_mode="Markdown")

async def dolar_tarjeta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_dolar_data("tarjeta")
    await update.message.reply_text(format_cotizacion(data), parse_mode="Markdown")

async def todos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Muestra todas las cotizaciones disponibles."""
    endpoints = ["oficial", "blue", "bolsa", "cripto", "tarjeta"]
    mensaje = "📊 *Cotizaciones actuales:*\n\n"
    
    for endpoint in endpoints:
        data = get_dolar_data(endpoint)
        if data:
            nombre = data.get("nombre", "Desconocido")
            compra = data.get("compra", 0)
            venta = data.get("venta", 0)
            mensaje += f"💵 *{nombre}*: Compra ${compra} | Venta ${venta}\n"
        else:
            mensaje += f"❌ Error al obtener el dólar {endpoint}\n"
            
    await update.message.reply_text(mensaje, parse_mode="Markdown")

def main():
    print("Iniciando el bot...")
    app = ApplicationBuilder().token(TOKEN).build()

    # Añadir manejadores de comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("oficial", dolar_oficial))
    app.add_handler(CommandHandler("blue", dolar_blue))
    app.add_handler(CommandHandler("mep", dolar_mep))
    app.add_handler(CommandHandler("cripto", dolar_cripto))
    app.add_handler(CommandHandler("tarjeta", dolar_tarjeta))
    app.add_handler(CommandHandler("todos", todos))

    print("Bot en ejecución. Presiona Ctrl+C para detener.")
    # Iniciar el bot (polling)
    app.run_polling()

if __name__ == "__main__":
    main()
