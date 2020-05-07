class NumberCalculation():
  def __init__(self,number1,number2):
    self.num1=number1
    self.num2=number2
  def CompeteNumber(self):
    if self.num1>self.num2:
      print(str(self.num1)+">"+str(self.num2))
    elif self.num1<self.num2:
      print(str(self.num)+"<"+str(self.num2))
    elif self.num1==self.num2:
     print(str(self.num1)+"="+str(self.num2))
    else:
      print ("錯誤") 
  def AddNumber(self):
    print(str(self.num1)+"+"+str(self.num2)+"="+str(self.num1+self.num2))
  def PresentNumber(self):
    print("number1:"+str(self.num1)+",number2:"+str(self.num2))
a=int(input("請輸入一個數字:"))
b=int(input("請輸入一個數字:"))
NumGroup1=NumberCalculation(a,b)
NumGroup1.CompeteNumber()
NumGroup1.AddNumber()
NumGroup1.PresentNumber()
