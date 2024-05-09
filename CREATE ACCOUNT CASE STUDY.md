```python
## Case Study 1 : Basic Bank Account Manager
# Objective:
# Create a simplified banking system using Python functions to handle operations such as creating a bank account, depositing money, and withdrawing money.

# Task
# Develop a basic bank account management system that allows users to:

# Create a new bank account with an initial deposit.
# Deposit money into their account.
# Withdraw money if sufficient funds are available.
# Details:

# Use a dictionary to store account information.
# Each account can be represented as a dictionary with keys like name and balance.
```


```python
accounts = {}
def create_account(account_id, name, initial_amount = 0):
    if account_id not in accounts:
        accounts[account_id] = {'name': name, 'balance': initial_amount}
    return "account created successfully."
    return "account already exists,"
def deposit (account_id, amount):
    if account_id is accounts:
        accounts[account_id]['balance'] += amount
        return "deposit successful."
    else:
        return "account not found."
def withdraw(account_id, amount):
    if account_id in accounts:
        if accounts[account_id]['balance'] >= amount:
           accounts[account_id]['balance'] -= amount
           return "withdrawal successful."
        else:
           return "insufficient fund"
    else:
           return "account not found"

print(create_account(1, "George wey", 200))
print(deposit(1, 500))
print(withdraw(1, 300))
print(withdraw(1, 1000))
```

    account created successfully.
    account not found.
    insufficient fund
    insufficient fund
    


```python
# Define accounts as a global dictionary
accounts = {}

# Function to create an account
def create_account(account_id, name, initial_amount=0):
    global accounts  # Use the global accounts variable
    
    if account_id not in accounts:
        accounts[account_id] = {'name': name, 'balance': initial_amount}
        return "Account created successfully."
    else:
        return "Account already exists."

# Function to deposit into an account
def deposit(account_id, amount):
    global accounts  # Use the global accounts variable
    
    if account_id in accounts:
        accounts[account_id]['balance'] += amount
        return "Deposit successful."
    else:
        return "Account not found."

# Function to withdraw from an account
def withdraw(account_id, amount):
    global accounts  # Use the global accounts variable
    
    if account_id in accounts:
        if accounts[account_id]['balance'] >= amount:
            accounts[account_id]['balance'] -= amount
            return "Withdrawal successful."
        else:
            return "Insufficient funds."
    else:
        return "Account not found."

# Example usage
print(create_account(1, "George wey", 200))
print(deposit(1, 200))
print(withdraw(1, 300))
print(withdraw(1, 1000))
```

    Account created successfully.
    Deposit successful.
    Withdrawal successful.
    Insufficient funds.
    


```python

```
