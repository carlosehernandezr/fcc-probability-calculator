import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **args):
    self.contents = []
    for k,v in list(args.items()):
      for v in range(v):
        self.contents.append(k)
    
  def draw(self,balls):
    
    to_draw =  []

    if balls>len(self.contents):
      return self.contents

    for ball in range(balls):
      r = random.choice(self.contents)
      #print(r)
      to_draw.append(r)      
      self.contents.remove(r)

    #print(to_draw)
    return to_draw
        
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  n = 0
  
  for experiment in range(num_experiments):
    mHat = copy.deepcopy(hat)
    actual = {}
    draw = mHat.draw(num_balls_drawn)
    
    actual={ball:draw.count(ball) for ball in set(draw)}
    
    answer=True
    for ball in expected_balls:
      if ball not in actual or actual[ball]<expected_balls[ball]:
        answer=False
        break
    if answer:
      n+=1
    
  return n/num_experiments