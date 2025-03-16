# Simple Quiz Game
print("Welcome to the Python Quiz! 🎮")

score = 0

answer = input("What keyword is used to define a function in Python? \n(a) define \n(b) def \n(c) func \nYour answer: ")
if answer.lower() == "b":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌")

print(f"Your final score: {score}/1")
