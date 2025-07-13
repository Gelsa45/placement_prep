n=int(input())
a=input()
s=int(input())
for i in range(n):
    for j in range(i):
        if (int(a[i]+a[j])==int(s)):
            print(a[i])
            print(a[j])
        break
print(-1)

