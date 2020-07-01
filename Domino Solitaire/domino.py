n=int(input())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))

prev=0
result=abs(s1[0]-s2[0])
for i in range(1,n):
	vertical=result+abs(s1[i]-s2[i])
	horizontal=prev+abs(s1[i]-s1[i-1])+abs(s2[i]-s2[i-1])
	prev=result
	result=max(vertical,horizontal)
print(result)
