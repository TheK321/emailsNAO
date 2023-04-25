from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Creamos un diccionario que asocia a cada persona un color
colors_by_person = {
    'Juan Perez': colors.green,
    'Maria Rodriguez': colors.blue,
    'Pedro Gomez': colors.red,
    'Ana Martinez': colors.orange,
    'Daniela Duarte': colors.purple,
}

# Definimos un ancho para ambas columnas
col_width = 2.5*inch

# Creamos una hoja en formato landscape
doc = SimpleDocTemplate("./Reto3/tareas.pdf", pagesize=landscape(letter))

# Creamos una lista vacía que contendrá los elementos que se agregarán a la hoja
elements = []

# Definimos un estilo para el encabezado
header_style = ParagraphStyle(
    name='Header',
    fontName='Helvetica-Bold',
    fontSize=16,
    leading=20,
    alignment=1,
    spaceAfter=10,
)

# Definimos un estilo para el texto
text_style = ParagraphStyle(
    name='Text',
    fontName='Helvetica',
    fontSize=12,
    leading=14,
    alignment=0,
)

tareas = [
    {'nombre': 'Juan Perez', 'fecha': '2023-04-25', 'tarea': 'Verificar assets'},
    {'nombre': 'Maria Rodriguez', 'fecha': '2023-04-25', 'tarea': 'Revisar campaña de marketing'},
    {'nombre': 'Pedro Gomez', 'fecha': '2023-04-25', 'tarea': 'Confirmar diseño preliminar'},
    {'nombre': 'Ana Martinez', 'fecha': '2023-04-25', 'tarea': 'Actualizar informe de ventas'},
    {'nombre': 'Daniela Duarte', 'fecha': '2023-04-25', 'tarea': 'Enviar correo electrónico'}
]
tasks_by_person = {}

for tarea in tareas:
    nombre = tarea['nombre']
    fecha = tarea['fecha']
    tarea_desc = tarea['tarea']
    
    if nombre not in tasks_by_person:
        tasks_by_person[nombre] = []
    
    tasks_by_person[nombre].append((fecha, tarea_desc))

# Creamos una tabla con las tareas de cada persona
data = []
for person, tasks in tasks_by_person.items():
    # Agregamos una fila con el encabezado
    data.append([Paragraph(person, header_style)])
    # Agregamos una fila por cada tarea
    for task in tasks:
        data.append([Paragraph(' - '.join(task), text_style)])


    # Agregamos un separador entre cada persona
    data.append([''])

    # Añadimos el estilo de fondo según la persona
    style = TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors_by_person[person]),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.white),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 16),
        ('LEADING', (0, 0), (0, 0), 20),
        ('TOPPADDING', (0, 0), (0, 0), 5),
        ('BOTTOMPADDING', (0, 0), (0, 0), 5),
    ])
    elements.append(Table([[Paragraph(person, header_style)]], colWidths=[col_width], style=style))

    # Creamos una tabla para las tareas de la persona
    table = Table(data, colWidths=[col_width])
    style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ])
    table.setStyle(style)
    elements.append(table)
    doc.build(elements)