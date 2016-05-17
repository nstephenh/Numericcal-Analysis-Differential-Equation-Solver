import math


def euler(function, iterations, initialx, initialy, interval=1, divisor=","):
    currx = initialx
    curry = initialy
    i = 0
    h = interval/iterations
    while (i < iterations):
        print(i, divisor, currx, divisor, curry)
        curry += h*function(currx, curry)
        currx += h
        i += 1
    print(i, divisor, currx, divisor, curry)
    return(curry)


def quadeuler(function, iterations, initialx, initialy, interval=1, divisor=","):
    pastx = initialx
    currx = initialx
    pasty = initialy
    curry = initialy
    i = 0
    h = interval/iterations
    while (i < iterations):
        print(i, divisor, currx, divisor, curry)
        curry += h*function(currx, curry)
        currx += h
        i += 1
    print(i, divisor, currx, divisor, curry)
    return(curry)


def difeq1(x, y):
    return x/y


def difderiv(x, y):
    return x/(y*y)


def difeq2(x, y):
    return x

initx = 1
print(euler(difeq1, 20, 1, abs(initx)))
print(euler(difeq2, 20, 1, 1))