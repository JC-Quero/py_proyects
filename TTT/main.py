import tkinter as tk #importa la biblioteca para crear interfaces graficas
from tkinter import messagebox #importa la funcionalidad para mostrar mensajes emergentes

#variables del juego (globales)
player = 'X'    #Establece el jugador inicial como X
game_over = False   #Bandera para indicar si el juego ha terminado

#Funcion para verificar si hay un ganador
def check_winner():

    #Verifica filas
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        
    #Verifica columnas

        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True
        
    #Verifica diagonal principal (de izquierda a derecha)

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
            return True
    
    #Verifica diagonal secundaria (de derecha a izquierda)

    if buttons[0][2]['text'] == buttons[1][2]['text'] == buttons[2][0]['text'] != '':
            return True
    
    return False # Si no hay ganador 

def button_click(row,col):
     global player, game_over
     # Si la casilla esta vacia y el juego no ha terminado
     if buttons[row][col]['text'] == '' and not game_over:
          # Colocar la marca del jugador actual
          buttons[row][col]['text'] = player

          #Cambia color de fondo segun el jugador
          buttons[row][col]['bg'] = '#37474F' if player == 'X' else '#455A64'

          # Verifica si hay un ganador
          if check_winner():
               messagebox.showinfo(title= "Tic Tac Toe", message= f"Jugador {player} gana!")
               game_over = True

          # Verifica si es un empate (todas la casillas llenas)
          elif all(buttons[row][col]['text'] != '' for row in range(3) for col in range(3)):
               messagebox.showinfo(title= "Tic Tac Toe", message= "Es empate")
               game_over = True

          # Cambia al siguiente jugador
          else:
               player = 'O' if player == 'X' else 'X'

def reset_game():
     global player, game_over
     player = 'X' # Reiniciar al primer jugador
     game_over = False # Reiniciar estado del juego

     #Limpiar todos los botones
     for row in range(3):
          for col in range(3):
               buttons[row][col]['text'] = ''
               buttons[row][col]['bg'] = '#263238'

root = tk.Tk() # Crear ventana principal
root.title("Tic Tac Toe")   # Titulo de ventana
root.geometry("400x450")    # Tamano de ventana
root.configure(bg='#263238')# Color de fondo

frame = tk.Frame(root, bg='#263238')
frame.place(relx=0.5, rely=0.5, anchor='center') # Centrar el frame

buttons = [[tk.Button(frame, text='', font='normal 20 bold', width=5, height=2,bg='#263238',fg='white',
                      command=lambda row=row, col=col: button_click(row,col))
                      for col in range(3)] for row in range(3)]

# Colocar los botones en una cuadricula
for row in range(3):
     for col in range(3):
          buttons[row][col].grid(row=row, column=col, padx=10, pady=10)

# Boton de reincio
reset_button = tk.Button(root, text='Reiniciar', font='normal 15 bold', command=reset_game, bg='#546E7A', fg='white')
reset_button.place(relx=0.5, rely=0.9, anchor='center')

root.mainloop() # Mantener la ventana abierta y responder a eventos