def binaryToDecimal(binNum):
    i = 0
    ans = 0
    exp = 11
    frac = 1
    while i < len(binNum) :
        if binNum[0] == '1':
            ans *= -1
            i += 1
        else:
            i += 1
        if i < 11:
            if binNum[i] == '1':
                ans += pow(2, exp)
                exp -= 1
                i += 1      
        if i >= 12:
            if binNum[i] == '1':
                ans += pow(0.5, frac)
                i += 1
                frac += 1
    return ans

def absoluteError(num1, num2):
    return abs(num1 - num2)

def relativeError(num1, num2):
    return absoluteError(num1, num2) / num1

def babylonainMethod(num):
    error = .0001
    numIterations = 0
    diff = 1
    k = 1
    equation = num
    while(diff >= error):
        currVariable = equation
        equation +=(pow(-1, k) * (pow(1, k) / pow(k, 3)))
        diff = currVariable - equation
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
    error = .001
    diff = right - left
    maxIterations = 50
    numIterations = 0
    while(diff >= error and numIterations <= maxIterations):
        numIterations  += 1

        midpoint = (left + right) / 2
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
    error = .001
    maxIterations = 100
    i = 1
    while(i <= maxIterations):
        if (3*(pow(prev, 3)) + (8*prev)) != 0:
            next = prev - ((pow(prev, 3) + 4*(pow(prev, 2) - 10)) / (3*(pow(prev, 3)) + (8*prev)))
            if abs(next - prev) < error:
                return maxIterations
            i += 1
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






