import pandas as pd
from TarjetaDeCumple import TarjetaDeCumpleanios
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Obtener la fecha actual
fecha_actual = datetime.now().date()
# Leer el archivo CSV utilizando pandas
df = pd.read_csv('./Reto3/correos.csv')

# Filtrar solo las personas que cumplen años en la fecha actual
cumplen_anios_hoy = df[df.apply(lambda x: (int(x['mm']), int(x['dd'])) == (fecha_actual.month, fecha_actual.day), axis=1)]

# Obtener la edad de cada persona que cumple años hoy
for index, row in cumplen_anios_hoy.iterrows():
    nombre = row['nombre']
    correo_electronico = row['email']
    fecha_nacimiento = datetime(int(row['aa']), int(row['mm']), int(row['dd'])).date()
    edad = relativedelta(fecha_actual, fecha_nacimiento).years
    html = TarjetaDeCumpleanios({nombre}, 'Mario', '¡Felices {edad}! Que tengas un gran día y cumplas muchos más.').generar_html()
    print(html)