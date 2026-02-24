# 🏰 Le Turbo Gang University — Discord Bot

Bot de Discord para el servidor universitario de U-Tad, temático de sociedad feudal medieval. Gestiona un sistema de rangos por actividad, duelos entre usuarios, poderes especiales y gremios por carrera.

---

## ⚔️ Características principales

- **Sistema de rangos** — 7 rangos obtenidos mediante puntos de actividad (mensajes, voz, reacciones)
- **Decay por inactividad** — pérdida de puntos escalable según rango
- **Gremios** — roles identificativos por carrera
- **Duelos** — sistema de retos entre usuarios con moderadores y recompensas
- **Poderes activos y pasivos** — habilidades desbloqueables según rango

---

## 🛠️ Stack técnico

| Componente | Tecnología |
|------------|------------|
| Lenguaje | Python 3.11+ |
| Librería Discord | discord.py |
| Base de datos | SQLite + aiosqlite |
| Variables de entorno | python-dotenv |

---

## 📁 Estructura del proyecto

```
bot/
├── main.py              # Punto de entrada del bot
├── .env                 # Token y variables sensibles (no commitear)
├── .env.example         # Plantilla de variables de entorno
├── requirements.txt     # Dependencias
├── cogs/
│   ├── roles.py         # Gestión de rangos y gremios
│   ├── puntos.py        # Sistema de puntos y decay
│   ├── duelos.py        # Sistema de duelos
│   └── poderes.py       # Poderes activos y pasivos
└── database/
    └── db.py            # Capa de acceso a SQLite
```

---

## 🚀 Instalación y uso

### 1. Clona el repositorio
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 2. Crea un entorno virtual e instala dependencias
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configura las variables de entorno
```bash
cp .env.example .env
# Edita .env y añade tu token de Discord
```

### 4. Arranca el bot
```bash
python main.py
```

---

## 📋 Estado del desarrollo

- [ ] Estructura base del bot
- [ ] Sistema de puntos
- [ ] Sistema de rangos y decay
- [ ] Gremios
- [ ] Duelos
- [ ] Poderes activos
- [ ] Poderes pasivos

---

## 🤝 Contribuir

Proyecto interno del servidor de U-Tad. Si eres del servidor y quieres contribuir, abre un issue o contacta con los admins.

---

## ⚠️ Aviso

Nunca subas el archivo `.env` al repositorio. Está incluido en el `.gitignore` por defecto.
