'''
Catherine Monteith
CMPSC 472

Lab: Spawn Child Processes

This code runs notepad and deltarune almost simultaenously
and notifies the user when each program closes. Once both programs execute and close
this code will submit a message to the user declaring that they have both closed and end its run.
If either program fails to execute, the user will also be notified.
'''


import subprocess
import threading

#this function opens notepad
def process1():
    p = subprocess.Popen("C:/Windows/notepad.exe", shell=True)
    if p.poll() is None:       #asks if subprocess p (notepad) is running will return None if true
        while p.poll() is None:           #keeps polling while notepad is running
            p.poll()
    returncode1 = p.poll()
    if returncode1 == 0:               #if p.poll() returns 0, the program has stopped..if 1 the program failed to open.
        print("Program 1 has been closed")
    elif returncode1 == 1:
        print("Error: Program1 failed to start")



#This function opens a popular video game called Deltarune
def process2():
    j = subprocess.Popen("C:/Program Files (x86)/SURVEY_PROGRAM/DELTARUNE.exe", shell=True)
    if j.poll() is None: #checks if subprocess j is running, returns None if True
        while j.poll() is None: #continuously polls subprocess until j.poll does not equal None
            j.poll()
    returncode2 = j.poll()
    if returncode2 == 0:#if j.poll() returns 0, the program has been stopped
        print("Program2 has been closed")
    elif returncode2 == 1: #if j.poll() returns 1, the program failed to start
        print("Error: Program2 failed to start")





#These lines initiate multithreading threading so that these functions can run at the same time
thread1 = threading.Thread(target=process1)
thread2 = threading.Thread(target=process2)


#calls threading
thread1.start()
thread2.start()

#Program must wait for both threads to end

thread1.join()
thread2.join()

print("Both Programs are closed, Goodnight")








