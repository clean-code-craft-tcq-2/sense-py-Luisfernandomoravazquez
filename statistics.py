
def calculateStats(numbers):
  fields = { "avg":float("NaN"), "max":float("NaN"), "min":float("NaN") }

  if(len(numbers) > 0):  
    fields["avg"] = sum(numbers)/len(numbers)
    fields["max"] = max(numbers)
    fields["min"] = min(numbers)

  return fields

class EmailAlert():
  emailSent = False
  def activate(self):
    self.emailSent = True

class LEDAlert():
  ledGlows = False
  def activate(self):
    self.ledGlows = True

class StatsAlerter:
  def __init__(self,maxValue,alerters):
    self.maxValue = maxValue
    self.alerters = alerters

  def checkAndAlert(self, numbers):
    if(max(numbers) > self.maxValue):
      for alerter in self.alerters:
        alerter.activate()