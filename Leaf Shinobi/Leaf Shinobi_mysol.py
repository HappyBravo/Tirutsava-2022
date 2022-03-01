def prime(a):
    primeornot = True
    if a == 1:
        primeornot = False
    else:
       for i in range(2, int(a/2)+1):
            if (a%i == 0):
                primeornot = False
                break
    return primeornot

def list_primes(left, right):
    to_test = range(left, right)
    # primes = 
    print("\n".join([str(i) for i in to_test if i > 1 and len([_ for _ in range(2, 8) if i%_ == 0]) == 0]))
    

testcases = int(input())
for i in range(testcases):
    L, R = map(int, input().split())
    list_primes(L, R+1)
    # print(L,  R)
    # print("\n".join(list(map(str,list_primes(L, R+1)))))
    # for j in final:
    #     print(j)
    # for _ in range(L, R+1):
        # if (prime(_)):
            # print(_)
                
        
