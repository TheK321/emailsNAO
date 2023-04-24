#!/bin/bash

# Ruta al directorio del script de Python
SCRIPT_DIR=/home/thek321/Reto3/

# Nombre del script de Python
SCRIPT_NAME=envia.py

# Contenido del script de shell que ejecuta el script de Python
SCRIPT_CONTENT="#!/bin/bash\npython3 ${SCRIPT_DIR}${SCRIPT_NAME}"

# Guarda el script de shell en un archivo
echo -e "${SCRIPT_CONTENT}" > "${SCRIPT_DIR}ejecutar_script.sh"

# Da permisos de ejecución al script de shell
chmod +x "${SCRIPT_DIR}ejecutar_script.sh"

# Configura cron para que ejecute el script de shell cada lunes a la medianoche
(crontab -l 2>/dev/null; echo "0 0 * * 1 ${SCRIPT_DIR}ejecutar_script.sh") | crontab -

echo "Se enviarán los correos cada lunes a la medianoche"
