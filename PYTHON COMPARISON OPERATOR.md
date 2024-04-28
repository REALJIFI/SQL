```python
password = 1234
```


```python
user_pass = int(input("please enter password"))

if user_pass == password:
    print("correct")
else:
    print("wrong")
```

    please enter password 763542
    

    wrong
    


```python
name = input("what is your name:")

if name == "GEORGE":
    print(f"i know you , {name}")
elif name == "Ben":
    print("how did you get here")
elif name == "Cece":
    print("my gee is here")
else:
    print("i no know your papa")
```

    what is your name: queenesther
    

    i no know your papa
    


```python
Evm232 = int(input("what is your test score:"))
Evm554 = int(input("what is your quiz score"))
Evm613 = int(input("what is your assignment score"))
Exam = int(input("what is your exam score"))
total_score = Evm232 + Evm554 + Evm613 + Exam 
if total_score >= 70:
    print("A")
elif  total_score >= 60:
    print("B")
elif  total_score >= 50:
    print("C")
elif  total_score >= 40:
    print("D")
else:
    print("F")
```

    what is your test score: 65
    what is your quiz score 69
    what is your assignment score 35
    what is your exam score 45
    

    A
    


```python
# AND & OR
```


```python
# N ORDER TO DRIVE, YOU HAVE TO BE 18 YEARS AND ABOVE
Dlicence = input("do you have a licence:")
Age = int(input("how old are you:"))

if Age >= 18 and Dlicence == "yes":
    print("welcome, you are eligible to drive")
else:
    print("you are not eligible to drive")
```

    do you have a licence: yes
    how old are you: 21
    

    welcome, you are eligible to drive
    


```python
# BOB RICE OR BEANS

Rice = input("Did you cook rice madam")
Beans = input("Did you cook beans madam")
if Rice == "yes" or Beans == "yes":
    print("buy")
else:
    print("I no dey buy")
```

    Did you cook rice madam no
    Did you cook beans madam yes
    

    buy
    


```python
### IF/ELIF/ELSE AND/OR statement 
```


```python
weather = input("what is the weather like (cold, warm, freezing):")
temperature = int(input("what is the temperatue (in celsius):"))

# processing weather/temperature to recommend activities
if weather.lower() == "warm" and temperature >= 40:
   activity = "it is safe to drive/work"
elif weather.lower() == "cold" and temperature < 30:
   activity = "it is a nice day for walk/jog"
elif weather.lower() == "freezing" or weather.lower() == "cold":
    activity = "it is too cold to drive/walk"
else:
    activity = "udo di na beanyi"
# output
print(activity)
```

    what is the weather like (cold, warm, freezing): warm
    what is the temperatue (in celsius): 35
    

    udo di na beanyi
    


```python
### FINANCIAL ADVICE BASED ON AGE
```


```python
# INPUT age and annual income
Age = int(input("How old are you",))
income = float(input("What is your annual income? "))

if Age < 30 and income < 50000:
    financial_advice = "it is the right time to start saving money"
elif Age < 30 and income >= 50000:
    financial_advice = "they have to start investing"
elif Age >= 30 and income < 50000:
    financial_advice = "creating a budget plan could help manage your finance"
elif Age >= 30 and income >= 50000:
    financial_advice = "start planning for your retirement"
elif income > 100000 or Age > 65:
    financial_advice = "with your income and age, speaking to a financial advicer is important"
else:
    financial_advice == "seeking a personal financial adviser will be the best action"
print(financial_advice)
```

    How old are you 57
    What is your annual income?  100000
    

    start planning for your retirement
    


```python
# FOR LOOP
```


```python
name = "George"
for g in range(4): 
    print(name)
```

    George
    George
    George
    George
    


```python
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    


```python
# EVEN Number
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print(f"{num} is an odd number")
```

    1 is an odd number
    2
    3 is an odd number
    4
    5 is an odd number
    6
    7 is an odd number
    8
    9 is an odd number
    10
    


```python
#WHILE LOOP
```


```python
password = input("what is your password: ")
while password == "hallyday":
    print("welcome to school")
    password = input("wrong password")
```

    what is your password:  hallyday
    

    welcome to school
    

    wrong password hallyday
    

    welcome to school
    

    wrong password youtube
    


```python
#BREAKE,CONTINUE AND PASS
```


```python
name = "george"
for e in name:
    print(e)
```

    g
    e
    o
    r
    g
    e
    


```python
name = "george"
for e in name:
    if e == "r":
        break
    print(e)
```

    g
    e
    o
    


```python
name = "george"
for e in name:
    if e == "r":
        continue
    print(e)
```

    g
    e
    o
    g
    e
    


```python
name = "george"
for e in name:
    if e == "r":
        pass
    print(e)
```

    g
    e
    o
    r
    g
    e
    


```python
# 3 TRIALS FOR PASSWORD VERIFICATION
for p in range(3):
    password = input("what is your password: ")
    if password == "selfworth":
        print("login successful")
        break
    print("wrong password")

```

    what is your password:  machine
    

    wrong password
    

    what is your password:  goosebump
    

    wrong password
    

    what is your password:  selfworth
    

    login successful
    

# FOR LOOP


```python
# password Verification
correct_password = "George"
max_attempt = 5
for attempt in range(max_attempt):
            password_try = input(f"this is attempt {attempt + 1} of {max_attempt} attempt: ")
        
            if password_try == correct_password:
                print("access granted")
                break #Stop the loop if password is correct
            else:
                print("Incorrect password")
                
                if attempt < max_attempt - 1:
                 print("Please try again.")
                continue #continue to the next attempt
else:
    print("you have reached your limit")
```

    this is attempt 1 of 5 attempt:  George
    

    access granted
    


```python
# FUNCTION

```


```python
def name():
    birth_name = input("what is your name:")
             
 
       
```


```python
name()
```

    what is your name: kenedy
    

     welcome kenedy.
    


```python
def password():
        # password Verification
    correct_password = "George"
    max_attempt = 5
    for attempt in range(max_attempt):
                password_try = input(f"this is attempt {attempt + 1} of {max_attempt} attempt: ")
            
                if password_try == correct_password:
                    print("access granted")
                    break #Stop the loop if password is correct
                else:
                    print("Incorrect password")
                    
                    if attempt < max_attempt - 1:
                     print("Please try again.")
                    continue #continue to the next attempt
    else:
        print("you have reached your limit")
```


```python
password()
```

    this is attempt 1 of 5 attempt:  GOOSE
    

    Incorrect password
    Please try again.
    

    this is attempt 2 of 5 attempt:  George
    

    access granted
    


```python
def check_loan_status():
    min_credit_score = 800
    min_income = 3000  # per annum
    max_DTI = 0.4  # Debt to income ratio = 40%
    min_down_payment = 0.2  # 20%
    valid_employment_statuses = {'employed', 'self-employed', 'not employed'}
    min_length_of_employment = 2

    # Get user input
    credit_score = int(input("What is your credit score: "))
    income = float(input("What is your current income: "))
    loan_amount = float(input("How much loan do you want: "))
    down_payment = float(input("What is your down payment: "))
    employment_status = input("Enter your employment status (employed, self-employed, not employed): ").lower()
    length_of_employment = int(input("How long have you worked in your current job (in years): "))

    # Check user input against minimum criteria
    if credit_score < min_credit_score or income < min_income:
        status = "Loan Denied: Credit score or minimum income is too low"
    elif employment_status not in valid_employment_statuses:
        status = "Loan Denied: Employment status is not eligible"
    elif loan_amount > income * max_DTI:
        status = "Loan Denied: Debt to income ratio not supported"
    elif down_payment < loan_amount * min_down_payment:
        status = "Loan Denied: Down payment is too low"
    elif length_of_employment < min_length_of_employment:
        status = "Loan Denied: Years of current employment is too low"
    else:
        status = "Loan Approved"

    return status
```


```python
check_loan_status()
```

    What is your credit score:  6665
    What is your current income:  788
    How much loan do you want:  900
    What is your down payment:  4888
    Enter your employment status (employed, self-employed, not employed):  employed
    How long have you worked in your current job (in years):  2
    




    'Loan Denied: Credit score or minimum income is too low'



FILTER,MAP AND LAMBDA


```python
#extract the even number from the list below
number = list(range(21))

def even_number(x):
    return x % 2 == 0
#filter (function, list,(iterable))
even_num = filter(even_number, number)

#convert output from filter function into a list
list(even_num)
```




    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




```python
words = ["keys","mouth","truth","dare","civil"]
#create a function to know if a word is palindrome
def palindrome(words):
    return words[::-1]
```


```python
palindrome(words)
```




    ['civil', 'dare', 'truth', 'mouth', 'keys']




```python
name = "George"
name[::-1]
```




    'egroeG'




```python

```


```python

```
