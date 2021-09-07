from tkinter import *
from pywhatkit import *	

def searchGoogleWindow():
	win = Tk()
	win.title("Search something on Google")

	def searchterm():
		user_input = e.get()
		search(user_input)

	text = Label(win, text="Search Google", font="Calibri 15 normal")
	text.pack()

	e = Entry(win)
	e.pack()

	b = Button(win, text="search", padx=20, pady=20, command=searchterm)
	b.pack()



	win.mainloop()

def searchYoutubeVideoWindow():
	win = Tk()
	win.title("Search videos on Youtube")

	def searchYoutube():
		user_input = e.get()
		playonyt(user_input)

	text = Label(win, text="Search Youtube", font="Calibri 15 normal")
	text.pack()

	e = Entry(win)
	e.pack()

	b = Button(win, text="search", padx=20, pady=20, command=searchYoutube)
	b.pack()



	win.mainloop()


def mainwindow():
	root = Tk()

	b1 = Button(root, text="Search Google", command=searchGoogleWindow)
	b1.pack()

	b2 = Button(root, text="Search Youtube", command=searchYoutubeVideoWindow)
	b2.pack()

	root.title("GUISearch")
	root.geometry('300x300')
	root.mainloop()

mainwindow()
