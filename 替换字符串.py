def replaceSpace(s):
    # write code here
    t = ''
    for i in s:
        if i == ' ':
            i = i.replace(i, '%20')
            t += i
        else:
            t += i
    return t

s = '  hello world'
print(replaceSpace(s))