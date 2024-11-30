# Importamos las librerías necesarias
# Tk: Para crear la interfaz gráfica
# Text: Área de texto para escribir
# Button: Botones de la interfaz
# END: Constante para manejar el final del texto
# Label: Etiquetas para mostrar información
from tkinter import Tk, Text, Button, END, Label

# gTTS: Librería para convertir texto a voz (Google Text-to-Speech)
from gtts import gTTS

# Librería para manejar comandos del sistema operativo
import os

# Función para guardar el texto escrito en un archivo
def save_text():
    # Obtiene todo el texto desde el inicio (1.0) hasta el final
    text = text_area.get("1.0", END)
    # Abre (o crea) un archivo para escribir, usando codificación UTF-8
    with open('user_input.txt', 'w', encoding='utf-8')as file:
        # Escribe el texto en el archivo
        file.write(text)
    # Actualiza la etiqueta de estado para mostrar que se guardó con éxito
    status_label.config(text="Texto guardado con exito.")

# Función para convertir texto a voz
def text_to_speech():
    # Obtiene todo el texto desde el inicio hasta el final
    text = text_area.get("1.0", END)
    # Crea un objeto de texto a voz
    # text: texto a convertir
    # lang='es': idioma español
    # slow=False: velocidad normal de habla
    speech = gTTS(text=text, lang='es', slow=False)
    # Guarda el audio generado como un archivo MP3
    speech.save('output.mp3')
    # Reproduce el archivo de audio 
    # 'start' es un comando específico de Windows para abrir archivos
    os.system('start output.mp3')
    # Actualiza la etiqueta de estado para mostrar que está reproduciendo
    status_label.config(text="Reproduciendo audio")

# Crea la ventana principal de la aplicación
root = Tk()
# Establece el título de la ventana
root.title("Texto a Voz")

# Crea un área de texto para escribir
# height=10: 10 líneas de alto
# width=50: 50 caracteres de ancho
text_area = Text(root, height=10, width=50)
# Agrega el área de texto a la ventana
text_area.pack()

# Crea un botón para guardar texto
# text: texto del botón
# command: función a ejecutar cuando se presiona
save_button = Button(root, text="Guardar Texto", command=save_text)
# Agrega el botón a la ventana
save_button.pack()

# Crea un botón para reproducir texto
play_button = Button(root, text="Reproducir Texto", command=text_to_speech)
# Agrega el botón a la ventana
play_button.pack()

# Crea una etiqueta para mostrar estado
# text="": inicialmente vacía
# fg='green': color del texto en verde
status_label = Label(root, text="", fg='green')
# Agrega la etiqueta a la ventana
status_label.pack()

# Inicia el bucle principal de la interfaz gráfica
# Mantiene la ventana abierta y responde a eventos
root.mainloop()