import tkinter as tk
from tkinter import filedialog
import pygame

class AudioPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Classifier")
        self.master.geometry("400x200")

        self.init_ui()

    def init_ui(self):
        select_button = tk.Button(self.master, text="Sélectionner un fichier audio", command=self.select_audio_file)
        select_button.pack(pady=20)
        play_button = tk.Button(self.master, text="Classify", command=self.play_audio)
        play_button.pack(pady=10)

    def select_audio_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers audio", "*")])
        if file_path:
            self.audio_file = file_path
            print(file_path)
            print('--------')
            print(f"Fichier audio sélectionné : {self.audio_file}")

    def play_audio(self):
        if hasattr(self, 'audio_file'):
            pygame.mixer.init()
            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play()
        else:
            print("Sélectionnez d'abord un fichier audio.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayerApp(root)
    root.mainloop()
