from datetime import datetime
from utils import log_transaction

def deposit(accounts, account_number):
    amount = float(input("Enter amount to deposit: "))
    accounts[account_number]['balance'] += amount
    log_transaction(account_number, 'Deposit', amount)
    print(f"Deposit successful! Current balance: {accounts[account_number]['balance']}")

def withdraw(accounts, account_number):
    amount = float(input("Enter amount to withdraw: "))
    if amount > accounts[account_number]['balance']:
        print("Insufficient balance.")
    else:
        accounts[account_number]['balance'] -= amount
        log_transaction(account_number, 'Withdrawal', amount)
        print(f"Withdrawal successful! Current balance: {accounts[account_number]['balance']}")