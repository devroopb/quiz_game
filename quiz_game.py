# Made by Devroop Banerjee
# This is a simple quiz game which asks 5 questions, provides feedback on answers and returns the score

print("Welcome to my quiz game!")

playing = input("Do you want to play? (y/n) ")

if playing.lower() == 'n': quit()
else: print("Type q to exit at any time.\nOkay, let's play!\n")

score = 0

q1 = input("What does CPU stand for? ")
if q1 == "central processing unit":
	print("Correct. Good job!")
	score +=1
elif q1 == 'q':
	print("\nscore: "+str(score))
	quit()
else: print("That's not correct.")

q2 = input("\nWhat does RAM stand for? ")
if q2 == "random access memory":
	print("Correct. Good job!")
	score +=1
elif q2 == 'q':
	print("\nscore: "+str(score))
	quit()
else: print("That's not correct.")

q3 = input("\nWhat does GPU stand for? ")
if q3 == "graphics processing unit":
	print("Correct. Good job!")
	score +=1
elif q3 == 'q':
	print("\nscore: "+str(score))
	quit()
else: print("That's not correct.")

q4 = input("\nWhat does PSU stand for? ")
if q4 == "power supply unit":
	print("Correct. Good job!")
	score +=1
elif q4 == 'q':
	print("\nscore: "+str(score))
	quit()
else: print("That's not correct.")

q5 = input("\nWhat does GUI stand for? ")
if q5 == "graphical user interface":
	print("Correct. Good job!")
	score +=1
elif q5 == 'q':
	print("\nscore: "+str(score))
	quit()
else: print("That's not correct.")

print("Your final score is: " +str(score))