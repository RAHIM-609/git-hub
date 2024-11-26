#exercise 1
word1="hello"
word2="everyone"
word3="welcome"
print(word1+"_"+word2+"_"+word3)

#exercise 2
num1 = 10
num2 = 20
sum = num1 + num2
print(sum)

# exercise 3
biography_info = {"name" : "rahim" , "home_town" : "sharjah","age" :"20"}
print("my name is " , biography_info["name"])
print("i live in " , biography_info["home_town"])
print("my age is " , biography_info["age"])

# exercise 4
answer = input("what is the capital of france ").lower()
if answer == "paris":
    print("correct")
else:
    print("incorrect")
    
answer = input("what is the capital of germany").lower()
if answer == "berlin":
    print("correct")
else:
    print("incorrect")
    
answer = input("what is the capital of italy").lower()
if answer == "rome":
    print("correct")
else:
    print("incorrect")
    
answer = input("what is the  capital of spain").lower()
if answer == "madrid":
    print("correct")
else:
    print("incorrect")

# exercise 5
months_days = { 
               1:31,
               2:38,
               3:31,
               4:30,
               5:31,
               6:30,
               7:31,
               8:30,
               9:31,
               10:30,
               11:31,
               12:30}
months_number = int(input("enter the month number from '1-12' = "))
if 1<= months_number <=12:
    print("number of days in the month is " , months_days[months_number])
else:
    print("invalid input")

# exercise 6
correct_password = "2004"
attempt_left ="5"
while attempt_left > "0":
    password = input("enter your password = ")
    if password == correct_password:
        print("welcome")
        break
    else:
        attempt_left -= 1
        print("incorrect password, attempt left = ", attempt_left)
    if attempt_left ==0:
        print("you have been locked out")

# exercise 7
for i in range(11,13,15):
    print(i)
for i in range(12,14,16):
    print(i)
for i in range(10,20,30):
    print(i)
#exercise 8
name = ["rahim","harneet","aryan","afser","ridwan"]
search_name = input("enter the name to search: ")
if search_name in name:
    print(f"'{search_name}'name is on the list")
else:
    print(f"'{search_name}' the name is not on the list")
    
# exercise 9  
def hello():
    print("hello")
def main():
    hello()
if __name__ == "__main__":
    main()

#exercise 10
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even number"
    else:
        return f"{number} is odd number"
    
 



