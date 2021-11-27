import smtplib
import json
import tkinter as tk
from tkinter import messagebox
import login_page as lg

# Screen size
WIDTH, HEIGHT = 800, 650

# Colours
WHITE = '#F0F5F9'
DARK_WHITE = '#C9D6DF'
GREY = '#52616B'
BLACK = '#1E2022'

# test email info
myemail = str()
mypassword = str()
send, subject, body = str(), str(), str()

# login page
login = lg.Login()
login.login_pg()
myemail = login.user
mypassword = login.pw


# Obtaining the email service
email_service = myemail.split('@')[1].split('.')[0]
with open('web_smtp_protocols.json' , 'r') as file :
    data = json.load(file)
    email_service_smtp = data[email_service]


def send(sender_email, sub, body_text):
    # Sender's email , subject  and body
    sender = sender_email.get().strip()
    subject = sub.get()
    body = body_text.get(1.0, "end-1c")
    with smtplib.SMTP(email_service_smtp) as connection:
        # Encrypting the mail contents
        connection.starttls()
        connection.login(user=myemail, password=mypassword)
        # sending the mail
        connection.sendmail(from_addr=myemail,
                            to_addrs=f'{sender}',
                            msg=f'Subject : {subject} \n\n {body} ')
        messagebox.showinfo(
            title='Congrats!',
            message='The email is sent!'
        )


if login.check:
    def main_pg():
        # Window
        root = tk.Tk()
        root.minsize(width=WIDTH, height=HEIGHT)
        root.title('Email')
        root.config(bg=DARK_WHITE)

        # logo
        logo = tk.Canvas(master=root, width=350, height=210, bg=DARK_WHITE, highlightthickness=0)
        img = tk.PhotoImage(file="img.png")
        logo.create_image(120, 90, image=img)
        logo.grid(row=1, column=2, columnspan=2)

        # Email heading
        email_label = tk.Label(master=root, text=f'Email Id : {myemail} ', bg=DARK_WHITE, fg=BLACK, font=(24))
        email_label.grid(row=2, column=1, columnspan=2, sticky='w')

        # Space
        space = tk.Label(master=root, text=' ', bg=DARK_WHITE)
        space.grid(row=3, column=2)

        # To label (sender)
        To_label = tk.Label(master=root, text='To :', bg=DARK_WHITE, fg=BLACK, font=(24))
        To_label.grid(row=4, column=1, sticky='w')

        #  Email id entry(sender)
        sender_email = tk.Entry(master=root, width=60, bg=WHITE, relief=tk.SUNKEN, font=('helvetica', 14))
        sender_email.grid(row=4, column=2, columnspan=3, ipady=3, sticky='w')
        sender_email.insert(index=0, string='nilaynathsharan16@gmail.com')

        # Space
        space = tk.Label(master=root, text=' ', bg=DARK_WHITE, font=('helvetica', 14))
        space.grid(row=5, column=2)

        #  Subject
        #  Subject Label
        sub_label = tk.Label(master=root, text='Subject :', bg=DARK_WHITE, fg=BLACK, font=(24))
        sub_label.grid(row=6, column=1)

        #  Subject Entry
        sub = tk.Entry(master=root, width=60, bg=WHITE, relief=tk.SUNKEN, font=('helvetica', 14))
        sub.grid(row=6, column=2, columnspan=3, sticky='w', ipady=3)

        # Space
        space = tk.Label(master=root, text=' ', bg=DARK_WHITE)
        space.grid(row=7, column=2)

        # Body
        # Body label
        body_label = tk.Label(master=root, text='Body :', bg=DARK_WHITE, fg=BLACK, font=(24))
        body_label.grid(row=8, column=1, sticky='nw')

        # Body Text
        body_text = tk.Text(master=root, bg=WHITE, width=60, height=10, font=('helvetica', 14), relief=tk.SUNKEN)
        body_text.grid(row=8, column=2, columnspan=2)

        # Space
        space = tk.Label(master=root, text=' ', bg=DARK_WHITE)
        space.grid(row=9, column=2)

        # send button

        send_button = tk.Button(master=root, text='Send', bg=GREY, fg=DARK_WHITE, activebackground=BLACK,
                                activeforeground=WHITE, width=20, command=lambda: send(sender_email, sub, body_text))
        send_button.grid(row=10, column=3, sticky='w')

        root.mainloop()


    main_pg() # calling the main function
