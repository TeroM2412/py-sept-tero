def Prime_number(n):
	a = []
	for i in range(2,n+1):
		e1 = n % i
		if e1 == 0:
			b.append(e1)
	if len(a) > 1:
		print('FALSE')
		print('This is not a prime number!')
	elif len(a) == 1:
		print('TRUE')
		print('This is a Prime number!')
Prime_number(int(input('Please give your number:  ')))