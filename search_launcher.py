import subprocess
from tkinter.simpledialog import askstring
from tkinter import *
import urllib.parse
import time
import os




global input_list	# for recalling past searches
input_list = [""]		# for recalling past searches
index = -1			# for recalling past searches
index_from_start = "yes"

def get_new_filename():
	counter = 1	
	while True:
		file_path = os.path.join("/mnt/various/BACKUP/syncthing_backup_folder/Pauls_notes_obsidian/_ QUICK NOTE/", "NewNote_"+str(counter)+".md")
		if os.path.isfile(file_path):
			counter+=1
		else:
			return file_path
			break

def save_note(event):
	note = t.get("1.0", "end-1c")
	filename = get_new_filename()
	with open(filename, "w") as f:
		f.write(note)
	f.close
	closeprocedure()

def closeprocedure():
	store_search()
	clear_radio_buttons()
	t.delete("1.0", END)	# deletes contents in text box
	set_top_radio_button()
	root.iconify()			# minimizes window

def store_search():
	INPUT = t.get("1.0", "end-1c")
	if INPUT[-1:] == "\n":
		INPUT = INPUT[:-1]
	input_list.append(INPUT)

def recall_past_up(event):
	global index
	global index_from_start
	if index_from_start == "yes":	# checks if this is the first time pressing ctrl-up
		index = len(input_list)-1	# sets index to last item in the list
		index_from_start = "no"		# sets the variable to now be 'no'
	else:
		index-=1
		if index == -1:	# if the index hits first item in the list go back to the last item in the list
			index = len(input_list)-1
	t.delete("1.0", END)
	t.insert("1.0", input_list[index])

def recall_past_down(event):
	global index
	global index_from_start
	if index_from_start == "yes":	# checks if this is the first time pressing ctrl-down
		index = 1					# sets index to first item entered in list
		index_from_start = "no"		# sets the variable to now be 'no'
	else:
		if index == (len(input_list)-1):	# if the index hits last item in the list reset it
			index = 0
		else:
			index+=1
	t.delete("1.0", END)
	t.insert("1.0", input_list[index])


def open_link(link):
	link = link.replace("#", "%23")	# this symbol cannot be put in a url, %23 is its representation
	command = ["snap", "run", "brave", "--new-tab", link]
	subprocess.run(command, check=True)

def set_top_radio_button():
	var.set(1)
	R1.config(fg="red")

def clear_radio_buttons():
	for rb in [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12]:
		rb.config(fg="black")

def exec_submit(instruc=0):

	if instruc == 1:
		open_link('https://weather.com/en-CA/weather/today/l/Mississauga+Ontario?canonicalCityId=4c22e901b21156f6d1435f69a68aea9eb004d01517be3b3e7489802e4242c2c2')

	else:

		INPUT = t.get("1.0", "end-1c")
		selection = var.get()

		if selection == 1:
			INPUT = INPUT.replace(' ', '+')	# replace new line characters
			open_link('https://search.brave.com/search?q='+INPUT)
		elif selection == 2:
			INPUT = INPUT.replace(' ', '+')	# replace new line characters
			open_link('http://www.google.com/search?q='+INPUT)
		elif selection == 3:
			INPUT = INPUT.replace(' ', '%20')
			open_link('http://www.mapquest.com/search/'+INPUT)
		elif selection == 4:
			INPUT = INPUT.replace(' ', '+')	# replace new line characters
			open_link('https://www.youtube.com/results?search_query='+INPUT)
		elif selection == 5:
			INPUT = INPUT.replace(' ', '+')	# replace new line characters
			open_link('https://www.amazon.ca/s?k='+INPUT)
		elif selection == 6:
			INPUT = INPUT.replace(' ', '%20')
			open_link('https://www.homedepot.ca/search?q='+INPUT)
		elif selection == 7:
			INPUT = INPUT.replace(' ', '+')	# replace new line characters
			open_link('https://www.canadiantire.ca/en/search-results.html?q='+INPUT)
		elif selection == 8:
			INPUT = INPUT.replace(' ', '+')	# replace new line characters
			open_link('https://www.ebay.ca/sch/i.html?_nkw='+INPUT)
		elif selection == 9:
			INPUT = INPUT.replace(' ', '-')	# replace new line characters
			INPUT = INPUT.replace('\n', '').replace('\r', '')	# replace new line characters
			open_link('https://www.kijiji.ca/b-oakville-halton-region/'+INPUT+'/k0l1700277?address=Mississauga%2C%20ON%20L5L%204T6&dc=true&ll=43.531353%2C-79.700897&radius=15.0')
		elif selection == 10:
			INPUT = INPUT.replace(' ', '%20')
			open_link('https://www.facebook.com/marketplace/106262189412553/search?query='+INPUT)
		elif selection == 11:
			open_link('http://'+INPUT)

	closeprocedure()


# tkinter gui setup
root = Tk()
root.title("Launchitz")
root.wm_geometry("+3100+1600")  #adjust for placement on screen, first num is x, 2nd is y
root.geometry("430x620")
var = IntVar()


# F2 & F4 button functions for launching other functions which do not require events
def weather_submit():
	exec_submit(1)
def weather(event):
	weather_submit()
def save_note_submit():
	save_note(1)


# function for submitting selection
def func(event):
    exec_submit()


# function for updating radio colors
def updated_radio_color():
	clear_radio_buttons()		# Reset all radio button colors to black    
	selection = var.get()
	eval(f"R{selection}.config(fg='red')")


# function for keyboard shortcutting selection, ALT+...
def alt_selection(event):
	if event.keysym == 's': var.set(1); updated_radio_color()
	elif event.keysym == 'g': var.set(2); updated_radio_color()
	elif event.keysym == 'm': var.set(3); updated_radio_color()
	elif event.keysym == 'y': var.set(4); updated_radio_color()
	elif event.keysym == 'a': var.set(5); updated_radio_color()
	elif event.keysym == 'h': var.set(6); updated_radio_color()
	elif event.keysym == 'c': var.set(7); updated_radio_color()
	elif event.keysym == 'e': var.set(8); updated_radio_color()
	elif event.keysym == 'k': var.set(9); updated_radio_color()
	elif event.keysym == 'f': var.set(10); updated_radio_color()
	elif event.keysym == 't': var.set(11); updated_radio_color()
	elif event.keysym == 'l': var.set(12); updated_radio_color()
	

# Bind keys to functions
root.bind('<Alt-Key-s>', alt_selection)
root.bind('<Alt-Key-y>', alt_selection)
root.bind('<Alt-Key-a>', alt_selection)
root.bind('<Alt-Key-h>', alt_selection)
root.bind('<Alt-Key-k>', alt_selection)
root.bind('<Alt-Key-f>', alt_selection)
root.bind('<Alt-Key-t>', alt_selection)
root.bind('<Alt-Key-c>', alt_selection)
root.bind('<Alt-Key-e>', alt_selection)
root.bind('<Alt-Key-g>', alt_selection)
root.bind('<Alt-Key-l>', alt_selection)
root.bind('<Alt-Key-m>', alt_selection)
root.bind('<F2>', weather)
root.bind('<F4>', save_note)
root.bind('<Return>', func)		#normal enter button
root.bind('<KP_Enter>', func)	#numberic keypad enter
root.bind('<Control-Up>', recall_past_up)
root.bind('<Control-Down>', recall_past_down)


# Main GUI configuring
font_settings = ("Arial", 16)
font_settings_2 = ("Arial", 24)
empty_line = Label(root, text="")  # Empty label
empty_line.pack()
R1 = Radiobutton(root, text="Search", variable=var, value=1, command=updated_radio_color, underline=0, font=font_settings)
R1.pack( anchor = CENTER)
R2 = Radiobutton(root, text="Google", variable=var, value=2, command=updated_radio_color, underline=0, font=font_settings)
R2.pack( anchor = CENTER)
R3 = Radiobutton(root, text="Mapquest", variable=var, underline=0, value=3, command=updated_radio_color, font=font_settings)
R3.pack( anchor = CENTER)

R4 = Radiobutton(root, text="Youtube", variable=var, value=4, command=updated_radio_color, underline=0, font=font_settings)
R4.pack( anchor = CENTER)
R5 = Radiobutton(root, text="Amazon.ca", variable=var, value=5, command=updated_radio_color, underline=0, font=font_settings)
R5.pack( anchor = CENTER)
R6 = Radiobutton(root, text="HomeDepot.ca", variable=var, command=updated_radio_color, underline=0, value=6, font=font_settings)
R6.pack( anchor = CENTER)
R7 = Radiobutton(root, text="CanadianTire.ca", variable=var, command=updated_radio_color, underline=0, value=7, font=font_settings)
R7.pack( anchor = CENTER)
R8 = Radiobutton(root, text="Ebay.ca", variable=var, underline=0, value=8, command=updated_radio_color, font=font_settings)
R8.pack( anchor = CENTER)

R9 = Radiobutton(root, text="Kijiji.ca", variable=var, underline=0, value=9, command=updated_radio_color, font=font_settings)
R9.pack( anchor = CENTER)
R10 = Radiobutton(root, text="FB Marketplace", variable=var, underline=0, value=10, command=updated_radio_color, font=font_settings)
R10.pack( anchor = CENTER)
R11 = Radiobutton(root, text="Go to Link", variable=var, underline=6, value=12, command=updated_radio_color, font=font_settings)
R11.pack( anchor = CENTER)

empty_line_2 = Label(root, text="")  # Empty label
empty_line_2.pack()
b2 = Button(root, text = "F2 - Weather", font=font_settings, bg="#777777", fg="white", command=lambda:weather_submit())
b2.pack()
b3 = Button(root, text = "F4 - Save Note", font=font_settings, bg="#777777", fg="white", command=lambda:save_note_submit())
b3.pack()
empty_line_3 = Label(root, text="")  # Empty label
empty_line_3.pack()

set_top_radio_button()		#sets first radio button

t=Text(root, height=3, width=50, font=font_settings_2)
t.pack( anchor = W)
t.focus()

b1 = Button(root, text = "Submit", font=font_settings, command=lambda:exec_submit())
b1.pack()

label = Label(root)
label.pack()
root.mainloop()