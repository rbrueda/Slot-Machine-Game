import logic
# Tkinter is a library for the GUI
import tkinter 
#import modules from tkinter
from tkinter import font
from tkinter.font import Font
from tkinter import messagebox
#library that allows support for opening , manipulating, and saving different file formats
from PIL import ImageTk, Image
#cross-platform API that allows to play sound asynchronously
from playsound import playsound
from play_sounds import play_file
#tracks path of files
from pathlib import Path
import time
from time import sleep
#allows differnet parts of program to run concurrently
import threading
from threading import Thread
from threading import Event

event = Event()

class PlayingMusic(object):
    def __init__(self):
        #initalizes an object in the class to a Thread
        self.t1 = threading.Thread(target = play_my_sound, daemon=True)
        
def play_my_sound():
    #plays sound
    playsound('assets/song.mp3')

def loop():
    #allows to play block of code indefinitely
    while True:
        #checks if the object instantiated for MyClass() is alive (ie. checks if thread is alive)
        if not play_music.t1.is_alive():
            play_music.t1 = threading.Thread(target = play_my_sound, daemon =True)
            play_music.t1.start()
        #kills thread --this is detected by event being set when clicked on exit button on tkinter window
        if (event.is_set()):
            break
            
#global variable money
money = 300


def main():

    # Intiating the main window
    window = tkinter.Tk()
    window.title("Slot Savory!")

    results = ["","assets/rich.png", "assets/bow.jpg", "assets/lobster.jpg","assets/moon.jpg","assets/sandwich.jpg","assets/blueberry.jpg","assets/strawberry.jpg","assets/cranberry.jpg","assets/homeless.jpg","assets/mad-face.jpg","assets/pickle.jpg"]

    # Creating the Canvas --> To add pictures and text onto
    game = tkinter.Canvas(window, width = 1080, height = 810)  
    game.pack()


    # Adding the Background
    background = ImageTk.PhotoImage(Image.open("assets/Background.jpg"))
    game.create_image(540, 405, image=background)

    # Creating an invisible circle and "spin" text for the button
    game.create_text(860,123,text="SPIN",fill="White",font=("monospace", 25))
    #create_oval(x0, y0, x1, y1)
    spinButton = game.create_oval(819,88,897,164,outline="")

    #button to retrieve money
    #create_rectangle(x0, y0, x1, y1)
    terminateButton = game.create_rectangle(764,692,1058,768,outline="")

    # Money text:
    game.create_text(538,654,text=str(money)+".00",fill="White",font=("monospace", 45), tags="result")


    def exit():
        MsgBox = messagebox.askquestion("Slot Savory!", "Are you sure you want to exit?")
        if MsgBox == 'yes':
            #closes the tkinter window
            window.destroy()
            #create an event for thread
            event.set()

    window.protocol("WM_DELETE_WINDOW", exit)


    # The function to run when the button is pressed
    def spin(event):
        # Removes the previous results
        game.delete("result")

        # Adds the proper slots that were randomized from logic.py: 
        var = logic.getResults()
        global slot1
        global slot2
        global slot3
        #retrieve all the images based on the result from logic
        slot1 = ImageTk.PhotoImage(Image.open(results[var[0]]))
        slot2 = ImageTk.PhotoImage(Image.open(results[var[1]]))
        slot3 = ImageTk.PhotoImage(Image.open(results[var[2]]))
        #display slot contents on the screen
        game.create_image(367,444, image=slot1,tags="result")
        game.create_image(533,444, image=slot2,tags="result")
        game.create_image(699,444, image=slot3,tags="result")

        
        # Stops the sound after 2.1s: 
        time.sleep(2.1) 

        #initialize current money value from logic to variable gainLoss
        gainLoss = logic.moneyEarned()
        #allows to change a global variable inside a function
        global money
        #add gainLoss to total money variable named money
        money += gainLoss
        
        #if total money is less than 0
        if money <= 0:
            #clear all existing contents from screen except background image
            game.delete("all")
            game.create_image(540, 405, image=background)
            #update to the screen
            game.update()
            #display the text "GAME OVER" to the screen
            game.create_text(540,90,text="GAME OVER",fill="White",font=("monospace", 100),tags="result")  
            play_file(Path('assets/loseMoney.mp3'), block=False)
        #if gainLoss value is positive
        elif (gainLoss > 0):
            #display expression to the screen
            game.create_text(540,60,text="You gained $" + str(gainLoss),fill="White",font=("monospace", 60), tags="result")
            #play good sound
            play_file(Path('assets/gainMoney.mp3'), block=False)
        elif (gainLoss < 0):
            game.create_text(540,60,text="You lost $" + str(gainLoss * -1),fill="White",font=("monospace", 60), tags="result")
            #play bad sound
            play_file(Path('assets/loseMoney.mp3'), block=False)
        #if gainLoss value is 0
        else:
            game.create_text(540,50,text="You gained nothing.",fill="White",font=("monospace", 60),tags="result")
            

        # Displays the total amount of money on the screen:
        game.create_text(538,654,text=str(money)+".00",fill="White",font=("monospace", 45),tags="result")

    #if clicked "Claim your money" button -- retrieves current money and ends game
    def terminate(event):
        #delete all existing contents except background image
        game.delete("all")
        game.update()
        game.create_image(540, 405, image=background)
        #displays the amount of money earned from game onto the screen
        game.create_text(540,60,text="YOU EARNED $" + str(money) + "!",fill="White",font=("monospace", 60), tags="result")

    # Allows the invisible circle to act like a button:
    game.tag_bind(spinButton, '<ButtonPress-1>', spin)     

    #Allows the invisible rectangle to act like a button:
    game.tag_bind(terminateButton, '<ButtonPress-1>', terminate)

    # Neccessary line to loop through the entire thing:
    window.mainloop()


#allows you to execute code when the file runs of a script  
if __name__ == "__main__":
    #creates instance for PlayingMusic class
    play_music = PlayingMusic()
    #starts thread that loops through music
    Thread(target = loop).start()
    #starts thread that works with the user interface
    #set daemon to True to ensure it is killed once they have finished
    Thread(target = main, daemon = True).start()
