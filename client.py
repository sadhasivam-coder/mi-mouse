# Import socket module
import socket
import pyautogui

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 12345			
import os
# connect to the server on local computer
s.connect(('192.168.1.8', port))
print('connected successfully')
import subprocess
while True:
# receive data from the server and decoding to get the string.
    v=(s.recv(1024).decode())
    inp=v.split()
    o=len(inp)
    #if the input is length of 2 
    if o==2:
        #print(inp)
        if inp[0]=='keys':
            pyautogui.press(inp[1][1:-1])
        else:
            pyautogui.moveTo(int(inp[0]),int(inp[1]))
    #mouse click monitoring
    if o==3 and inp[2]=='yes':
         pyautogui.click()
# close the connection
#s.close()