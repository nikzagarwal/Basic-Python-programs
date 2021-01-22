# Python Strings

- Python treats single quotes the same as double quotes. Creating strings is as simple as assigning a value to a variable
- Python has no char type

**a="Nikhil"**

## section 1

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

## Section 2

### Slicing

#6

print(str[2:5])#not included 5
#7
print(str[:-2])

## Section 3

### Built in methods

#8

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

### formatting

#14

str2="i am {} i can vote"
age=22
print(str2.format(age))
#15

### escape character

print("he is \"very\" good")

