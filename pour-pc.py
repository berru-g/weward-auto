import tkinter as tk
import subprocess
import pyautogui

def launch_android():
    # Exécutez ici votre commande pour afficher votre Android
    subprocess.Popen('chemin_vers_executable_android')

def open_application():
    # Exécutez ici votre commande pour ouvrir l'application souhaitée
    subprocess.Popen('chemin_vers_executable_application')

def automate_clicks():
    # Coordonnées des points à cliquer automatiquement
    points = [(x1, y1), (x2, y2), (x3, y3)]  # Remplacez par les coordonnées réelles

    # Boucle pour effectuer les clics
    for point in points:
        pyautogui.click(point[0], point[1])

# Création de la fenêtre principale
window = tk.Tk()

# Fonctions à exécuter pour chaque option
options = [
    {'text': 'Afficher Android', 'command': launch_android},
    {'text': 'Ouvrir une application', 'command': open_application},
    {'text': 'Automatiser les clics', 'command': automate_clicks}
]

# Ajout des boutons avec les options dans la fenêtre
for option in options:
    button = tk.Button(window, text=option['text'], command=option['command'])
    button.pack()

# Lancement de la boucle principale de la fenêtre
window.mainloop()
