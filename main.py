from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

web_text = None
user_text = None
password_text = None


# ________________________________________________search_________________________________________________________________

def find_password():
    global web_text
    web = web_text.get()
    try:
        with open("data.json", "r") as data_file:
            try:
                data = json.load(data_file)
                user = data[web]["user"]
                code = data[web]["password"]
                messagebox.showinfo(title="web", message=f"website: {web} \nemail: {user}\npassword: {code}")

            except KeyError:
                messagebox.showwarning(title=None, message=f"No details for '{web}' exists")

    except FileNotFoundError:
        messagebox.showwarning(title=None, message=f"no data is stored")


# ______________________________________________save Password___________________________________________________________
def get_info():
    global web_text, user_text, password_text
    web = web_text.get()
    user = user_text.get()
    password = password_text.get()
    new_data = {web: {
        "user": user,
        "password": password
    }}
    if len(web) == 0 or len(password) == 0:
        messagebox.showwarning('Oops!', "Please don't leave any boxes empty.")
    else:

        is_ok = messagebox.askokcancel(title=web,
                                       message=f"these are the details entered:\nwebsite: {web}\nemail: {user}\n "
                                               f"password: {password}\n is it ok to save")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
                    f.close()
            finally:
                web_text.delete(0, END)
                password_text.delete(0, END)


# ------------------------------------- PASSWORD GENERATOR -------------------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0, password)


# _______________________________________________UI________________________________________________
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(window, width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(0, 0, image=img, anchor='nw')
canvas.grid(row=0, column=0, columnspan=3)
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
web_text = Entry(width=21)
web_text.focus()
web_text.grid(row=1, column=1)
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_text = Entry(width=40)
user_text.grid(row=2, column=1, columnspan=2)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_text = Entry(width=21)
password_text.grid(row=3, column=1)
user_text.insert(0, "my_email@email.com")
# Buttons:
generate_password = Button(text="Generate Password", width=13, command=generate_password)
generate_password.grid(row=3, column=2)
search = Button(text="search", width=13, command=find_password)
search.grid(row=1, column=2)
add_button = Button(text="add", width=39, command=get_info)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
