# implementation of card game - Memory
import Tkinter
import random
from PIL import ImageTk


class GameBoard:
    """ This class initializes the game board by creating the frame. """
    def __init__(self, master):

        frame = Tkinter.Canvas(master, width=800, height=100)
        frame.grid()

        self.restart = Tkinter.Button(frame, text="Restart", command=frame.quit)
        self.restart.grid(row=0, column=0)
        Tkinter.Label(frame, text="Turns: %s" %(0)).grid(row=1, column=0)

        self.image = ImageTk.PhotoImage(file="card.png")
        for i in range(12):
            self.draw(frame, image=self.image, col=i+1)

    def draw(self, frame, image, col):
        self.card = Tkinter.Button(frame, image=image, command=frame.quit)
        self.card.grid(row=0, column=col)


# helper function to initialize globals
def new_game():
    pass


# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass


# register event handlers
# frame.set_mouseclick_handler(mouseclick)
# frame.set_draw_handler(draw)


master = Tkinter.Tk()
board = GameBoard(master)
master.mainloop()
