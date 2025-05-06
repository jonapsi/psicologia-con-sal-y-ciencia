#!/bin/bash

PROYECTO_DIR="/root/apps/psc"
VENV_DIR="$PROYECTO_DIR/venv"
GUNICORN_SERVICE="gunicorn"

echo "📁 Entrando al directorio del proyecto..."
cd $PROYECTO_DIR || { echo "❌ No se pudo entrar al directorio del proyecto"; exit 1; }

echo "🧪 Verificando entorno virtual..."
if [ ! -f "$VENV_DIR/bin/activate" ]; then
    echo "❌ No se encontró el entorno virtual en: $VENV_DIR"
    echo "🔧 Ejecuta: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

echo "🐍 Activando entorno virtual..."
source $VENV_DIR/bin/activate

echo "🌱 Estableciendo variable DJANGO_SETTINGS_MODULE..."
export DJANGO_SETTINGS_MODULE=config.settings.dev

echo "⬇️ Actualizando código desde GitHub..."
git pull origin main || { echo "❌ Error al hacer pull del repositorio"; exit 1; }

echo "📦 Instalando dependencias (por si acaso)..."
pip install -r requirements.txt || { echo "❌ Error al instalar dependencias"; exit 1; }

echo "🧱 Ejecutando migraciones..."
python manage.py migrate || { echo "❌ Error en migraciones"; exit 1; }

echo "🎨 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput || { echo "❌ Error al recolectar archivos estáticos"; exit 1; }

echo "🚀 Reiniciando Gunicorn..."
sudo systemctl restart $GUNICORN_SERVICE
sudo systemctl status $GUNICORN_SERVICE --no-pager

echo "✅ ¡Proyecto actualizado y reiniciado correctamente!"
#!/bin/bash

PROYECTO_DIR="/root/apps/psc"
VENV_DIR="$PROYECTO_DIR/venv"
GUNICORN_SERVICE="gunicorn"

echo "📁 Entrando al directorio del proyecto..."
cd $PROYECTO_DIR || { echo "❌ No se pudo entrar al directorio del proyecto"; exit 1; }

echo "🧪 Verificando entorno virtual..."
if [ ! -f "$VENV_DIR/bin/activate" ]; then
    echo "❌ No se encontró el entorno virtual en: $VENV_DIR"
    echo "🔧 Ejecuta: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

echo "🐍 Activando entorno virtual..."
source $VENV_DIR/bin/activate

echo "🌱 Estableciendo variable DJANGO_SETTINGS_MODULE..."
export DJANGO_SETTINGS_MODULE=config.settings.dev

echo "⬇️ Actualizando código desde GitHub..."
git pull origin main || { echo "❌ Error al hacer pull del repositorio"; exit 1; }

echo "📦 Instalando dependencias (por si acaso)..."
pip install -r requirements.txt || { echo "❌ Error al instalar dependencias"; exit 1; }

echo "🧱 Ejecutando migraciones..."
python manage.py migrate || { echo "❌ Error en migraciones"; exit 1; }

echo "🎨 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput || { echo "❌ Error al recolectar archivos estáticos"; exit 1; }

echo "🚀 Reiniciando Gunicorn..."
sudo systemctl restart $GUNICORN_SERVICE
sudo systemctl status $GUNICORN_SERVICE --no-pager

echo "✅ ¡Proyecto actualizado y reiniciado correctamente!"