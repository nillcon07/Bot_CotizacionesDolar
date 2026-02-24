# 💵 Bot de Cotizaciones del Dólar — Telegram

Bot de Telegram que consulta en tiempo real las cotizaciones del dólar argentino usando la [DolarAPI](https://dolarapi.com).

---

## 📋 Comandos disponibles

| Comando     | Descripción                    |
|-------------|-------------------------------|
| `/start`    | Muestra el menú de bienvenida  |
| `/oficial`  | Cotización Dólar Oficial       |
| `/blue`     | Cotización Dólar Blue          |
| `/mep`      | Cotización Dólar MEP (Bolsa)   |
| `/cripto`   | Cotización Dólar Cripto        |
| `/tarjeta`  | Cotización Dólar Tarjeta       |
| `/todos`    | Todas las cotizaciones juntas  |

---

## 🚀 Instalación y uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/nillcon07/Bot_CotizacionesDolar.git
cd Bot_CotizacionesDolar
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno
Crear un archivo `.env` en la raíz del proyecto:
```env
TELEGRAM_TOKEN=tu_token_aqui
```

> ⚠️ **Nunca subas tu `.env` al repositorio.** Ya está incluido en `.gitignore`.

### 4. Ejecutar el bot
```bash
python bot.py
```

---

## 🛠️ Tecnologías

- **Python 3.10+**
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) `v21.1.1`
- [requests](https://pypi.org/project/requests/) `v2.32.3`
- [python-dotenv](https://pypi.org/project/python-dotenv/) `v1.2.1`
- [DolarAPI](https://dolarapi.com) — API de cotizaciones del dólar argentino

---

## 📁 Estructura del proyecto

```
Bot_CotizacionesDolar/
├── bot.py              # Lógica principal del bot
├── requirements.txt    # Dependencias del proyecto
├── .env                # Variables de entorno (NO subir)
├── .gitignore          # Archivos ignorados por git
└── README.md           # Este archivo
```
