print("welcome to my quiz game")

playing = input("Do you want to play the game?")

if playing.lower() != "yes":
    quit()
print("lets play")
score = 0
answer = input("what does CPU stands for?")

if answer.lower() == "central processing unit":
    print("yes that is the correct answer")
    score += 1

else:
    print("no, the answer is central processing unit")

answer = input("what does WWW stands for?")

if answer.lower() == "world wide web":
    print("yes that is the correct answer")
    score += 1

else:
    print("no, the answer is world wide web")

answer = input("who is the main protagonist of despecable me series?")

if answer.lower() == "gruu":
    print("yes that is the correct answer")
    score += 1

else:
    print("no, the answer is Gruu")


answer = input("which country is known as land of rising sun?")

if answer.lower() == "japan":
    print("yes that is the correct answer")
    score += 1

else:
    print("no, the answer is Japan")

print("you got " + str(score) +  " correct answers")