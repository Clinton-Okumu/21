print("Lets play a quiz game!")

answer = input("Do you want to play a quiz game?(yes/no) ")
if answer.lower() != "yes":
    quit()

score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score = score + 1
else:
    print("incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("correct")
    score = score + 1
else:
    print("incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct")
    score = score + 1
else:
    print("incorrect")

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print("correct")
    score = score + 1
else:
    print("incorrect")

print("you scored " + str(score) + " questions correctly")
print("you scored a percentage of " + str(score/4*100) + "%")

