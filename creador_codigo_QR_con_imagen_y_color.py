import qrcode  # Importamos la librería qrcode que contiene todo lo necesario para crear el QR
from PIL import Image  # Importamos la librería PIL para manipular imágenes

# Aquí va la información que va a guardar el QR, en este caso es la dirección que querramos
input_text = "pagina_de_ejemplo.com"

# Crear el QR
qr = qrcode.QRCode(
    version=1,  # Versión del QR, determina la capacidad de datos del QR
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada cuadro del QR
    border=4  # Tamaño del borde del QR
)
qr.add_data(input_text)  # Añadimos la información al QR
qr.make(fit=True)  # Ajustamos el tamaño del QR para que encaje toda la información

# Crear la imagen del QR con colores personalizados
qr_image = qr.make_image(fill_color="rgb(0, 0, 0)", back_color="rgb(255, 255, 255)")  # Negro para los módulos, blanco para el fondo

# Cargar la imagen que deseas agregar al centro del QR
center_image = Image.open("ejemplo_de_imagen.png")  # Asegúrate de que la imagen esté en el mismo directorio que el script

# Obtener las dimensiones del QR y de la imagen
qr_width, qr_height = qr_image.size
image_width, image_height = center_image.size

# Calcular la posición donde colocar la imagen en el centro del QR
position = ((qr_width - image_width) // 2, (qr_height - image_height) // 2)

# Pegar la imagen en el centro del QR
qr_image.paste(center_image, position)

# Guardar el QR con la imagen
qr_image.save("ejemplo.png")  # Guardar el QR generado con el nombre "xtremrocks.png"
