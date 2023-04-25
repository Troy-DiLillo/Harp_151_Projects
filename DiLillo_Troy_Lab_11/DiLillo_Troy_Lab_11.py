#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Lab 11 Pre-lab. Tkinter Variables.


# In[1]:


#basic dropdown menu
from tkinter import *

root = Tk()
root.title("Dropdown practice")
root.geometry("400x400")

item_list = ["Yellow", "Blue", "Green", "Purple", "Violet", "Black"]

def chosen_option():
    color = value.get()
    result_label = Label(root, text=f"You've chosen {color}")
    root.configure(background=color)
    result_label.pack()
    
value = StringVar()
value.set("Select a Color")
    
dropdown = OptionMenu(root, value, *item_list)
choose_button = Button(root, text="Click to choose", command=chosen_option)

dropdown.pack()
choose_button.pack()

root.mainloop()


# In[2]:


#radio buttons & Tkinter variables
from tkinter import *

root = Tk()
root.title("Radio Buttons")

#intvar helps it keep track of the variable at any one moment
r = IntVar()
r.set("2") #sets it to the second value

def clicked(value): 
    mylabel = Label(root, text=value)
    mylabel.pack()

Radiobutton(root, text="Choice1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Choice2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

root.mainloop()


# In[6]:


from tkinter import *



root = Tk()
root.geometry("700x350")

def selection():
    selected = "You selected the option " + str(radio.get())
    label.config(text=selected)

radio = IntVar()
Label(text="Your Favourite programming language:", font=('Aerial 11')).pack()

r1 = Radiobutton(root, text="C++", variable=radio, value=1, command=selection)
r1.pack(anchor=N)

r2 = Radiobutton(root, text="Python", variable=radio, value=2, command=selection)
r2.pack(anchor=N)

r3 = Radiobutton(root, text="Java", variable=radio, value=3, command=selection)
r3.pack(anchor=N)

# Define a label widget
label = Label(root)
label.pack()

root.mainloop()


# In[23]:


#Exercise 1. Simplify the code above to run more efficiently

from tkinter import *

root = Tk()
root.geometry("700x350")

list = ["C++","Python","Java"]

def selection():
    selected = "You selected the option " + str(radio.get())
    label.config(text=selected)

radio = IntVar()
Label(text="Your Favourite programming language:", font=('Aerial 11')).pack()
n=0
for i in list:
    n += 1
    r = Radiobutton(root, text = i, variable=radio, value= n , command=selection)
    r.pack(anchor=N)

# Define a label widget
label = Label(root)
label.pack()

root.mainloop()


# In[ ]:


#adapted from https://www.tutorialspoint.com/how-to-get-radiobutton-output-in-tkinter
from tkinter import *

root = Tk()
win.geometry("700x350")

def selection():
    ans = radio.get()
    if ans == "4100 miles":
        label.config(text="You're right!")
    else:
        label.config(text="You're wrong :( !")

radio = StringVar()
radio.set("3000 miles")
Label(text="How long is the Nile river?", font=('Aerial 11')).pack()

r1 = Radiobutton(root, text="3000 miles", variable=radio, value="3000 miles", command=selection)
r1.pack(anchor=N)
#anchors https://www.tutorialspoint.com/python/tk_anchors.htm

r2 = Radiobutton(root, text="6300 miles", variable=radio, value="6300 miles", command=selection)
r2.pack(anchor=N)

r3 = Radiobutton(root, text="8000 miles", variable=radio, value="8000 miles", command=selection)
r3.pack(anchor=N)

r4 = Radiobutton(root, text="4100 miles", variable=radio, value="4100 miles", command=selection)
r4.pack(anchor=N)

label = Label(root)
label.pack()

root.mainloop()


# In[ ]:


#from https://www.plus2net.com/python/tkinter-radiobutton.php

from tkinter import * 

root = Tk()
root.geometry("200x200")  # Size of the window 

def my_upd():
    print('Radiobutton  value :',r1_v.get())

r1_v = BooleanVar()   # We assigned Boolean variable here
r1_v.set(True) # Can assign False 

r1 = Radiobutton(root, text='Passed', variable=r1_v, value=True,command=my_upd)
r1.grid(row=1,column=1) 

r2 = Radiobutton(root, text='Failed', variable=r1_v, value=False,command=my_upd)
r2.grid(row=1,column=2) 

root.mainloop()  


# In[25]:


from tkinter import *
 
class GreetingApp(Tk):
    def __init__(self):
        super().__init__()
        self.title('Greeting Application')
        self.geometry("300x300")
 
        self.name_var = StringVar()
        self.name_var.trace('w', self.create_greeting_message)
 
        self.create_widgets()
     
    def create_widgets(self):
        self.description_label = Label(self, text="Enter your name:")
        self.description_label.grid(column=0, row=0)
 
        self.entry = Entry(self, textvariable=self.name_var)
        self.entry.grid(column=1, row=0)
        self.entry.focus()
 
        self.greeting_label = Label(self)
        self.greeting_label.grid(column=0, row=1, columnspan=2)
     
    def create_greeting_message(self, *args):
        name_entered = self.name_var.get()
 
        greeting_message = ""
        if name_entered != "":
            greeting_message = "Hello " + name_entered
         
        self.greeting_label['text'] = greeting_message
 
if __name__ == "__main__":
    app = GreetingApp()
    app.mainloop()


# In[10]:


#Post Lab 11
#Create a Trivia API 
#https://the-trivia-api.com/api/questions?categories=film_and_tv&limit=10&region=US&difficulty=easy

from tkinter import *
import requests

response = requests.get('https://the-trivia-api.com/v2/questions')
response.text


# In[44]:


from tkinter import *
import requests
import json

#Will attempt to make question a label

root = Tk()
root.geometry("900x600")
root.title("Trivia App")


def getQuestion(): 
    url = 'https://the-trivia-api.com/api/questions?categories=film_and_tv&limit=10&region=US&difficulty=easy'
    question = requests.get(url).json()
    for i in question:
        diction= i
        quiz = diction['question']
        print(quiz)
    
getQuestion()


# In[48]:


from tkinter import *
import requests
import json

#First attempting to make question a label

root = Tk()
root.geometry("900x600")
root.title("Trivia App")

r = IntVar()
r.set("2")

def getQuestion(): 
    url = 'https://the-trivia-api.com/api/questions?categories=film_and_tv&limit=10&region=US&difficulty=easy'
    question = requests.get(url).json()
    
    for i in question:
        diction= i
        quiz = diction['question']
        label = Label(root, text = quiz, font = 18, justify = "center").pack()
    
    
    

#stuff for adding buttons later on 
#value = StringVar() 
#value.set("Select a Question")



#label.pack(pady = 20)

#Radiobutton(root, text="Choice1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Choice2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Choice3", variable=r, value=3, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Choice4", variable=r, value=4, command=lambda: clicked(r.get())).pack()

getQuestion()


# In[1]:


#post lab 11
#https://www.freecodecamp.org/news/how-to-create-a-gui-quiz-application-using-tkinter-and-open-trivia-db/


# In[5]:


#Cooperated on project with Rami and Sharon
#Problems with the code. Sometimes need to clikc the correct answer twice. 
import random
from tkinter import *
import requests

url = "https://the-trivia-api.com/api/questions?categories=film_and_tv&limit=10&region=US&difficulty=easy"
get_request = requests.get(url).json()

root = Tk()
root.title("Trivia")
root.geometry("1000x800")


#creating canvas
canvas = Canvas(root, width=800, height=250, bg="khaki1")
canvas.place(relx=.5, rely=.5,anchor= CENTER) #anchors the canvas in the center

#adding text to the canvas
game_display = canvas.create_text(200, 75, text="", fill="black", font=('Helvetica 15 bold'))

#creating the label that will display if something is correct/incorrect
feedback = Label(root, text="", pady=10, font=("arial", 15, "bold"))
scoring = Label(root, text="", pady=10, font=("arial", 15, "bold"))

#decided that the points system was the best way to keep the programming moving forward. Wanted negative points on a wrong answer but error would be thrown saying out of range.
user_answer = StringVar()
user_answer.set("")
points = 0
score = 0
questions_right = 0

def generate_qlist(json):
    question_list = []
    for i in json:
        i = i["question"]
        question_list.append(i)
    return question_list

def gen_question(list_):
    choice = random.choice(list_)
    list_.remove(choice)
    return choice

def generate_answers(json, question): 
    option_list = []
    for i in get_request:
        if i["question"] == question:
            cor = i["correctAnswer"]
            option_list.append(cor)
            for incor in i["incorrectAnswers"]:
                option_list.append(incor)
    random.shuffle(option_list)
    return option_list

def ask_question(question, answers):
    canvas.itemconfig(game_display, text=question, width=300)
    
def gen_radiobuttons(answers):
    y_pos = 140
    for i in answers:
        rad_btn = Radiobutton(canvas, text=i, variable=user_answer, command=eval_score, value=i, font=('Helvetica 10 bold'))
        rad_btn.place(x=50, y=y_pos)
        y_pos+=20
def eval_score():
    answer = user_answer.get()
    global score
    global questions_right
    for i in get_request:
        if i["question"] == current_question:
            old_score = score
            new_score = score
            if i["correctAnswer"] == answer:
                score += 10
                new_score = 10
                questions_right += 1
                scoring["text"] = "Score:", score
                scoring.place(x=400, y=600)
            else:

                feedback["text"] = "choose your answer"
                feedback.place(x=400, y=550)
                scoring["text"] = "Score:", score
                scoring.place(x=400, y=600)
                
            if new_score != old_score:
                main()
            
            if score == 50:
                feedback["text"] = "You've won. How many did you get wrong?"                
                root.destroy()              
def main():
    global current_question
    current_question = gen_question(q_list)
    ans_list = generate_answers(get_request, current_question)
    ask_question(current_question, ans_list)
    gen_radiobuttons(ans_list)
    eval_score()


    
q_list = generate_qlist(get_request)
main()

root.mainloop()

print("You managed to score" + " " + str(score))


# In[ ]:




