def fib(n):
    a,b = 0,1
    while a <= n :
        print (a)
        a,b = b, a + b

    print("end of fibonacci!")

	
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

