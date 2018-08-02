n=int(input())
if(n%4):
	print('yes')
	if(n%100):
		print('yes')
		if(n%400):
			print('yes')
		else:
			print('no')
	else:
		print('no')
else:
	print('no')
	
