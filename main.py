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
elif is_tall and not(is_male):
    print("you are tall but you are not man")
else:
    print("you are neither tall or man ")


def max(num1,num2,num3):
    max = num1
    if num2 > num1:
        max = num2
    elif num2>num3:
        max=num3
    return max
print(max(1,6,3))

num1 =float(input("enter number 1: "))
op =input("enter operator: ")
num2 =float(input("enter number 2: "))

def calculator(num1,num2,op):
   if op=="+":
    return num1+num2
   elif o p=="*":
    return num1*num2
   elif op=="-":
       return  abs(num2-num1)
print(calculator(num1,num2,op))
hani={"hani":"hanieh","armani":"arman",}
print(hani["hani"])




