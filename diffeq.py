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

def rk4(function, iterations, initialx, initialy, interval=1, divisor=","):
    currx = initialx
    curry = initialy
    i = 0
    h = interval/iterations
    while (i < iterations):
        print(i, divisor, currx, divisor, curry)
        m1 = function(currx, curry)
        m2 = function(currx+(h/2),curry+(h*m1/2))
        m3 = function(currx+(h/2), curry+(h*m2/2))
        m4 = function((currx+h), curry+(h*m3))
        curry += (h/6)*(m1+2*m2+2*m3+m4)
        currx += h
        i += 1
    print(i, divisor, currx, divisor, curry)
    return(curry)

def quadeuler(function, deriv,  iterations, initialx, initialy, interval=1, divisor=","):
    pastx = initialx
    currx = initialx
    pasty = initialy
    curry = initialy
    i = 0
    h = interval/iterations
    while (i < iterations):
        print(i, divisor, currx, divisor, curry)
        curry += h*function(currx, curry) + (h*h/2)*difderiv(currx, curry)
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
#print(euler(difeq2, 20, 1, 1))
print(quadeuler(difeq1, difderiv, 20, 1, 1))
print(rk4(difeq1, 20, 1, abs(initx)))
