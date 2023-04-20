class TarjetaDeCumpleanios:
    def __init__(self, destinatario, remitente, mensaje):
        self.destinatario = destinatario
        self.remitente = remitente
        self.mensaje = mensaje

    def generar_html(self):
        html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Tarjeta de Cumpleaños</title>
        </head>
        <body style="background-color: #FDC8C3;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    text-align: center;">
                    <h1>¡Feliz Cumpleaños, {0}!</h1>
                    <h2>De: {1}</h2>
                    <h2>Para: {0}</h2>
                    <p style="font-size: 24px;
                    margin-top: 10px;
                    margin-bottom: 10px;">{2}</p>
                    <img src="https://www.imageshine.in/uploads/gallery/Colorful_happy_birthday_lettering.png" alt="Tarjeta de Cumpleaños">
        </body>
        </html>
        '''.format(self.destinatario, self.remitente, self.mensaje)
        return html
