import hashlib
from utils import write_account, read_accounts

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_account():
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter your initial deposit: "))
    account_number = str(100000 + len(read_accounts()))  # Simple account number generation
    password = hash_password(input("Enter a password: "))
    
    write_account(account_number, name, password, initial_deposit)
    print(f"Your account number: {account_number} (Save this for login)")
    print("Account created successfully!")

def login(accounts):
    account_number = input("Enter your account number: ")
    password = hash_password(input("Enter your password: "))
    
    if account_number in accounts:
        # Debugging output
        print(f"Stored password: {accounts[account_number]['password']}")
        print(f"Entered password: {password}")
        
        if accounts[account_number]['password'] == password:
            print("Login successful!")
            return account_number
    print("Invalid account number or password.")
    return None