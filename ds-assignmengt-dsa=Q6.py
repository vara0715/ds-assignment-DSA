def operatorValidater(x):
 
    if x in ["+","-","/","*"]:
        return True
 
    return False
 

def postToPre():
    expression = input('Enter the expression:')
    s = []
    length = len(expression)

    for i in range(length):
        if (operatorValidater(expression[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = expression[i] + op2 + op1
            s.append(temp)

        else:
            s.append(expression[i])
 
    ans = ""
    for i in s:
        ans += i
    return ans
  

print("Prefix : ", postToPre())
