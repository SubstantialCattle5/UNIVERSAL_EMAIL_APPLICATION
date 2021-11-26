import tkinter as tk

WIDTH, HEIGHT = 350, 350

# Colours
WHITE = '#F0F5F9'
DARK_WHITE = '#C9D6DF'
GREY = '#52616B'
BLACK = '#1E2022'
login_entry, pw_entry = None, None


class Login:
    def __init__(self):
        self.user = str()
        self.pw = str()
        self.root = tk.Tk()
        self.login_pg()

    def login_pg(self):
        global login_entry, pw_entry
        # Window
        self.root.title('Login Page')
        self.root.minsize(width=WIDTH, height=HEIGHT)
        self.root.config(bg=DARK_WHITE)
        # Image
        logo = tk.Canvas(master=self.root, width=350, height=180, bg=DARK_WHITE, highlightthickness=0)
        img = tk.PhotoImage(file="padlock.png")
        logo.create_image(125, 90, image=img)  # Image credits goes to Smashicons
        logo.grid(row=1, column=2, columnspan=2)

        # Login Details
        # Email label
        login_label = tk.Label(master=self.root, text='Email :', bg=DARK_WHITE, fg=BLACK, font=(24))
        login_label.grid(row=2, column=1, sticky='w')

        # Email Entry
        login_entry = tk.Entry(master=self.root, width=30, bg=WHITE, relief=tk.SUNKEN, font=('helvetica', 14))
        login_entry.grid(row=2, column=2, columnspan=2, sticky='w')

        # Password
        pw_label = tk.Label(master=self.root, text='Password :', bg=DARK_WHITE, fg=BLACK, font=(24))
        pw_label.grid(row=3, column=1, sticky='w')

        # Password Entry
        pw_entry = tk.Entry(master=self.root, width=30, bg=WHITE, relief=tk.SUNKEN, font=('helvetica', 14))
        pw_entry.grid(row=3, column=2, columnspan=2, sticky='w')

        # Space
        space = tk.Label(master=self.root, text=' ', bg=DARK_WHITE)
        space.grid(row=4, column=2)

        # Login Button
        login_button = tk.Button(master=self.root, text='Send', bg=GREY, fg=DARK_WHITE, activebackground=BLACK,
                                 activeforeground=WHITE, width=15, command=lambda: self.login())
        login_button.grid(row=5, column=2)

        self.root.mainloop()

    def login(self):
        self.user = login_entry.get()
        self.pw = pw_entry.get()


l = Login()
l.login_pg()
