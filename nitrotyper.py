
from selenium import webdriver
import time
from tkinter import *
from pyautogui import write



root = Tk()
root.title("Typing.com")
root.geometry("500x500")
global scale_widget
scale_widget = Scale(from_=0, to=1, resolution=.001)
scale_widget.pack()


def webdriverS():
    #webdriver shit
    global widgetScale
    widgetScale = float(scale_widget.get())
    print(widgetScale)
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    global driver
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.nitrotype.com/")


def mainfunc():
    lettersChrome = driver.find_elements_by_class_name("dash-word")
    time.sleep(3)
    num = len(lettersChrome)
    bad_chars = ['\n']
    widgetScale = float(scale_widget.get())

    for i in range(num):

        printt = lettersChrome[i].text
        if printt == NONE:
            continue
    
        printt = ''.join(i for i in printt if not i in bad_chars)
        print(printt)
        write(printt, interval=widgetScale)

        
button2 = Button(root, text="Initialize", command = webdriverS)
button1 = Button(root, text="GO", command = mainfunc)

button2.pack()
button1.pack()

root.mainloop()