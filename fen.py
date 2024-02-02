import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

def charger_fichier():
    fichier = filedialog.askopenfilename()

    if fichier:
        # Charge l'image à partir du fichier avec OpenCV
        image_cv2 = cv2.imread(fichier)
        
        # Convertit l'image de BGR à RGB (OpenCV utilise BGR par défaut)
        image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)

        # Convertit l'image en format Tkinter PhotoImage
        image_tk = ImageTk.PhotoImage(Image.fromarray(image_rgb))

        # Affiche l'image dans une nouvelle fenêtre
        nouvelle_fenetre = tk.Toplevel(fenetre)
        nouvelle_fenetre.title("Image chargée")

        # Crée une étiquette pour afficher l'image
        etiquette_image = tk.Label(nouvelle_fenetre, image=image_tk)
        etiquette_image.image = image_tk  # Garde une référence à l'objet pour éviter la suppression par le ramasse-miettes
        etiquette_image.pack()

# Crée une fenêtre principale
fenetre = tk.Tk()
fenetre.title("Charger une image avec OpenCV")

# Crée un bouton pour charger un fichier
bouton_charger = tk.Button(fenetre, text="Charger une image", command=charger_fichier)
bouton_charger.pack(pady=20)

# Lance la boucle principale de la fenêtre
fenetre.mainloop()
