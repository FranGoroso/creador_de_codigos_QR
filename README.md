# Generador de Código QR con Imagen Central

Este script de Python genera un código QR con una imagen personalizada en el centro. Utiliza las librerías `qrcode` para la generación del código QR y `Pillow` para la manipulación de imágenes.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes librerías:

- qrcode
- Pillow

Puedes instalarlas utilizando `pip`:

```
pip install qrcode[pil]
pip install Pillow
```

# Uso

1. Clona este repositorio.

2. Asegúrate de tener la imagen icono_bebida.png en el mismo directorio que el script.

3. Edita el valor de input_text en el script para cambiar la información que se almacenará en el código QR.

4. Ejecuta el script:

```
python qr_code_generator.py
```
El código QR generado se guardará como ejemplo.png en el mismo directorio que el script.

# Personalización

Puedes personalizar varios aspectos del código QR y de la imagen central:

`input_text`: La información que quieres almacenar en el código QR.

`fill_color` y `back_color`: Colores del código QR.

`ejemplo_imagen.png`: Cambia esta imagen por la que desees colocar en el centro del código QR.

# Ejemplo

Este script, tal como está, generará un código QR que almacenará la dirección pagina_de_ejemplo.com y tendrá una imagen central llamada ejemplo_de_imagen.png.

# Notas

Asegúrate de que la imagen que deseas colocar en el centro del código QR no sea demasiado grande, para que no interfiera con la legibilidad del código QR.
Puedes ajustar los parámetros del código QR, como la versión y el nivel de corrección de errores, según tus necesidades.

