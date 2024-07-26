import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer

    # Make a variable and initialize it to a random number between 0 and 3
    A1 = random.randint(0, 1)
    # If the random number is 0
    A2 = simpledialog.askstring(title="8ball", prompt="Ask any yes or no question and the 8 ball will answer it.")
        # tell the user "Yes"

    if A1 == 0:
        messagebox.showinfo(message="yes")
    elif A1 == 1:
        messagebox.showinfo(message="no")
    elif A1 == 2:
        messagebox.showinfo(message="a little bit")
    elif A1 == 3:
        messagebox.showinfo(message="10000000000000%")
    elif A1 == 4:
        messagebox.showinfo(message="maybe")
    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
