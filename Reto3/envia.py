import csv
import yagmail

yag = yagmail.SMTP("thek321xd@gmail.com", oauth2_file="~/oauth2_creds.json")

with open('/home/thek321/Reto3/correos.csv') as archivocsv:
    reader = csv.DictReader(archivocsv)
    for row in reader:
        alias = row['nombre']
        to = row['email']
        subject = f"Hola, {alias}, desde Python"
        contents = '¡Este es un correo de prueba enviado desde Python!'
        yag.send(to=to, subject=subject, contents=contents)