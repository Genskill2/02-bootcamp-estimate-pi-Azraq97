def wallis(n):
    pi = 2
    for i in range(1, n):
        left = (2. * i)/(2. * i - 1.)
        right = (2. * i)/(2. * i + 1.)
        pi = pi * left * right
    return pi
print(wallis(10))



def monte_carlo(n):
    import random

    INTERVAL = 1000

    circle_points = 0
    square_points = 0


    for i in range(INTERVAL ** 2):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        origin_dist = rand_x ** 2 + rand_y ** 2


        if origin_dist <= 1:
            circle_points += 1

        square_points += 1


        pi = 4 * circle_points / square_points
    return pi
print(monte_carlo(10))



