# implementation of card game - Memory
import Tkinter
import random
from PIL import ImageTk


class GameBoard:
    """ This class initializes the game board by creating the frame. """
    def __init__(self, master):

        self.frame = Tkinter.Canvas(master, width=800, height=100)
        self.frame.grid()

        self.restart = Tkinter.Button(self.frame, text="Restart", command=self.new_game)
        self.restart.grid(row=0, column=0)
        Tkinter.Label(self.frame, text="Turns: %s" %(0)).grid(row=1, column=0)

        self.image = ImageTk.PhotoImage(file="card.png")
        for i in range(16):
            self.draw_hidden(col=i+1)

    def draw_hidden(self, col=None):
        card = Tkinter.Button(self.frame, image=self.image, command=self.frame.quit)
        card.grid(row=0, column=col)

    def draw_exposed(self, val, col=None):
        card = Tkinter.Button(self.frame, text=val, command=self.frame.quit)
        card.grid(row=0, column=col)

    def new_game(self):
        print "Restarting"
        values = range(1,9) * 2
        random.shuffle(values)
        print values
        for i in range(16):
            self.draw_exposed(val=values[i], col=i+1)


# register event handlers
# frame.set_mouseclick_handler(mouseclick)
# frame.set_draw_handler(draw)


master = Tkinter.Tk()
board = GameBoard(master)
master.mainloop()
