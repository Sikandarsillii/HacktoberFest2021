# Problem from Codeforces https://codeforces.com/contest/1440/problem/B

#Sum of Medians

T=int(input())
while T!=0:
    n,k=[int(i) for i in input().split()]
    v=[int(i) for i in input().split()]
    sums=0
    step=int(n/2)

    for i in v[-(step+1)::-(step+1)]:

        sums+=i
        k-=1
        if k==0:
            break
    print(sums)
    T-=1