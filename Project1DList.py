from tkinter import *
import random

root=Tk()

root.title("Random Letter")
root.geometry("500x500")

list1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print (list1)

def random_number():
        random_no = random.randint(1,26)
        print(random_no)
        random_lucky_friend = list1[random_no]
        print("Your lucky letter is " + random_lucky_friend)
        
btn1 = Button(root, text="Your random letter is  ", command = random_number)
btn1.place(relx = 0.5, rely = 0.5, anchor=CENTER)

root.mainloop()
