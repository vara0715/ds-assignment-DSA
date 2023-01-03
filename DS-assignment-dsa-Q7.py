def prefixToInfix():
    prefix = input('enter the expression:')
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if not operatorValidater(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    return stack.pop()
 
def operatorValidater(x):
    if x in ["+","-","/","*", "^", "(", ")"]:
        return True
    return False
 


print(prefixToInfix())
