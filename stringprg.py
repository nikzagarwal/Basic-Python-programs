str="Nikhil Agarwal"
print("section1")
#1
print(str)
#2
print(str[0])
#3
print(len(str))
#4
print("Nikhil" in str)#return boolean value
#5
print("this" not in str)#return boolean value
#6
print("section2")
print(str[2:5])#not included 5
#7
print(str[:-2])
#8
print("section3")
#built in methods
print(str.upper())
#9
print(str.lower())
#10
print(str.strip())
#11
print(str.replace("i","j"))
#12
print(str.split(" "))
#13
print(str+" is good")
#14
#formatting
str2="i am {} i can vote"
age=22
print(str2.format(age))
#15
print("he is \"very\" good")
