def nonRepeat():
    string = input('give the string:')
    for i in string:
        if (string.find(i, (string.find(i)+1))) == -1:
            print("First non-repeating character is", i)
            break
    return

nonRepeat()
