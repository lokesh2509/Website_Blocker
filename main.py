from tkinter import *
from ttkthemes import themed_tk as tk
import tkinter.messagebox as tmsg

#--------------GUI--------------

root = tk.ThemedTk()
root.get_themes()
root.set_theme("yaru")
root.resizable(0,0)
root.geometry("600x300")
root.title("Website Blocker - Lokesh Vyas")


def web_block():
    website_lists = link.get()
    Website = list(website_lists.split(","))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                tmsg.showinfo("Blocker", "Already Blocked")
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                tmsg.showinfo("Blocker", "Blocked the website")

host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

l1 = Label(root, text="Website Blocker", font="arial 20 bold")
l1.pack()

l2 = Label(root, text="Enter Website: ", font="arial 10 bold")
l2.place(x=10,y=70)

link=StringVar()
web_entry = Entry(root, width=70,textvariable=link)
web_entry.place(x=110, y=70)

submit_button = Button(root, text="Block", font="arial 10 bold",bg="blue", fg="white", width=10)
submit_button.place(x=250,y=100)

root.mainloop()
