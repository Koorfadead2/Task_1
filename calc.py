import sys
print("Введите начальное число")
start = input()
if (not start.isdigit()):
    sys.exit("Не число")
t = True
flag = True
start = int(start)
while(t):
    print("Введите операцию и число")
    a = input()
    if (not (a[0:] >= chr(48) and a[0:] <= chr(57) or (a[0:] == chr(61) and len(a) == 1 ))):
        flag = True
    if (not (a[3:] >= chr(48) and a[3:] <= chr(57) and (a[0:2] == chr(42)))):
        flag = True
    if (not (a[2:] >= chr(48) and a[2:] <= chr(57) or (a[0:1] == chr(42)) or a[0:1] == chr(43) or a[0:1] == chr(45)) or a[0:1] == chr(47)):
        flag = True
    if (not flag):
        sys.exit("Не число")
    if (a == "="):
        t = False
    elif (a[0:2] == ("**")):
        start = start ** int(a[3:])
    elif (a[0] == "+"):
        start = start + int(a[2:])
    elif (a[0] == "-"):
        start = start - int(a[2:])
    elif (a[0] == "*"):
        start = start * int(a[2:])
    elif (a[0] == "/"):
        start = start / int(a[2:])
print(start)