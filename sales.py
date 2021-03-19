class sales:
  taxLessProduct=['book','food','medical']
  basictax=0.1
  importtax=0.05

  def __init__(self,quantity,product,rate,state):
    self.quantity=quantity
    self.product=product
    self.rate=rate
    self.state=state
    
  def calculate(self):
    if self.product in sales.taxLessProduct and self.state=="imported":
      costWithImportTax=round((self.quantity*(self.rate+sales.importtax)),2)
      print(self.quantity,self.product,costWithImportTax)
      
    elif self.product in sales.taxLessProduct and self.state=="local":
      costWithoutTax=round((self.quantity*self.rate),2)
      print(self.quantity,self.product,costWithoutTax)
      
    elif self.product not in sales.taxLessProduct and self.state=="imported":
      costWithBasicImportTax=round((self.quantity*(self.rate+sales.basictax+sales.importtax)),2)
      print(self.quantity,self.product,costWithBasicImportTax)
      
    elif self.product not in sales.taxLessProduct and self.state=="local":
      costWithBasicTax=round((self.quantity*(self.rate+sales.basictax)),2)
      print(self.quantity,self.product,costWithBasicTax)
    else:
      return

order=sales(1,"book",0.85,"local")
order.calculate()
