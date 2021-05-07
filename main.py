import documents as documents

print("Hello world")
print("   /|")
print("  / |")
print(" /__|")
print("There once was a man named john  ")
print("he was 60  ")
print("he liked his name john ")
print("but he didnt like being 60")

charactername = "john "
characterage = 60.5
print("There once was a man named  " + charactername)
print("he was" + str(characterage) + "years")
print("he liked his name  " + charactername)
print("but he didnt like being " + str(characterage))
phrase = "Girrafe academy "
print(phrase + "is cool")
print(phrase.lower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0].isupper())
print(phrase[1].isupper())
print(phrase[7])
print(phrase.replace("Girrafe", "elephant"))
number = -5
print(abs(number))
print(pow(number, 2))
print((max(2, 3, 6, 7
           )))
name = input("enter your name :")
age = input("enter your age:")
print("Hello " + name + " " + "you are :" + age + "  years old")
num1 = input(" enter number 1 ")
num2 = input("enter number 2: ")
result = int(num1) + int(num2)
print(result)
num1 = input(" enter number 1 ")
num2 = input("enter number 2: ")
result = float(num1) + float(num2)
print(result)
friends = ["kevin", "hani", "arman"]
print(friends[1])
print(friends)
friends[0] = "mike"
print(friends)
lucknumbers = [1, 2, 3, 7, 9, 11, 17]
friends.extend(lucknumbers)
print(friends)
friends.append(3)
friends.insert(1, "hani")
print(friends)
friends.remove(friends[3])
print(friends)
print(friends.count("hani"))


def say_hi(name, age):
    print("hello" + name + "you are " + str(age))


say_hi("hh", 23)


def cube(num):
    result = num * num * num
    return result


print(cube(3))
is_male = True
is_tall = True
if is_male or is_tall:
    print("you are tall and man")
elif is_tall and not (is_male):
    print("you are tall but you are not man")
else:
    print("you are neither tall or man ")


def max(num1, num2, num3):
    max = num1
    if num2 > num1:
        max = num2
    elif num2 > num3:
        max = num3
    return max


print(max(1, 6, 3))

num1 = float(input("enter number 1: "))
op = input("enter operator: ")
num2 = float(input("enter number 2: "))


def calculator(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "*":
        return num1 * num2
    elif op == "-":
        return abs(num2 - num1)


print(calculator(num1, num2, op))
hani = {"hani": "hanieh", "armani": "arman", }
print(hani["hani"])
i = 1
while i <= 10:
    print("i:" + str(i))
    i = int(input("enter the i:"))
print("loop done")
secret_world = "giraffe"
guess = ""
guesslimits = 3
gueesscount = 0
outofgame = False
while guess != secret_world:
    if gueesscount < guesslimits:
        guess = input("enter your guess:")
        gueesscount += 1
    else:
        outofgame = True

if outofgame == True:
    print("you passed the limit, you lose")
else:
    print("you win")
for letter in "gira":
    print(letter)
friens = ["hani", "arman", "sadri ", "yousef"]
for friend in friens:
    print(friend)
for index in range(10):
    print(index)


def raisetopower(base, power):
    result = 1
    for power in range(power):
        result = result * base
    return result


print(raisetopower(2, 3))
grades = [[1, 2, 3], [2, 3, 4]]
for row in grades:
    for column in row:
        print(column)


def translate(phrase):
    tranlation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            tranlation = tranlation + "g"
        else:
            tranlation = tranlation + letter

    return tranlation


print(translate("Hanieh"))


def translate2(phrase):
    tranlation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                tranlation = tranlation + "G"
            else:
                tranlation = tranlation + "g"
        else:
            tranlation = tranlation + letter

    return tranlation


aa = input("enter your world for translation: ")
print(translate2(aa))
from Student import Student

student1 = Student("hanieh", "sadri", "masters", 3.72)
student2 = Student("Arman", "yousezadeh", "masters", 3.68)
print(student1.on_honor_roll())
from HaniehStudent import HaniehStudent

student3 = HaniehStudent("hanie", "sadri", "maths", 3.72, 23)
student3.on_honor_roll()
students = []
students.append(student1)
students.append(student2)
for s in students:
    if s.lastname == "sadri":
        print("welcome Hanieh")
    if s.lastname == "yousezadeh":
        print("welcome Arman ")

# multiple quiz
question_prompts = ["what is the answer of x in this equation? 2x=6 (a) 4 (b) 2  (c)3",
                    "where is the biggest country in the world? (a) Canada (B)America (c)russia"
                    ]
from Question import Question

questions = [Question(question_prompts[0], "c"), Question(question_prompts[1], "c")]


# khod payton mifahme k q list yani . ro ke mizani onja mifahme
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(score)

run_test(questions)

try:
    numberr = int(input("enter number:"))
except ZeroDivisionError:
    print("zerodividionerror")
except ValueError:
    print("invalidvalue")
#documents=open("doocument","r")
#documentsarray=documents.readlines()
#for document in documentsarray:
  #  print(document)
documents2=open("doocument","r+")
line=input("enter namr and career ")
documents2.write("\n"+line)

documents2=open("doocument","r+")
documentsarray=documents2.readlines()
for document in documentsarray:
   print(document)


