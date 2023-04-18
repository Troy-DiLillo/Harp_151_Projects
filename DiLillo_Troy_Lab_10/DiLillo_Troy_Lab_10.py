#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Prelab Tkinter


# In[ ]:


from tkinter import * # * means everything

root = Tk()  #root widget 
root.geometry("200x100") #set the window size 

myLabel = Label(root, text="Hello World") #going in the root widget

myLabel.pack() #puts on screen, very basic 

root.mainloop() #gotta get it looping/running


# In[ ]:


#pack() versus grid()
#cannot use pack and grid at the same time

root = Tk()

myLabel1 = Label(root, text="Hello World", font=("Arial", 20))
myLabel2 = Label(root, text="This is a message")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop() 


# In[ ]:


#Exercise 1 
# Create a few labels, give them unique text, and try using different fonts and sizes for each.
# use the .grid() to post them on the screen

root = Tk()

myLabel1 = Label(root, text="Hello World", font=("Arial", 20))
myLabel2 = Label(root, text="This is a message")
myLabel3 = Label(root, text="This doesn't seem so bad", font =("Times New Roman", 40))
myLabel4 = Label(root, text="I'm sure I will be proven wrong", font =("Helvetica", 50))

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=0)
myLabel4.grid(row=3, column=0)

root.mainloop() 


# In[ ]:


#Adding a button

root = Tk()
root.geometry("300x100")

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="This is a message")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

def click():
    label3 = Label(root, text="You clicked a button!").grid(row=3, column=0)

button1 = Button(root, text="Click me", command=click, padx=20, pady=20)
button1.grid(row=2, column=0)

root.mainloop() 


# In[ ]:


#button countdown
#code from https://python-course.eu/tkinter/buttons-in-tkinter.php

counter = 0 
def counter_label(label):
    counter = 0
    def count():
        global counter #global variable declaration 
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count) #after(parent, ms, function = None, *args)
    count()
 
 
root = Tk()
root.title("Counting Seconds")
label = Label(root, fg="dark green")
label.pack()
counter_label(label)
button = Button(root, text='Stop', width=25, command=root.destroy) #destroy(parent, command, widgetobject.destroy) 
button.pack()
root.mainloop()


# In[ ]:


# Excercise #2 
#Try creating two different buttons. They can do anything. 

counter = 0 
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()
 
 
root = Tk()
root.title("Counting Moments")
label = Label(root, fg="dark red")
label.pack()
counter_label(label)
button = Button(root, text='Stop', width=100, command=root.destroy) #destroy(parent, command, widgetobject.destroy) 
button.pack()
root.mainloop()

from tkinter import * # * means everything

root = Tk()
root.geometry("200x100") 

myLabel = Label(root, text="Why did you stop my timer?") 

myLabel.pack() 

root.mainloop()


# In[ ]:


#frame widget
#https://pythonbasics.org/tkinter-frame/

root = Tk()  
root.geometry("300x180")

for fm in ["pink", 'red','orange','yellow','green','blue','purple', "brown", "black"]:  
    Frame(height = 20,width = 640,bg = fm).pack()  

root.mainloop() 


# In[ ]:


root = Tk()
topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

redbutton = Button(topframe, text="Red", fg="red")
redbutton.pack(side = LEFT)
bluebutton = Button(topframe, text="Blue", fg="blue")
bluebutton.pack(side = LEFT)

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()


# In[ ]:


#Exercise 3
#Create a few buttons and labeles of your choosing
#Try and create three frames to house them

root = Tk()
topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

leftframe = Frame(root)
leftframe.pack(side = LEFT)


rightframe = Frame(root)
rightframe.pack(side = RIGHT)


redbutton = Button(topframe, text="Red", fg="red")
redbutton.pack(side = LEFT)

bluebutton = Button(topframe, text="Blue", fg="blue")
bluebutton.pack(side = LEFT)

blackbutton = Button(leftframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

greenbutton = Button(rightframe, text="Green", fg="green")
greenbutton.pack(side = RIGHT)

root.mainloop()


# In[ ]:


#message boxes

from tkinter import messagebox

root = Tk()
root.title("Let's Message")

def popup():
    response = messagebox.showinfo("Title Bar", "Message in PopUp") #has a sound too
    
def askyesno(): #returns a boolean 
    answer = messagebox.askyesno("Title Bar", "Do you want to proceed?")
    
    if answer == True:
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You clicked no.").pack()

Button(root, text="Pop-up", command=popup).pack()

root.mainloop()


# In[ ]:


from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Ankur Gajurel Clockitty clocke")

def time():
    string = strftime('%H:%M:%S: %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root , font=("ds-digital", 200), background="black", foreground="green")
label.pack(anchor='center')
time()
mainloop()


# In[ ]:


# Make a calculator. My initial twenty minute attempt

root = Tk()
topframe = Frame(root)
topframe.grid()

entry_user= Entry(root,width=35, border=5).grid()

onebutton = Button(root, text="1")

twobutton = Button(root, text="2")

threebutton = Button(root, text="3")

fourbutton = Button(root, text="4")

fivebutton = Button(root, text="5")

sixbutton = Button(root, text="6")

sevenbutton = Button(root, text="7")

eightbutton = Button(root, text="8")

ninebutton = Button(root, text="9")

zerobutton = Button(root, text="0")

onebutton.grid(row=0, column=0)
twobutton.grid(row=0, column=1)
threebutton.grid(row=0, column=2)
fourbutton.grid(row=1, column=0)
fivebutton.grid(row=1, column=1)
sixbutton.grid(row=1, column=2)
sevenbutton.grid(row=2, column=0)
eightbutton.grid(row=2, column=1)
ninebutton.grid(row=2, column=2)
zerobutton.grid(row=3, column=0)




root.mainloop()


# In[ ]:


# The Doctors calculator
#simple buttons 
root = Tk()

#creating an Entry widget
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = Button(root, text="1", padx=40, pady=10)
button_2 = Button(root, text="2", padx=40, pady=10)
button_3 = Button(root, text="3", padx=40, pady=10)
button_4 = Button(root, text="4", padx=40, pady=10)
button_5 = Button(root, text="5", padx=40, pady=10)
button_6 = Button(root, text="6", padx=40, pady=10)
button_7 = Button(root, text="7", padx=40, pady=10)
button_8 = Button(root, text="8", padx=40, pady=10)
button_9 = Button(root, text="9", padx=40, pady=10)
button_0 = Button(root, text="0", padx=40, pady=10)
button_add = Button(root, text="+", padx=39, pady=10)
button_equal = Button(root, text="=", padx=86, pady=10)
button_clear = Button(root, text="Clear", padx=76, pady=10)
button_subtract = Button(root, text="-", padx=40, pady=10)
button_multiply = Button(root, text="*", padx=39, pady=10)
button_divide = Button(root, text="/", padx=40, pady=10)


#putting the buttons on the screen 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()

#see a much more sophisticated version here:
# https://github.com/copyassignment/tkinter/blob/main/calculator.py


# In[ ]:


#code from https://www.youtube.com/watch?v=gXl88MaxueY

import requests
from tkinter import *

def getNews(): 
    api_key = "f1c70529d3b0428cb705358e2492d497"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])
    
    for i in range(10): 
        my_news = my_news + str(i+1) + ". " + my_articles[i] + "\n"

    label.config(text = my_news)

root = Tk()
root.geometry("900x600")
root.title("News App")

button = Button(root, font = 24, text = "Reload", command=getNews)
button.pack(pady = 20)

label = Label(root, font = 18, justify = "left")
label.pack(pady = 20)

getNews()

root.mainloop()


# In[ ]:


#Use the linked api to create a gui that will display that quote in a Text widget 
# click a button to generate a totally new quote

import requests
from tkinter import *

topframe = Frame(root)
topframe.grid()

def getQuote(): 
    url = "https://api.quotable.io/random"
    quotes = requests.get(url).json()
    quote_box = Text(root).grid
    
    
    
root = Tk()
root.geometry("900x600")
root.title("Quote Generator")

button = Button(root, font = 24, text = "Generate new quote", command=getQuote)
button.pack(pady = 20)

label = Label(root, font = 18, justify = "left")
label.pack(pady = 20)



root.mainloop()


# In[ ]:


#Gibson version of the exercise

from tkinter import font
root = Tk()
root.title("Quotes")
root.geometry("600x400")

def get_quote():
    text_box.delete(0.0, END)
    r = requests.get("https://api.quotable.io/random")
    data = r.json()
    quote = data["content"]
    text_box.insert(END, quote)
    
intro_label = Label(root,text="Here is a quote for you")
text_box = Text(root, font="Elephant", height = 4, width = 30, bg = "#D1E1F3", padx= 30, pady=50)
get_button = Button(root, text="Click to get quote",command=get_quote)

intro_label.pack()
text_box.pack()
get_button.pack()

root.mainloop()
    


# In[ ]:


#Postlab 10

#UI #1 (5pts)
#Using the quotes API, build a GUI that provides a drop-down menu of people randomly chosen from the API
#I want a user to be able to pick from that list and receive a quote that corresponds to that person 
#Ideally, I want to be able to reset that menu & allow people to choose from a new list 


# In[ ]:


#Work done with group member sharon. Random int for problem one was her idea. Also helped after class. 
#Reset button work inspired by stack overflow. Didn't end up working. 


# In[ ]:





# In[10]:


import requests
from tkinter import *
import random

root = Tk()
root.title("Famous Quotes")
root.geometry("600x400")

url = "https://api.quotable.io/authors"
r = requests.get(url)
data = r.json()

author_list = []

random_list = []


def generate_random():
    for i in range (0,5):
        a = random.randint(0,19) #throws an error if the range is increased past this. Think its because thats how many authors are on the "level" that were looking through the api for. There are more authors in total.
        if a not in random_list:
            random_list.append(a)


def generate_authors():
    for i in random_list:
        dict =data['results'][i]
        number = int(i)
        author =dict['slug']
        author_list.append(author)

def chosen_option():
    author = value.get()
    result_label = Label(root, text=f"You've chosen {author}")
    result_label.pack()

    text.delete(0.0, END) #an attempt to clear out the box after use
    url_2 = f"https://api.quotable.io/quotes?author={author}"
    req = requests.get(url_2)
    data_quote = req.json()
    
    index = data_quote['results'][0]
    quote = index['content']
    text_box.insert(END, quote)

def reset(): #attempted reset button
    root.destroy()
    root.mainloop()

generate_random() 
generate_authors() 

value = StringVar()
value.set("Select an Author")

dropdown = OptionMenu(root, value, *author_list)
choose_button = Button(root, text="Click to choose", command=lambda:[generate_random(),generate_authors(),chosen_option()]) #was taken as an idea from what we did in class

text_box = Text(root, font='cooper 8', height=5, width=31)
text = Text(root,height=3, width=40)


reset_button = Button(root, text="click to reset", command = reset) #reset button closes window but does not reopen it. Was unsure how to proceed. Tried reseting the libraries but removed because it would throw errors.

dropdown.pack()
choose_button.pack()
text_box.pack()
reset_button.pack()

root.mainloop()


# In[9]:


from tkinter import *
import requests
import json
from urllib.request import urlopen #using images as our special widget

root = Tk()

lat = "42.098843" #the binghamton latitude and longitude 
lon = "-75.920647"
genius = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

json_file = genius.json()
forecast =json_file["properties"]["forecast"] #taken from prelab 7 work done in class
new_request = requests.get(forecast)
json = new_request.json()

detailed_forecast_days = json['properties']['periods']
for day in detailed_forecast_days:
    name = (day['name'])               #taken from prelab 7
    temp = (day['temperature'])
    temp_unit = (day['temperatureUnit'])
    detail =(day['shortForecast'])

    frame = Frame(root, width = 100, height = 100, bd=2)
    frame.grid()

    date_temp = f"{name}{temp}{temp_unit}"

    labels = Label(frame, text = date_temp,font = ("cooper", 12))
    labels.grid()

    details = Label(frame, text = detail,fg="blue", font = "cooper 12")
    details.grid(column=0)
    
    icon_url = (day['icon'])
    opened = urlopen(icon_url)
    raw_data = opened.read()
    opened.close()
    
    icon = PhotoImage(data=raw_data)
    icon_label = Label(image = icon)
    icon_label.image = icon
    icon_label.grid(column=1)

root.mainloop()


# In[ ]:




