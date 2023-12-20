import random
import time
class Bank:

  acc_details = {'user_details':{'acc_no' : 0,'balance': 0 , 'password': '', 'name' : '', 'gender' : 'na', 'is_active':False}}
  

  def __init__(self):
    self.menu()

  
  def create_account(self):

    is_active  = False
    try:

      name = str(input("Eneter Your Name:- "))
      gender = str(input("Enter your gender:- "))
      min_bal = int(input("Enter recquired minimum balance :- "))
      password = input("Enter your password:- ")

      if len(name) > 3:
        if gender.lower() == 'male':
          print(f"Welcomr Sir {name}")
        
        if gender.lower() == 'female':
          print(f"Welcome Mam {name}")
      else:
        print("Not a valid name...\n")

      if min_bal >= 500:
        print("Please Wait While Genrating Your Account Number ..\n\n")
        time.sleep(2)
        acc_num = random.randint(123456, 987654)
        print(f"Your account number has been genrated {acc_num}\n")
        time.sleep(1)
        print("! Congrats! your account has been activated !")
        print("\n\n")
        time.sleep(2)
        is_active = True

        self.acc_details['user_details']['name'] = name
        self.acc_details['user_details']['gender'] = gender
        self.acc_details['user_details']['is_active'] = is_active
        self.acc_details['user_details']['password'] = password
        self.acc_details['user_details']['balance'] = min_bal
        self.acc_details['user_details']['acc_no'] = acc_num

        print("Your details updated\n\n")
      else:
        print("Minimum Balance recquired...")
    except:
      print("An error occured..")

  
  def login(self, acc_no, password):
    is_valid = False
    try:
      user_data = self.acc_details.get('user_details')
      if user_data['acc_no'] == int(acc_no) and user_data['password'] == str(password):
        is_valid = True
        print(f"Welcomr {user_data['name']}")
      else:
        print("Invalid user...")

    except:
      print("An error occured..")
    
    return is_valid
  
  
  def deposit(self):
    amount = int(input("Enter amount to deposit: -"))
    if amount > 0:
      self.acc_details['user_details']['balance'] = self.acc_details['user_details']['balance'] + amount
      print(f"Amount has been deposited\nAvilable balance {self.avilabel_balance()}")
    else:
      print("amount should be greater than 0 ")
    
  
  def avilabel_balance(self):
    try:
      print(f"Avilabel Balance :- {self.acc_details['user_details']['balance']}")
    except:
      print("an error occured..")
    return self.acc_details['user_details']['balance']
  
  
  def withdraw(self):
    try:
      amount = int(input("Enter amount to withdraw:- "))
      
      if amount <= self.acc_details['user_details']['balance']:
        print(f"{amount} amount has been debited from your account")
        self.acc_details['user_details']['balance'] = self.acc_details['user_details']['balance'] - amount

        print(f'Avilabel amount {self.avilabel_balance()}')
      else:
        print("insufficient balance...")
    
    except Exception as e:
      # print("Something went wrong...")
      print(e)

  
  def menu(self):
    choice = int(input('''\n\n\t\t\t!! Welcome to the Mini Bank !!\n
                       Please Choose option below
                       Press [1] Register Your Self
                       Press [2] Log in
                       Presss [3] to exit
                       '''))
    if choice == 1:
      self.create_account()
      self.menu()
    
    elif choice == 2:
      account_number = input("Enter Your Account Number:- ")
      password = input("Enter Your Password:- ")

      check = self.login(account_number, password)
      if check:
        
        choice = int(input('''\n\n\t\t\tPlease Choose option below
                           Press [1] to deposit
                           Press[2] check balance
                           Press [3] withdraw 
                           Press [4] Exit '''))
        if choice == 1:
          self.deposit()
          self.menu()
        elif choice == 2:
          self.avilabel_balance()
          self.menu()
        elif choice == 3:
          self.withdraw()
          self.menu()
        else:
          exit()
    else:
      print("Thankyou for banking...")
      exit()


obj = Bank()