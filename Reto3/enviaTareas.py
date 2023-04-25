import datetime
import yagmail
import pandas as pd

yag = yagmail.SMTP("thek321xd@gmail.com", oauth2_file="~/oauth2_creds.json")

today = datetime.date.today()
df = pd.read_csv("./Reto3/tareas.csv", header=None, names=["Nombre", "Email", "Fecha", "Tarea"])
tareas_hoy = df[df["Fecha"] == str(today)]

persona_anterior = ""
tareas_persona = ""
for _, tarea in tareas_hoy.iterrows():
    if tarea["Nombre"] == persona_anterior:
        tareas_persona += f"{tarea['Tarea']}\n"
    else:
        if tareas_persona:
            subject = f"Hola, {persona_anterior}, estas son tus tareas de hoy {today}"
            contents = f"Estas son tus tareas de hoy:\n{tareas_persona}"
            yag.send(to=tarea["Email"], subject=subject, contents=contents)
        tareas_persona = f"{tarea['Tarea']}\n"
        persona_anterior = tarea["Nombre"]

# Enviar las tareas de la última persona
if tareas_persona:
    ultima_persona = tareas_hoy.iloc[-1]
    to = ultima_persona['Email']
    subject = f"Hola, {persona_anterior}, estas son tus tareas de hoy {today}"
    contents = f"Estas son tus tareas de hoy:\n{tareas_persona}"
    yag.send(to=to, subject=subject, contents=contents)
