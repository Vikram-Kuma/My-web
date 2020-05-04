def binary_conversion(e):
    A=[]
    while e>0:
        A.append(e%2)
        e=e//2
    while len(A)<4:
        A.append(0)
    return A[::-1]

def compliment(e):
    A=[]
    while e>0:
        A.append(e%2)
        e=e//2
    while len(A)<4:
        A.append(0)
    A=A[::-1]
    for i in range(len(A)):
        if A[i]==0:
            A[i]=1
        else:
            A[i]=0
    count=1
    for i in range(len(A)-1,-1,-1):
        s=A[i]+count
        if s==2:
            A[i]=0
            count=1
        elif s==1:
            A[i]=1
            count=0
    return A
    
def add(result,M):
    X=result[0:4]
    count=0
    for i in range(len(X)-1,-1,-1):
        a=X[i]+M[i]+count
        if a==2:
            X[i]=0
            count=1
        elif a==3:
            X[i]=1
            count=1
        elif a==0:
            X[i]=0
            count=0
        elif a==1:
            X[i]=1
            count=0
    for i in range(len(X)):
        result[i]=X[i]
    print("After adding A and M, Result is: ",result)
    print()
    return result 
    
def right_shift(result):
    a=result[-2]
    for i in range(len(result)-2,0,-1):
        result[i]=result[i-1]
    result[0],result[-1]=a,a
    print("After Performing right_shift our answer is:",result)
    print()
    return result

def booth_algo(result,M,M0):
    n=4
    print()
    print('Initial array containing A,Q and Q(-1):',result)
    while n>0:
        if result[-1]==0 and result[-2]==1:
            print()
            print("Since Q(0)=1 and Q(-1)=0, Hence we'll perform Function (A-M)")
            print('Compliment of M is:',M0)
            result=add(result,M0)
        elif result[-1]==1 and result[-2]==0:
            print()
            print("Since Q(0)=0 and Q(-1)=1, Hence we'll perform Function (A+M)")
            result=add(result,M)
        result=right_shift(result)
        n-=1
        print('------------------------------------------------------------------')
    a=[str(i) for i in result[0:len(result)-1]]
    z=''.join(a)
    print("Our Final Result is: ",z)
    
print('Enter the First Number:',end=' ')
m=int(input())
print('Enter the Second Number:',end=' ')
q=int(input())
print('Expected output is:',m*q)
M=binary_conversion(m)
Q=binary_conversion(q)
M0=compliment(m)
result=[0,0,0,0]
for i in range(len(Q)):
    result.append(Q[i])
result.append(0)
booth_algo(result,M,M0)

