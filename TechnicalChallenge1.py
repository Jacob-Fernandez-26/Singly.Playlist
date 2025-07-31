# Technical Challenge 1: Playlist management with a Singly Linked List
# Scenario: You're asked with developing the back-end for a musci app's
# playlist feature. The app should allow users to add songs to the end of their
# playlist and skip to the next song.
# Task: Implementing a singly linked list to manage the songs in a users 
# playlist. The list should support adding songs to the end and retrieving
#  the next song to play.
# Input:
# Operations to be perfomed on the playlist, such as "add song" and :play next.
# Example inputs: add_song("Yesterday"), add_song("Hey Jude"), play_next(),
# add_song("Let it Be"), play_next()
# Expecte Output:
# the current song being played after each operation.
# For the given example, the outputs would be "Song added: Yesterday", 
# "Song added: Hey Jude"< "now Playing: Yesterday", "Song addded: Let it be"< "Now Playing:  Hey Jude"

class SongNode:
    def __init__(self,title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title, save_to_file = True):
        if not title.strip():
            print("Error titulo de la cancion no puede dejarse en blanco")
            return 
        new_song = SongNode(title) 
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song  

        if save_to_file:
            with open(""r"C:\Users\jacob\OneDrive\Documents\terminal34_script\Unit2\playlist.txt", "a") as file:
                file.write(title + "\n")
                           
        print(f"/\Added/\: '{title}'")                   

    def play_next(self):
        if not self.head:
            print("No hay canciones para darle play")
            return
        print((f"Play: {self.head.title}"))
        self.head = self.head.next

    def show_playlist(self):
        if not self.head:
            print("El Playlist esta vacio") 
            return
        print("playlist:")
        current = self.head
        index = 1
        while current:
            print(f"{index}. {current.title}")
            current = current.next
            index += 1

    def show_playlist(self):
        if not self.head:
            print("Playlist esta vacio.")
            return
        print("Current Playlist:")
        current = self.head
        index = 1
        while current:
            print(f"{index}. {current.title}")
            current = current.next
            index += 1

    def load_from_file(self, filename = ""r"C:\Users\jacob\OneDrive\Documents\terminal34_script\Unit2\playlist.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    title = line.strip()
                    if title:
                        self.add_song(title, save_to_file = False)
        except FileNotFoundError:
            pass

playlist = Playlist()
playlist.load_from_file()
print("Playlist Terminal!")

while True:
    print("\nEscoge una Opcion:")
    print("1. Anade una cancion")
    print("2. Play la proxima cancion")
    print("3. Ensena el Playlist")
    print("4. Salida")

    opcion = input("Entra una opcion (1 al 4): ").strip()

    if opcion == "1":
        title = input("Entre Titulo De Cancion: ").strip()
        playlist.add_song(title)
    elif opcion == "2":
        playlist.play_next()
    elif opcion == "3":
        playlist.show_playlist()
    elif opcion == "4":
        print("Adios!")
    else:
        print("Opcion Invalida. Entre Opcion Del 1 Al 4")            



            
