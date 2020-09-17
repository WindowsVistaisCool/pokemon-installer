from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk
from os import system
import ctrl
import sys
import json

def exitpls():
	sys.exit()
def ync():
	MBOX = messagebox.askyesno('d', 'd')
	if MBOX == True:
		print("true")
	elif MBOX == False:
		print("false")
def write_json(game="0A"):
	data = {}
	data['gdata'] = game
	with open('storedconfig.json', 'w') as testfile:
		json.dump(data, testfile, indent=4)
def read_json():
	with open('storedconfig.json', 'r') as testfile:
		readfile = json.load(testfile)
	print(readfile['gdata'])
def install():
	messagebox.showinfo("LOOK", "Look back in the terminal window for more information. This window will dissapear after the task is completed.")
	system("sudo apt install make gcc git")
	system("sudo apt-get install pkg-config flex bison libpng-dev")
	print("Done! You can now return to the GUI")
	
window = Tk()
window.title("POKEMON INSTALL")
window.geometry('650x300')
def rme():
	MBX = messagebox.askyesnocancel("INFO", "Press yes to open README. Close the README window after done reading to continue. This window will dissapear after the task is completed.")
	if MBX == False:
		pass
	elif MBX == True:
		system("mousepad README.txt")
	else:
		pass

if ctrl.get_menu():
	menu = Menu(window)
	new_item = Menu(menu)
	new_item.add_command(label='Exit', command=exitpls)
	new_item.add_command(label='write json', command=write_json)
	new_item.add_command(label='read json', command=read_json)

	menu.add_cascade(label='Dev Tools', menu=new_item)
	window.config(menu=menu)

txt = Entry(window, width=20)
txt.grid(column=1, row=1)
lbl = Label(window, text="Please enter the game name!", font=("Corier New", 10))
lbl.grid(column=1, row=2)
def clicked():
	if len(txt.get()) > 0:
		if txt.get() == "red":
			messagebox.showinfo("Done", "Game set to RED/ENGLISH!")
			res = "Done!"
			lbl.configure(text=res)
			txt['state'] = "disabled"
			btn['state'] = "disabled"
		elif txt.get() == "blue":
			messagebox.showinfo("Done", "Game set to BLUE/ENGLISH!")
			res = "Done!"
			lbl.configure(text=res)
			txt['state'] = "disabled"
			btn['state'] = "disabled"
			write_json("0B")
		elif txt.get() == "gold" or txt.get() == "silver":
			messagebox.showwarning("Warning", "GOLD-SILVER/ENGLISH is not setup yet, please try another game.")
			res = "Error"
			lbl.configure(text=res)
		elif txt.get() == "crystal":
			messagebox.showwarning("Warning", "CRYSTAL/ENGLISH is not setup yet, please try another game.")
			res = "Error"
			lbl.configure(text=res)
		else:
			res = "Invalid game!"
			lbl.configure(text=res)
	else:
		messagebox.showerror("ERROR", "No text provided!")

btn = Button(window, text="ENTER", command=clicked)
if ctrl.enable_input():
	btn['state'] = "disabled"
	txt['state'] = "disabled"
	
btn.grid(column=2, row=1)
bbbtn = Button(window, text="README", command=rme)
bbbtn.grid(column=3, row=1)
bbtn = Button(window, text="EXIT", command=exitpls)
bbtn.grid(column=2, row=2)
labl = Label(window, text="Before entering,\nbe sure to have\nlibraries installed", font=("Courier New", 18))
labl.grid(column=1, row=3)
battn = Button(window, text="INSTALL\nLIBRARIES", command=install)
battn.grid(column=2, row=3)
if ctrl.enable_exit():
	bbtn['state'] = "disabled"
if ctrl.enable_readme():
	bbbtn['state'] = "disabled"
txt.focus()

window.mainloop()
