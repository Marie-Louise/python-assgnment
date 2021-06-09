  
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
      if amount >  0:
          self.balance+=amount
          now=datetime.now() 
          transaction={
             "amount":amount,
             "time":now,
             "narration":"you haave deposited"
         }
          self. statement.append(transaction)
          return self.show_balance
       
      else :
         return  f"Dear {self.name} yor deposit is not enough"        
           
   def get_statement(self):
      for  transaction in self.transactions:
         narration =transaction ["narration"]
         amount = transaction["amount"]
         balance=transaction["balance"]
         time=transaction["time"]
         date=time.strftime("%d/%m/%y")
         print(f"{date}:{narration}  {amount}")
         
         return 
        
               
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
   def repay(self,amount):
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
            
                 
     
   
