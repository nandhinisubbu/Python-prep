class ipod:
   def __init__(self,country,noofitems,prize):
     self.country=country
     self.noofitems=noofitems
     self.prize=prize
     
   def calculate(self):
     if self.country=="Brazil" and (self.noofitems>=10 and self.noofitems%10==0):
       if self.noofitems<=100:
         costInBrazil=self.noofitems*self.prize
         remainingInBrazil=100-self.noofitems
         remainingInArgentina=100
         print(costInBrazil,":",remainingInBrazil,":",remainingInArgentina)      
       elif self.noofitems<=200:
         ipodInBrazil=100
         ipodInArgentina=self.noofitems-ipodInBrazil
         costOfIpodInBrazil=100*100
         costOfIpodInArgentina=(ipodInArgentina*50)+((ipodInArgentina//10)*400)
         totCostOfIpod=costOfIpodInArgentina+costOfIpodInBrazil
         remainingInBrazil=0
         remainingInArgentina=100-ipodInArgentina
         print(totCostOfIpod,":",remainingInBrazil,":",remainingInArgentina)
       else:
         print("out Of stock")

     elif self.country=="Argentina" and (self.noofitems>=10 and self.noofitems%10==0):
       if self.noofitems<=100:
         costInArgentina=self.noofitems*self.prize
         remainingInArgentina=100-self.noofitems
         remainingInBrazil=100
         print(costInArgentina,":",remainingInBrazil,":",remainingInArgentina)
       elif self.noofitems<=200:
         ipodInArgentina=100
         ipodInBrazil=self.noofitems-ipodInArgentina
         costOfIpodInArgentina=50*100
         costOfIpodInBrazil=(ipodInBrazil*100)+((ipodInBrazil//10)*400)
         totCostOfIpod=costOfIpodInArgentina+costOfIpodInBrazil
         remainingInArgentina=0
         remainingInBrazil=100-ipodInBrazil
         print(totCostOfIpod,":",remainingInBrazil,":",remainingInArgentina)
       else:
         print("out Of stock")

pod1=ipod("Argentina",250,50)
pod1.calculate()
