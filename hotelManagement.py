class hotel:
  weekDay=["Mon","Tue","Wed","Thur","Fri"]
  weenEnd=["Sat","Sun"]
  regularWeekDay={"x":100,"y":130,"z":195}
  regularWeekEnd={"x":120,"y":150,"z":150}
  rewardeeWeekDay={"x":90,"y":100,"z":120}
  rewardeeWeekEnd={"x":60,"y":95,"z":90}
  
  def __init__(self,data):
    self.data=data

  def compare(self):
    booking=self.data
    customerStatus=[]
    days=[]
    for i in booking:
      if i==":":
        break
      customerStatus.append(i)
    customerStatus="".join(customerStatus)

    if customerStatus=="regular":
      if self.data in hotel.weekDay:
        print(min(hotel.regularWeekDay),"is the hotel where customer gets profitted")
      else:
        print(min(hotel.regularWeekEnd),"is the hotel where customer gets profitted")
    elif customerStatus=="rewardee":
      if self.data in hotel.weekDay:
        print(min(hotel.rewardeeWeekDay),"is the hotel where customer gets profitted")
      else:
        print(min(hotel.rewardeeWeekEnd),"is the hotel where customer gets profitted")
    else:
      print("Enter valid data")

     
person1=hotel("rewardee:16Mar2010(Sun),19Mar2010(Wed),21Mar2010(Fri)")
person1.compare()
