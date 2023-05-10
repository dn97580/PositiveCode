# This program create three buttons and when 
# pressed, it will display a POSITIVE QUOTE.

import tkinter
import tkinter.messagebox
import random

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create three Button widgets. The do_something method
        # should be executed when the user clicks each Button.
        self.button1 = tkinter.Button(self.main_window, text='Button 1', command=self.show_quote)
        self.button2 = tkinter.Button(self.main_window, text='Button 2', command=self.show_quote)
        self.button3 = tkinter.Button(self.main_window, text='Button 3', command=self.show_quote)
        
        # Create a Quit button. When this button is clicked
        # the root widget's destroy method is called.
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        # Pack the Buttons.
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.quit_button.pack()
        
        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The show_quote method is a callback function
    # for the Button widgets. It displays a positive
    # quote in an info dialog box.
    def show_quote(self):
        quotes = ['Learn from yesterday, live for today,\hope for tomorrow. The important thing is not to stop questioning. \ -Albert Einstein',
                  'Great things in business are never done by one person.\ They are done by a team of people\ - Steve Jobs',
                  'Software is a great combination between artistry and engineering.\ - Bill Gates',
                  'Positive anything is better than negative nothing. -Elbert Hubbard',
                  'It is possible to invent a single machine which can be used to\ compute any computable sequence\ - Alan Turing']
        quote = random.choice(quotes)
        tkinter.messagebox.showinfo('Positive Quote', quote)

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()




