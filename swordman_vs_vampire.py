import random
import time

class character:
  def __init__(self, hp, mp, sp, atk, deff, name):
    self.hp = hp
    self.mp = mp
    self.sp = sp
    self.atk = atk
    self.deff = deff
    self.name = name

def sword_draw():
  for i in range(2):
    for j in range(2-i):
      print(" ", end=" ")
    for j in range(2*i+1):
      print("*", end = " ")
    print()
    time.sleep(.2)
    
  for i in range(3):
    print(" ", end=" ")
    for j in range(3):
      print("*",end=" ")
    print()
    time.sleep(.2)
    
  for i in range(1):
    for j in range(5):
      print("*",end=" ")
    print()
    time.sleep(.2)
    
  for i in range(2):
    for j in range(2):
      print(" ", end = " ")
    for k in range(1):
      print("*",end=" ")
    print()
    time.sleep(.2)
    
def blood_draw():
  for i in range(1):
    for k in range(3):
      print(" ", end=" ")
    for j in range(1):
      print("o",end=" ")
    print()
    time.sleep(.2)
    
  for i in range(3):
    for j in range(3-i):
      print(" ", end=" ")
    for k in range(2*i+1):
      if (i == 1 and k == 1) or (i==0 and k==0):
        print("o",end=" ")
      else:
        print("*",end=" ")
    print()
    time.sleep(.2)
    
  for i in range(2):
    for j in range(i+2):
      print(" ", end=" ")
    for k in range(3-(2*i)):
      print("*",end=" ")
    print()
    time.sleep(.2)

def eye_draw():
  for i in range(5):
    for j in range(10-i):
      print(" ", end=" ")
    for k in range(2*i+1):
      if (i==1 and k ==2) or (i==2 and k ==4) or (i==3 and k ==6):
        print("*",end=" ")
      else:
        print("p", end=" ")
    print()


def initial():
  global swordman ; global vampire ;global r
  global option ; global debuff ;global passer
  global gate ; global gate2 ; global buff
  global stage ; global sdr;global dr
  global passer2 ; global multi
  global multy ; global sw_name ; global vp_name
  print()
  print("Welcome to swordman vs vampire!!!")
   
  sw_name = "" ; vp_name = ""
  
  time.sleep(1)
  
  print()
  sword = sword_draw()
  while len(sw_name) == 0:
    sw_name = input("Input swordman(your) name: ")
    if len(sw_name) == 0:
      time.sleep(.5) ; print()
      print("input something!!!") 

  
  time.sleep(1)
  print()  
  blood = blood_draw() 
  while len(vp_name) == 0:
    vp_name = input("Input vampire name: ")
    if len(vp_name) == 0:
      time.sleep(.5) ; print()
      print("input something!!!") 
 

  print()

  swordman = character(1000,300,100,50,75, sw_name)
  passer = " " ; gate = 0 ; buff = " " ; multy = 0
  sdr = 3
  vampire = character(800,500,100,40,55, vp_name)
  dr = 3 ; debuff = " " ; multi = 0 ; stage = 1 ; gate2 = 0
  passer2 = " "

  r = 0 #rounds

  difficulty = " "


  while difficulty != "ok":
    option = input("Choose 1.easy 2.hard: ")
    if option == "1":
      difficulty = "ok"
    elif option == "2":
      print(f"vampire hp +400 and your buff last only 2 turns")
      vampire.hp = 1200 ; print()
      difficulty = "ok"
    if difficulty != "ok":
      print("choose only 1 and 2.")
    
    print()
    
   

def game():
  while swordman.hp > 0 and vampire.hp > 0:
    global r; global passer; global gate
    global stage; global gate2; global debuff
    global passer2 ; global multi ; global buff
    global multy ; global sdr ; global dr
    
    r += 1 ; print("---ROUND ",r, "---")
    if option == "2" and buff == "act":
      print(buff)
      print(f"your atk buff last for {sdr} rounds.")
      print()
      
    if debuff == "act":
      print(f"atk debuff last for {dr} rounds")
      print()
      
    while passer != "ok":
      if 0 <= gate < 100:
        order = input("Choose your move 1.atk 2.def 3.magic: ") 
      elif gate == 100:
        order = input("CHOOSE YOUR MOVE 1.ATK 2.DEF 3.MAGIC 4.ULTI: ")
      if order == "1":
        atk = input("Choose skill to attack 1.normal 2.holy sword strike(20) : ")
        if atk == "1": #normal
          crit = random.uniform(1.25,1.75)
          if crit > 1.5:
            sw = swordman.atk*crit ; sw = int(sw)
            vampire.hp -= sw ; gate2 += sw//8
            print(f"You have dealed {sw} critical damage!!!")
            passer = "ok"
          else:
            sw = swordman.atk*crit ; sw = int(sw) 
            vampire.hp -= sw ; gate2 += sw//8
            print(f"You have dealed {sw} damage!")
            passer = "ok"
        elif atk == "2": #holy sword
          if swordman.mp > 20:
            swordman.mp -= 20
            hol = random.randint(3,6)
            if hol > 4:
              vampire.hp -= swordman.atk*hol ; gate2 += (swordman.atk*hol)//8
              print(f"You have dealed {swordman.atk*hol} critical damage!!!")
              passer = "ok"
            else:
              vampire.hp -= swordman.atk*hol ; gate2 += (swordman.atk)//8
              print(f"You have dealed {swordman.atk*hol} damage!")
              passer = "ok"
          else:
            print("You dont have enough mana.")
      elif order == "2":
        swordman.deff += 30
        
      elif order == "3":
        mg = input("Choose your magic 1.heal(30) 2.atk up(50) 3.purification(30): ")
        if mg == "1": #heal
          if swordman.mp > 30:
            swordman.mp -= 30 ; heal = random.randrange(500,1000)
            swordman.hp += heal 
            print(f"swordman healed {heal} hp.") ; passer = "ok"
          else:
            print("you dont have enough mp")
        elif mg == "2": #atk up
          if swordman.mp >= 50:
            swordman.mp -= 50 ; swordman.atk += 300
            buff = "act"
            print(f"your attack +30 = {swordman.atk}")   
            if buff == "act":
              if option == "2": #game hard
                multy += 1 ; sdr = 3
                passer = "ok" 
            passer = "ok"             
          else:
            print("no enough mp.")
        elif mg == "3": #purification
          if swordman.mp > 30:
            swordman.mp -= 30 ; dr = 0
            passer = "ok"
          else:
            print("not enough mp.")
      elif order == "4" and gate == 100:
        ulti = input("Choose ulti 1.Final sword 2.Recovery: ")
        if ulti == "1":
          ult = swordman.atk*7 ; vampire.hp -= ult
          gate2 += ult//8
          sword_draw()
          print(f"YOU USED FINAL SWORD DEALED {ult} DAMAGED!!!")
          gate = 0 ; passer = "ok"
        elif ulti == "2":
          swordman.hp += 500 ; swordman.atk += 50
          swordman.mp += 200 ; dr = 0
          sword_draw()
          print("YOU USED RECOVERY hp+500 atk+50 mp+200.")
          print(f"NOW YOU HAVE {swordman.hp} hp,{swordman.mp} mp,and {swordman.atk} atk.")
          gate = 0 ; passer = "ok"
    
    print()
    time.sleep(1)         
    while passer2 != "ok" and vampire.hp > 0:
      if vampire.hp > 400 and stage == 1:
        enemy = random.choice(["1", "2","3"]) #normal atk, sucking blood, kaiser nail,cursed
        if enemy == "1":
          cri = random.uniform(1.25,1.75)
          if cri > 1.5:
            vc = vampire.atk*cri ; vc = int(vc)
            swordman.hp -= vc ; gate += vc//8
            print(f"{vampire.name} dealed {vc} critical damage!!!")
            passer2 = "ok"
          else:
            vc = vampire.atk*cri ; vc = int(vc)  
            swordman.hp -= vc ; gate += vc//8
            print(f"{vampire.name} dealed {vc} damage.")
            passer2 = "ok"
        elif enemy == "2":
          if vampire.mp > 75:
            vampire.mp -= 75
            bl = random.randrange(50,80)
            swordman.hp -= bl ; vampire.hp += bl ; gate += bl//8
            print(f"{vampire.name} suck your blood healed and dealed you {bl} damage.")
            passer2 = "ok"
        elif enemy == "3":
          if vampire.mp > 25:
            vampire.mp -= 25
            ecri = random.randrange(2,5)
            swordman.hp -= vampire.atk*ecri ; gate += (vampire.atk*ecri)//8
            print(f"{vampire.name} used kaiser nail dealed {vampire.atk*ecri} damage!!!")
            passer2 = "ok"
      elif vampire.hp < 400 and stage == 1:
        blood_draw()
        stage += 1 ; print(f"{vampire.name} angry!!! hp and atk up.", end = " ")
        vampire.hp += 800 ; vampire.atk += 40
        print(f"{vampire.name} hp = {vampire.hp} atk = {vampire.atk}")
        passer2 = "ok"
      elif vampire.hp > 400 and stage == 2 or vampire.hp < 400 and stage == 2:
        if gate2 >= 100:
          ult2 = vampire.atk*2 ; swordman.hp -= ult2 ; gate2 = 0
          vampire.hp += 200 ; vampire.atk += 20 
          blood_draw()
          print(f"{vampire.name} USED ULTI DEALED YOU {ult2} DAMAGED AND HEALED 200  AND ATK UP 20")
          print(f"NOW {vampire.name} HP = {vampire.hp} AND ATK = {vampire.atk}.")
          passer2 = "ok"
        elif 0 <= gate2 < 100:
          enemy = random.choice(["1","2","3","4"]) # normal attack, sucking blood, kaiser nail
          if enemy == "1":
            cri = random.uniform(1.25,1.75)
            if cri > 1.5:
              vatk = vampire.atk*cri ; vatk = int(vatk)
              swordman.hp -= vatk ; gate += vatk//8
              print(f"{vampire.name} DEALED {vatk} CRITICAL DAMAGE!!!")
              passer2 = "ok"
            else:
              vatk = vampire.atk*cri
              vatk = int(vatk)
              swordman.hp -= vatk ; gate += vatk//8
              print(f"{vampire.name} DEALED {vatk} DAMAGE!") ; passer2 = "ok"
          elif enemy == "2":
            if vampire.mp > 50:
              bl = random.randrange(100,150)
              vampire.mp -= 50 ; vampire.hp += bl ; swordman.hp -= bl
              gate += bl//8
              print(f"{vampire.name} HEALED AND DEALED YOU {bl} DAMAGE!")
              passer2 = "ok"
          elif enemy == "3":
            if vampire.mp > 25:
              vampire.mp -= 25
              ecri = random.randrange(2,5)
              swordman.hp -= vampire.atk*ecri ; gate += (vampire.atk*ecri)//8
              print(f"{vampire.name} USED KAISER NAIL DEALED {vampire.atk*ecri} DAMAGE!!!")
              passer2 = "ok"
          elif enemy == "4":
            if vampire.mp > 50:
              vampire.mp -= 50 ; swordman.atk -= 30
              if swordman.atk <= 0:
                swordman.atk = 0 
              debuff = "act"
              print(f"{vampire.name} REDUCE YOUR ATK FOR 30 now your atk = {swordman.atk}.")
              if debuff == "act":
                if swordman.atk != 0:
                  multi += 1 ; dr = 3
                  passer2 = "ok"
                else:
                  dr = 3 ; passer2 = "ok"
              
                             
    if debuff == "act":
      dr -= 1
      if dr <= 0:
        swordman.atk += 30*multi ; print()
        if swordman.atk < 0:
          swordman.atk = 0
        print(f"+++your atk recover by {30*multi} your atk now are {swordman.atk}.+++")
        dr = 3 ; debuff = "reset" ; multi = 0
    
    if buff == "act":
      # game difficulty hard
      if option == "2": #hard
        sdr -= 1
      if sdr <= 0:
        swordman.atk -= 30*multy ; print()
        if swordman.atk < 0:
          swordman.atk = 0
        print(f"---your atk return by {30*multy} your atk now = {swordman.atk}.---")
        sdr = 3 ; buff = "reset" ; multy = 0

    if swordman.hp < 0:
      swordman.hp = 0
    if vampire.hp < 0:
      vampire.hp = 0 
  
    if gate > 100:
      gate = 100
    if gate2 > 100:
      gate2 = 100
    
    time.sleep(1)    
    print()       
    print(f"{swordman.name} have <{swordman.hp}> hp and >{swordman.mp}< mp.")
    time.sleep(.8)
    print(f"{vampire.name} have <{vampire.hp}> hp and >{vampire.mp}< mp.")
    time.sleep(.8) ; print()
    print(f"{swordman.name} ult {gate}% AND {vampire.name} ulti {gate2}%")
    time.sleep(.8)
    passer = " " ; passer2 = " "
    print()
  after() 

def after():
  global r ; global swordman; global vampire
  global gate; global gate2 ; global option
  global stage; global dr; global sdr
  global multi; global multy ; global buff
  global debuff ; global again ; global difficulty 
  
  print(f"Finish in {r} rounds.")
  if r > 12 and vampire.hp == 0 and option == "1":
    print("you took too long")

  if swordman.hp == 0:
    print(f"{vampire.name} lose") ; print()
    blood = blood_draw()
  elif vampire.hp == 0:
    print(f"{swordman.name} win") ; print()
    sword = sword_draw()
   
  print() 
  again = " " ; difficulty = " "
  
  while again != "yes" and again != "no":
    again = input("Play again (yes) or (no): ").lower()
    if again != "yes" and again != "no":
      print("Type only yes or no.")
 
  if again == "yes":
    swordman = character(1000,300,100,50,75, sw_name)
    vampire = character(800,500,100,40,55, vp_name)
    gate = 0 ; gate2 = 0 ; stage = 1
    dr = 3; sdr = 3 ; multi = 0
    multy = 0 ; buff = "reset" ; debuff = "reset"
    r = 0;print()
    while difficulty != "ok":
      option = input("Choose 1.easy 2.hard: ")
      if option == "2":
        print("vampire hp +400 and swordman buff last only 2 turns.")
        vampire.hp = 1200
      print(); game() 
  elif again == "no":
    print("Bye") ; difficulty = "ok"



def main():
  
  ready = " "
  while ready != "ready":
    ready = input("Are you READY?: ").lower()
    if ready != "ready":
      print()
      print("Type only (ready) ,get it?")
      time.sleep(1)
      
  initial()
  game()
  
  
main()



