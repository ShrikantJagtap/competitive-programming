"""
    Task :
            Input will be integer n
            If n is odd print weired
            if n is even in between 2, 5 print not weired
            if n is even in between 6, 20 print weired
            if n is greater than 20 print not weried
"""
if __name__ == '__main__':
    n = int(input())
    even = True if n%2==0 else False
    if not even:
        print("Weird")
    elif even and even >=2 and even <=5:
        print("Not Weird")
    elif even and even >=6 and even<=20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
