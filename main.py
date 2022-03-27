
import time

from random import randint as t
import cursor

cursor.hide()


def clear():
    print("\033c",end = "")


def load():
  suc = "\033[1m\033[38;2;255;0;0m"
  what = ["Toad is Getting Information", "Toad is Unpacking information", "Toad is Indexing Place", "Toad is Writing Files", "Toad is Activating Program"]
  lLen = ["\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m","\033[4m\033[1m \033[0m"] 
  
  for j in range(len(what)):
    for c in range(t(3, 7)):
      for i in range(len(lLen)):
        lLen[i] = suc + "\033[4m\033[38;2;255;0;255m\033[1m    \033[0m"
        print("\033[48;2;255;50;75m              \033[1mLOADING              \033[0m\n\nStatus [\033[93m" + str(j + 1) + "\033[0m - \033[93m"+ str(len(what)) + "\033[0m]\n\033[1m" + what[j]+"\033[0m\n\033[1m"+ "".join(lLen)+ "\033[0m\n\n\033[48;2;255;50;75m              \033[1mLOADING              \033[0m")

        lLen[i] = "\033[4m\033[1m \033[0m"
        time.sleep(0.065)
        print("\033c",end = "")


  clear()        
  print("\033[48;2;50;255;75m               \033[1mDONE              \033[0m\n") 
  lLen[i] = suc + "__\033[0m"
  print("Status [\033[38;2;0;255;0m" + str(j + 1) + "\033[0m - \033[38;2;0;255;0m"+ str(len(what)) + "\033[0m]")
  #print("\033[1m" + what[j]+"\033[0m") 
  #print("\033[1m"+ "".join(lLen)+ "\033[0m")
  print("\n\033[48;2;50;255;75m               \033[1mDONE              \033[0m")    
  input("\n\n\t[ENTER] >") 
  clear()       



load()




