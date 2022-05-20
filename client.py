# This is for the client

from click import command
from flask import request
from vidstream import *
import tkinter as tk
import socket 
import threading

local_ip_address = socket.gethostbyname(socket.gethostname())

############################ Functionality ########################
server = StreamingServer(local_ip_address,7777)
receiver = AudioReceiver(local_ip_address,6666)

def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()



def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'),9999)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()




############################# GUI PART #############################
window = tk.Tk()
window.title("Client")
window.geometry('500x200')

#set window color
window.configure(bg='yellow')

# adding elements to window
label_target_ip = tk.Label(window,text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window,height=1)
text_target_ip.pack()

btn_listen = tk.Button(window,text="Start Listening",width=50,command=start_listening)
btn_listen.pack(anchor=tk.CENTER,expand=True)


btn_screen = tk.Button(window,text="Start Screen Sharing",width=50,command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER,expand=True)



window.mainloop() 

############################# GUI PART #############################