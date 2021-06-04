class account:
 def __init__(self,name,phone,loan_limit):
    self.name=name
    self.phone=phone
    self.balance=0
    self.loan_limit=loan_limit
    self.loan=0
 def deposit(self,amount):
       if amount<=0:
          return f"You cannoy deposit negative amount" 
       else:
           self.balance+=amount
       return f"Hi {self.name} you have to deposited {amount} your new balance is{self.balance}"
      
 def withdrow(self,amount):
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
     
   
