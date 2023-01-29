def binaryToDecimal(binNum):
    i = 0
    ans = 0
    exp = 12
    frac = 0
    expAns = 0
    fracAns = 0
    while i < len(binNum) :
        if i <= 11:
            exp -= 1
            if binNum[i] == '1':
                expAns += pow(2, exp)
                i += 1
                continue      
        if i >= 12:
            frac += 1
            if binNum[i] == '1':
                fracAns += pow(0.5, frac)
                i += 1
                continue
        i += 1
    ans = (pow(2, (expAns - 1023)) * (1 + fracAns))
    return ans

def absoluteError(num1, num2):
    return abs(num1 - num2)

def relativeError(num1, num2):
    return absoluteError(num1, num2) / num1

def babylonainMethod(num):
    error = .0001
    numIterations = -1
    diff = 1
    k = 1
    equation = num
    while(diff >= error):
        currVariable = equation
        equation +=(pow(-1, k) * (pow(1, k) / pow(k, 3)))
        diff = abs(currVariable - equation)
        numIterations += 1
        k += 1
    return numIterations

def bisectionMethod(left, right, function):
    x = left
    initLeft = eval(function)
    x = right
    initRight = eval(function)

    if initLeft * initRight >= 0:
        print("Error")
        return
    error = .0001
    diff = right - left
    maxIterations = 50
    numIterations = 0
    while(diff >= error and numIterations <= maxIterations):
        numIterations  += 1

        midpoint = (left + right) / 2
        x = midpoint
        evalMid = eval(function)
        if evalMid == 0.0:
            break
        x = left
        evalLeft = eval(function)
        firstCond = evalLeft < 0 and evalMid > 0
        secondCond = evalLeft > 0 and evalMid < 0

        if firstCond or secondCond:
            right = midpoint
        else:
            left = midpoint
        diff = abs(right - left)
    return numIterations

def newtonMethod(initValue):
    prev = initValue
    error = .0001
    maxIterations = 100
    i = 1
    while(i <= maxIterations):
        i += 1
        if (3*(pow(prev, 2)) + (8*prev)) != 0:
            next = prev - ((pow(prev, 3) + 4*(pow(prev, 2) - 10)) / (3*(pow(prev, 2)) + (8*prev)))
            if abs(next - prev) < error:
                return i
            prev = next
        else:
            print("Error: Derivative is zero")
    else:
        print("Error: Max iterations reached")        



ans1 = "{:.5f}".format(binaryToDecimal('010000000111111010111001'))
print(ans1)
print("\n")
print("{:.3f}".format(binaryToDecimal('010000000111111010111001')))
print("\n")
ans3 = round((binaryToDecimal('010000000111111010111001')), 3)
print(ans3)
print("\n")
print(absoluteError(float(ans1), ans3))
print(relativeError(float(ans1), ans3))
print("\n")
print(babylonainMethod(1))
print("\n")
print(bisectionMethod(-4, 7, "x**3 + (4*(x**2)) - 10"))
print(newtonMethod(7))






