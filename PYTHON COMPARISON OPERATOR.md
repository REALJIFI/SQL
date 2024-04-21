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

    please enter password 9087
    

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

    what is your name: tayo
    

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

    what is your test score: 25
    what is your quiz score 37
    what is your assignment score 45
    what is your exam score 76
    

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

    Did you cook rice madam yes
    Did you cook beans madam no
    

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
    what is the temperatue (in celsius): 17
    

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

    How old are you 40
    What is your annual income?  51000
    

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
# ODD number
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    if num % 2 == 1:
        print(num)
```

    1
    3
    5
    7
    9
    


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
