import time
import random

time.sleep(0.1)
print("Hello, and welcome to the Hunger Games!")
time.sleep(0.1)
print("...")
time.sleep(1)
player1 = input("Input Player 1: ")
player2 = input("Input Player 2: ")
player3 = input("Input Player 3: ")
player4 = input("Input Player 4: ")
player5 = input("Input Player 5: ")
player6 = input("Input Player 6: ")
player7 = input("Input Player 7: ")
player8 = input("Input Player 8: ")
player9 = input("Input Player 9: ")
player10 = input("Input Player 10:  ")
print("...")
time.sleep(1)
player_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10]
survivelist=["gathered food","grabbed a glock","grabbed a knife","grabbed a sword","gathered food","gathered food","has made camp","has made camp","has grabbed a crosbow","has grabbed a bow and arrow","has grabbed a hammer","has fled","has fled","has fled","has grabbed a lighter","has grabbed some rope"]
survivelist1=["gathered food","grabbed a glock","grabbed a knife","grabbed a sword","gathered food","gathered food","has made camp","has made camp","has grabbed a crosbow","has grabbed a bow and arrow","has grabbed a hammer","has fled","has fled","has fled","has grabed some rope","has grabbed some rope"]
kill=["has smited","has stabbed","has posioned","has killed" ,"has shot","has stabbed","has stabbed","has killed","has smited","has killed","has crushed","has killed"]
teamsurvive=["are hunting together","have made camp together","shared supplies","are hunting together"]
teamhunt=["has stolen from","is hunting for","is targeting"]
teamkill=["has smited","has killed","has shot","has crushed"]
hunt=["is hunting for","has stolen from","is targeting"]
discuss=["is discussing the Hunger Games"]
whattodo=[kill,survivelist,survivelist1,teamsurvive,teamhunt,teamkill,hunt,discuss]
print("")
print("...")
print("Press enter to continue after every character action.")
print("")
while True:
  victim=(random.choice(player_list))
  action=(random.choice(whattodo))
  focus=(random.choice(player_list))
  focus2=(random.choice(player_list))
  if action==kill:
    victim=(random.choice(player_list))
    actionkill=(random.choice(kill))
    print(focus,actionkill,victim)
    if focus==victim:
      print(focus,"has commited self oof!")
    if victim in player_list:
      player_list.remove(victim)
  else:
    if action==survivelist:
      print(focus,random.choice(survivelist))
    else:
      if action==survivelist1:
        print(focus,random.choice(survivelist1))
  if action==teamsurvive:
    if focus==focus2:
      print("")
      print(focus,"is thinking about home.")
    else:
      teamdo=(random.choice(teamsurvive))
      print("")
      print(focus,"and",focus2,teamdo)
  if action==teamhunt:
    if focus==focus2:
      print("")
      print(focus,"is hunting for",victim)
    if focus==victim or focus2==victim:
      print("")
      print(focus,"is hunting for",focus2)
    else:
      teamdo=(random.choice(teamhunt))
      print("")
      print(focus,"and",focus2,teamdo,victim)
  if action==teamkill:
    if focus==victim:
      print("")
      print(focus,"is sick!")
    victim=(random.choice(player_list))
    actionkill=(random.choice(teamkill))
    print(focus,"and",focus2,actionkill,victim)
    if victim in player_list:
      player_list.remove(victim)
  if action==hunt:
    if focus==victim:
      print("")
      print(focus,"has overheard someone!")
    victim=(random.choice(player_list))
    actionkill=(random.choice(teamhunt))
    print(focus,actionkill,victim)
  if action==discuss:
    print("")
    print(focus,"is discussing the Hunger Games with",focus2)
    if focus==focus2:
      print(focus,"is talking to him/her self.")
  if len(player_list)==1:
    time.sleep(1)
    print("")
    print("...")
    time.sleep(1)
    print("")
    print("............................................")
    print("The winner of the HUNGER GAMES is",player_list[0])
    print("............................................")
    break
  conad=input("")
print("") 
print("-----------------------------------------")
print("Pando Conglomerate-HUNGER GAMES SIMULATOR")
print("-----------------------------------------")