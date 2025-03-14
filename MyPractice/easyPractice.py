def inputFunc():
    A, B = input().split()
    C, D, E = input().split()
    F, G, H, I = input().split()
    print(A, B, C, D, E, F, G, H, I)


t = int(input())

for i in range(t):
    # accept 2 integers on the 1st line of each test case
    A, B = map(int, input().split())
    
    # accept 1 string on the 2nd line of each test case
    C = input()
    
    # output the 2 integers and 1 string on a single line
    print(A, B, C)   

t = int(input())
for i in range(t):
    n = int(input())
    print(n+1)  


# accept the count of test cases given in the the 1st line
x = int(input())
# run a for loop for each test case
# then for each test case input an integer and output it's negative
for item in range(x):
    y = int(input())
    n = (-1) * y
    print(n)


t = int(input())
for i in range(t):
    # take input and output the join using +
    s = input()
    x = s + s
    print(x)    

