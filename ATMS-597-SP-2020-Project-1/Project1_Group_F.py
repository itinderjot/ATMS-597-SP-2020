class temp_array():
  """ Library to convert units of temp
  
      Methods: tempconvert
  """
  
  def __init__(self,values,units):
    """Initialisation of the class attributes

    Args:
        values (Float) : A numpy array/list denoting user-input temeperatures.
        units (Str) : Unit of the input temperatures. Can be either 'C' (Celsius),
                      'K' (Kelvin) or 'F' (Fahrenheit)
    """
    self.values=values
    self.units=units

  def tempconvert(self,TO):
    """Python function to convert temperatures interchangeably between 
    degrees Celsius, Fahrenheit, and Kelvin.

    Args:
        TO (String) : String variable denoting the unit of the output list/array.
                      Can accept 'toC' (change to Celsius), 'toK' (change to Kelvin),
                      or 'toF' (change to Fahrenheit).

    Returns:
        Values (Float) : An output list/array of temperatures in desired units.
        Units (Str) : Desired units or a prompt to let the user know that the desired
                      and input units are the same.

    """
    
    # Following block of code handles output if input unit is Celsius.
    if self.units == "C" and TO == "toC": # Celsius to Celsius
      print("Values already in deg C")
      return self
    if self.units == "C" and TO == "toK": # Celsius to Kelvin
      return temp_array([x + 273.15 for x in self.values], "K")
    if self.units == "C" and TO == "toF": # Celsius to Fahrenheit
      return temp_array([x * 9.0/5.0 + 32.0 for x in self.values], "F")
    
    # Following block of code handles output if input unit is Kelvin.
    if self.units == "K" and TO == "toC": # Kelvin to Celsius
      return temp_array([x - 273.15 for x in self.values], "C")
    if self.units == "K" and TO == "toF": # Kelvin to Fahrenheit
      return temp_array([(x - 273.15) * 9.0/5.0 + 32.0 for x in self.values], "F")
    if self.units == "K" and TO == "toK": # Kelvin to Kelvin
      print("Values already in deg K")
      return self
    
    # Following block of code handles output if input unit is Fahrenheit.
    if self.units=="F" and TO=="toC": # Fahrenheit to Celsius
      return temp_array([(x-32.0)*5.0/9.0 for x in self.values],"C")
    if self.units=="F" and TO=="toK": # Fahrenheit to Kelvin
      return temp_array([((x-32.0)*5.0/9.0) + 273.15 for x in self.values],"K")
    if self.units=="F" and TO=="toF": # Fahrenheit to Fahrenheit
      print("Values already in deg F")
      return self
