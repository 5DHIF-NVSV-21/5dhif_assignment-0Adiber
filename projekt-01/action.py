import random
from results import Base, Quote, Cute

options: dict = {
    "MOTIVATE": 1,
    "REALITY": 2,
    "CUTE": 3,
    "EXIT": 9
}

class Action(object):
  def __init__(self, motivation, demotivation, cute):
    self.motivation = list(Quote(**m) for m in motivation)
    self.demotivation = list(Quote(**d) for d in demotivation)
    self.cute = list(Cute(**c) for c in cute)

  def getChoice(self, choice: int) -> Base:
    if choice == options["MOTIVATE"]:
      return random.choice(self.motivation)
    elif choice == options["REALITY"]:
      return random.choice(self.demotivation)
    elif choice == options["CUTE"]:
      return random.choice(self.cute)
    else:
      return None