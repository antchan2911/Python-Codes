a, b, c, d = map(int, input().split())
if ((a + b) > c and (b + c) > a and (c + a) > b):
    print("S")
elif ((a + b) > d and (a + d) > b and (b + d) > a):
    print("S")
elif((b + c) > d and (b + d) > c and (c + d) > b):
    print("S")
elif ((a + c) > d and (a + d) > c and (c + d) > a):
    print("S")
else:
    print("N")
