import tkinter as tk
WIDTH , HEIGHT = 350 , 600

# Colours
WHITE = '#F0F5F9'
DARK_WHITE = '#C9D6DF'
GREY = '#52616B'
BLACK = '#1E2022'


class Login :
    def __init__(self):
        self.user = str()
        self.pw  = str()
        self.root = tk.Tk()
    def login_pg(self):
        # Window
        self.root.title('Login Page')
        self.root.minsize(width= WIDTH , height=HEIGHT)
        self.root.config(bg = DARK_WHITE)
        # Image
        logo = tk.Canvas(master= self.root, width=350, height=210, bg=DARK_WHITE, highlightthickness=0)
        img = tk.PhotoImage(file="padlock.png")
        logo.create_image(180, 90, image=img) #Image credits goes to Smashicons
        logo.grid(row=1, column=2, columnspan=2  )


        # Login Details
        login = 





        self.root.mainloop()

l = Login()
l.login_pg()