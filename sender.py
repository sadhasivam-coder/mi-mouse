# first of all import the socket library
import socket	
from pynput.keyboard import Key#hey i am sadhasivam 
from pynput.keyboard import Listener as Liistener

def on_press(key):
    li=['keys',str(key)]
    c.send(' '.join(li).encode())

    # Collect events until release

# next create a socket object
s = socket.socket()		
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345			

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
import threading
s.bind(('192.168.1.8', port))		
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)	
print ("socket is listening")		
import pyautogui,time
c, addr = s.accept()
print('connection successfull')
from pynput.mouse import Listener
#import logging

#logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_move(x, y):
    l=list(map(str,[x,y]))
    c.send(' '.join(l).encode())
def on_click(x, y, button,tap):
    l=list(map(str,[x,y,'yes']))
    c.send(' '.join(l).encode())
with Listener(on_move=on_move, on_click=on_click),Liistener(on_press=on_press) as listener:
    listener.join()

