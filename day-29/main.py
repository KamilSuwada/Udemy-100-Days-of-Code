import os, random
import pyperclip as p
import tkinter as tk
from tkinter import messagebox

CWD = os.path.dirname(__file__)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters + symbols + numbers
    random.shuffle(password_list)
    
    return "".join(password_list)


def generate_password_pressed():
    password_entry.delete(0, tk.END)
    password = generate_password()
    password_entry.insert(0, password)
    p.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def validate_website(website: str):
    if len(website) < 1:
        messagebox.showinfo(message="Plaese enter the website.", title="Error!")
        return False
    else:
        return True


def validate_email(email: str):
    if len(email) < 1:
        messagebox.showinfo(message="Please enter the email.", title="Error!")
        return False
    else:
        return True


def validate_password(password: str):
    if len(password) < 8:
        messagebox.showinfo(message="Your password should not be shorter than 8 characters.", title="Error!")
        return False
    elif len(password) > 36:
        messagebox.showinfo(message="Your password should not be longer than 36 characters.", title="Error!")
        return False
    else:
        return True



def validate(website: str, email: str, password: str):
    if validate_email(email=email) and validate_website(website=website) and validate_password(password=password):    
        return True
    else:
        return False



def add_button_pressed():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if validate(password=password, email=email, website=website):

        path_to_data = os.path.join(CWD, "data.txt")
        entry = f"{website} | {email} | {password}\n"
        proceed = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\nSave?")

        if proceed:
            with open(file=path_to_data, mode="a") as file:
                file.writelines(entry)
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
image = tk.PhotoImage(file=os.path.join(CWD, "logo.png"))
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)



website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)



website_entry = tk.Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = tk.Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "kamilsuwada@icloud.com")

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)



generate_password_button = tk.Button(text="Generate Password", command=generate_password_pressed)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36,command=add_button_pressed)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()