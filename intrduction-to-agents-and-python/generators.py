def fun(n):
    cnt=1
    while (cnt<n):
        yield cnt
        cnt+=1

cn=fun(5)
for x in cn:
    print(x)