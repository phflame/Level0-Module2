import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    R1 = random.randint(1, 9)
    R2 = random.randint(0, 9)
    R3 = random.randint(0, 9)
    R4 = random.randint(0, 9)
    R5 = random.randint(0, 9)
    R6 = random.randint(0, 9)


    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket

    messagebox.showinfo(message=str(R1)+str(R2)+str(R3)+str(R4)+str(R5)+str(R6))
