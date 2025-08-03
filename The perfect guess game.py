import random as rd
comp=rd.randint(1,100)
player=-1
i=1
while player!=comp:
   player=int(input("Enter the number between 1-100: "))
   if comp>player:
        print("Choose higher number...")
   elif comp<player:
        print("Choose lower number...")
   else:
       print(f"You choosed correct number \nYou have taken {i} attempts to guess")
   n=(f"Your number of guesses: {i}")
   i+=1