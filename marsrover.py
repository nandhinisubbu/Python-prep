class rover:

  def __init__(self,upper,lower,xcoordinate,ycoordinate,startingPoint,instructions):
    self.upper=upper
    self.lower=lower
    self.xcoordinate=xcoordinate
    self.ycoordinate=ycoordinate
    self.startingPoint=startingPoint
    self.instructions=instructions
    

  

  def turnLeft(self,startingPoint):
    if startingPoint=="N":
      startingPoint="W"
    elif startingPoint=="W":
      startingPoint="S"
    elif startingPoint=="S":
      startingPoint="E"
    else:
      startingPoint=="N"
    return startingPoint

  def turnRight(self,startingPoint):
    if startingPoint=="N":
      startingPoint="E"
    elif startingPoint=="S":
      startingPoint="W"
    elif startingPoint=="E":
      startingPoint="S"
    else:
      startingPoint=="N"
    return startingPoint

  def moveForward(self,startingPoint):
    if startingPoint=="N":
      self.xcoordinate = self.xcoordinate
      self.ycoordinate +=1
    elif startingPoint=="S":
      self.xcoordinate = self.xcoordinate
      self.ycoordinate -=1
    elif startingPoint=="E":
      self.xcoordinate +=1
      self.ycoordinate=self.ycoordinate
    else:
      self.xcoordinate -=1
      self.ycoordinate=self.ycoordinate
    return self.xcoordinate,self.ycoordinate


  def seriesinstruction(self):
    startingPoint=self.startingPoint
    movingPoint=self.xcoordinate,self.ycoordinate

    for instruction in self.instructions:
      if instruction=='L':
        startingPoint=self.turnLeft(startingPoint)
      elif instruction=="R":
        startingPoint=self.turnRight(startingPoint)
      elif instruction=="M":
        movingPoint=self.moveForward(startingPoint)
      else:
        print("Enter the valid data ")
    return movingPoint, startingPoint

  def plateau(self):
    if self.xcoordinate<=self.lower and self.ycoordinate<=self.upper:
      out=self.seriesinstruction()
      return out
    else:
      print("Invalid data")

rover1=rover(5,5,1,2,"N",'LMLMLMLMM')
rover2=rover(5,5,3,3,'East','MMRMMRMRRM')
print(rover1.plateau())
print(rover2.plateau())
