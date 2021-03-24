print("Введите строку")
s = input()
a_count = 0 #97
o_count = 0 #111
u_count = 0 #117
i_count = 0 #105
e_count = 0 #101
y_count = 0 #121
for i in range(len(s)):
    if (s[i] == chr(97)):
        a_count += 1
    elif (s[i] == chr(111)):
        o_count += 1
    elif (s[i] == chr(105)):
        i_count += 1
    elif (s[i] == chr(101)):
        e_count += 1
    elif (s[i] == chr(117)):
        u_count += 1
    elif (s[i] == chr(121)):
        y_count += 1
print ("a" + " " + str(a_count) + "," , "o" + " " + str(o_count) + "," , "u" + " " + str(u_count) + "," , "i" + " " + str(i_count) + "," , "e" + " " + str(e_count) + "," , "y" + " " + str(y_count))