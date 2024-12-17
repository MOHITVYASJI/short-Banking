class bankaccount:
    def __init__(self,bal,acc):
        self.Balance = bal
        self.Account = acc
    #Dedit Method
    def debit(self,account):
        self.Balance -= account
        print("Rupee ",account," Was diducted" )
        print("Total Account Balance is : ",self.Balance)
    def credit(self,account):
        self.Balance += account
        print("Rupee ", account," Was Creadit")
        print("Total Account Balance is : ",self.Balance)
    def git_balance(self):
        return self.Balance
    
x=int(input("Enter the Ammount => "))
y=int(input("Enter the ACcount Number => "))


acc1=bankaccount(x,y)
acc1.debit(1000)
acc1.credit(500)
acc1.debit(10000)
acc1.credit(45000)