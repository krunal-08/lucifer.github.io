from tkinter import *
from tkinter import Tk, Button, Frame
import re
from time import sleep
from bitcoin import *
import subprocess
import threading
import tkinter as tk
import requests, json
from bit import Key, PrivateKey

#3HnpWD48knNGdRD4n6xFE3c4dJrUhYgj7A

window = Tk()
window.title("Private key Checker")
window.geometry("1200x1000")
window.iconbitmap('logo.ico')
window.configure(bg='black')
window.resizable(0, 0)

#new code here--------------------------------------------------------------------------------------------------------
    
found = 0
count = 0
# import all key from text file

def file_upload():
    found = 0
    count = 0    
    filename = hashkey1.get()  
    with open(filename, 'r', encoding='utf-8', errors='ignore') as fr:
        for Prikvatekey in fr.readlines():
            Privatekey = Prikvatekey.strip('\n').strip()
            Private_Key = Key(Privatekey)
            
            # Create Address from Private Key
            addr = Private_Key.address
            req = requests.get("https://blockchain.info/balance?active=" + addr).json()
            balance = dict(req)[addr]['final_balance']
            count += 1
            if int(balance) > 0:
                found += 1
                with open('FoundValue.txt', 'a') as vf:
                    vf.write(f"{addr}        Balance: {balance}\n{Privatekey}\n{'=' * 55}\n")
                    Output1.insert(END, f"{addr}        Balance: {balance}\n{Privatekey}\n{'=' * 55}\n")
                    vf.close()
            else:
                
                #print(f"{count} Address: {addr} # Balance: {balance}\n{Privatekey}")
                Output.insert(END, f"{count} Address: {addr} # Balance: {balance}\n{Privatekey}\n")
                with open('nothing.txt', 'a') as tf:
                    tf.write(f"{addr}       Balance: {balance}\n{Privatekey}\n")
                    tf.close()    

    
        
#windowcode--------------------------------------------------------------------------------------------------------
abc = PhotoImage(file='logo1.png')
label17 = Label(window, image=abc,bg = "black")
label17.grid(row = 0, column = 0, sticky = E)

l = Label(window, text = "DEVELOPED BY LUCIFER",bg = "black",foreground="white")
l.config(font =("Courier", 14))
l.grid(row = 0, column = 1, sticky = E)

button4 = Button(window, text = "Cancel",bg = "black",foreground="white", command = window.destroy)
button4.grid(row = 0, column = 5)

hash_key = Label(window, text = "private Key File:  ",bg = "black",foreground="white")
hash_key.config(font =("Courier", 14))
hash_key.grid(row = 2, column = 1, sticky = E)

hashkey1 = Entry(window, width=60)
hashkey1.grid(row = 2, column = 2, pady = 1,padx = 0)


button3 = Button(window, text = "Upload",bg = "black",foreground="white", command=file_upload)
button3.grid(row = 2, column = 5)

Output = Text(window, height = 28, 
              width = 80, 
              bg = "black",foreground="white")
Output.grid(row = 5, column = 2,pady = 20)

Output1 = Text(window, height = 20, 
              width = 80, 
              bg = "black",foreground="white")
Output1.grid(row = 6, column = 2,pady = 20)


window.mainloop()
