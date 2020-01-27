class temp_array():
  """ convert units of temp
  """
  def __init__(self,values,units):
    self.values=values
    self.units=units

  def tempconvert(self,TO):

    if self.units=="C" and TO=="toC":
      print("Values already in deg C")
      return self
    if self.units=="C" and TO=="toK":
      return temp_array([x +273.15 for x in self.values],"K")
    if self.units=="C" and TO=="toF":
      return temp_array([x*9.0/5.0 + 32.0 for x in self.values],"F")
