def wallis(n):
    pi = 2
    for i in range(1, n):
        left = (2. * i)/(2. * i - 1.)
        right = (2. * i)/(2. * i + 1.)
        pi = pi * left * right
    return pi






def monte_carlo(n):
import random
  i=1
  inspoint=0
  while i<=n:
      x=random.random()
      y=random.random()
      distance=math.sqrt((x**2)+(y**2))
      if distance<1:
          inspoint+=1
      i+=1
      val=4*(inspoint/n)
      return val



