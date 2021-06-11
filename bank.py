  
from datetime import datetime
class Account:
   def __init__(self,name,phone,loan_limit):
    self.name=name
    self.phone=phone
    self.balance=0
    self.loan_limit=loan_limit
    self.loan=0
    self.statement=[]
   def deposit(self,amount):
      try:
            5/amount
      except TypeError:
            print  ("cant divide by string")        
      if amount <  0:
         return 'please input a positive amount'
       
      else :
         self.balance+=amount
         now=datetime.now() 
      transaction={
             "amount":amount,
             "time":now,
             "narration":"you haave deposited"}
      self.statement.append(transaction)
      return f'you have deposited  {amount} and your balance is {self.balance}'          
   def get_statement(self):
      for  transaction in self.statement:
         narration =transaction ["narration"]
         amount = transaction["amount"]
         balance=transaction["balance"]
         time=transaction["time"]
         date=time.strftime("%d/%m/%y")
         print(f"{date} {narration} {balance} {amount}")
     
               
   def withdrow(self,amount):
      try:
            5/amount
      except TypeError:
             print ("cant divide by string")          
          
      if amount<0:
       return f"Dear {self.name} You can't borrow negative amount"
      elif self.balance<amount:
       return f"Dear {self.name} You have less balance."
      else:
       self.balance-=amount      
       return f"Dear {self.name}, You have withdrawn {amount}, Your balance is {self.balance}"
   def  show_balance(self):
     return self.balance
   def borrow(self,amount):
      if amount >=self. loan_limit:  
       return f"dear{self. name},the amount you want to withdrow is aroud to withdrow"
      elif self.loan>0:
       return f"dear{self.name}you have not paid your loan" 
      else:
          self.loan+=1
          self.balance+=amount
      return f"Dear {self.name}, You have borrowed {amount} your new balance is{self.balance}"  
   def repay(self,amount):
       try:
             5/amount
       except TypeError:
               print("cant divide by string") 
                       
       if amount > 0:
                 return f"Dear {self.name} your loan is not valid"
       elif amount>self.loan:
            self.loan-=amount
            return f"Dear {self.name} your loan has been decreased {self.loan}"
       else:
            diff=amount-self.loan
            self.laon=0
            self.deposit(diff)
            self.balance+=amount
            now=datetime.now()
            transaction={
               "amount":amount,
               "time":now,
               "narration":"you have repaid"
               
            } 
            self.statement.append(transaction)
            return f"Dear {self.name} your loan is cleared"   
   def transfer(self,account,amount):
      try:
            3/amount
      except TypeError:
            print("please put number") 
      fee=amount*0.05      
      if amount<0:
         return "Please put a positive amount"  
      elif  amount+fee>self.balance:
         return f"You have less money on your account. you need {amount+fee} to complete the transaction" 
      else:
         self.balance-amount-fee
         account.deposit(amount)
         return f"You have sent {amount}  to {account.name} your balance is {self.balance} and you have been charged {fee}"                   
            
class Mobilemoney(Account):
   def __init__(self,name,phone,loan_limit,service_provider):
      Account.__init__(name,phone,loan_limit)
      self.service_provide=service_provider
      self.limit=200000
   def buy_airtime(self,amount):
       try:
            5/amount  
       except TypeError:
            print("Cant divide a string")    
       if amount<0:
          return 'you cant borrow negative airtime'  
       elif amount>self.balance:
          return 'you dont have enough balance to buy airtime'
       else:
          self.balance-=amount 
          return f'You have bought {amount} airtime your balance is now {self.balance}' 
   
          
                   
     
   

                 
     
   
