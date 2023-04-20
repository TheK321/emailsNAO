class TarjetaDeCumpleanios:
    def __init__(self, destinatario, remitente, mensaje):
        self.destinatario = destinatario
        self.remitente = remitente
        self.mensaje = mensaje
        
    def generar_html(self):
        html = '''
        <html>
            <head>
                <title>Tarjeta de Cumpleaños</title>
                <style>
                    body {{
                        background-color: #FDC8C3;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        text-align: center;
                    }}
                    h1 {{
                        font-size: 48px;
                        margin-top: 80px;
                        margin-bottom: 0;
                    }}
                    h2 {{
                        font-size: 36px;
                        margin-top: 20px;
                        margin-bottom: 0;
                    }}
                    p {{
                        font-size: 24px;
                        margin-top: 10px;
                        margin-bottom: 10px;
                    }}
                    img {{
                        width: 400px;
                        height: 400px;
                        margin-top: 50px;
                    }}
                </style>
            </head>
            <body>
                <h1>¡Feliz Cumpleaños, {0}!</h1>
                <h2>De: {1}</h2>
                <h2>Para: {0}</h2>
                <hr>
                <p>{2}</p>
                <img src="https://example.com/tarjeta_de_cumpleanos.png" alt="Tarjeta de Cumpleaños">
            </body>
        </html>
        '''.format(self.destinatario, self.remitente, self.mensaje)
        return html
