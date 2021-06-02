def wallis(n):
    pi = 2
    for i in range(1, n):
        left = (2. * i)/(2. * i - 1.)
        right = (2. * i)/(2. * i + 1.)
        pi = pi * left * right
    return pi





import random 
def monte_carlo(n):

  circle_point=1
  square_point=0
  while circle_point<=square_point:
     x=random.random()
     y=random.random()
     distance=mat.sqrt((x**2)+(y**2))
     if distance<1:
         square_point +=1
     circle_point+=1
  pi=4*(square_point/n)
  return pi



