def sumofAP(n,a,d):
	sum=0
	k=0
	while k<n:
		sum=sum+a
		a=a+d
		k=k+1
	return sum
n,a,d=map(int,raw_input().split())	
print(sumofAP(n,a,d))	
