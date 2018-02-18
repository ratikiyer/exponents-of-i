num = 99.0
s1 = "i**%s="%num

if num % 4 ==  1:
    print (s1, "i")
elif num % 4 ==  2:
    print (s1, "-1")
elif num % 4 ==  3:
    print (s1, "-i")
else:
    print (s1, "1")
