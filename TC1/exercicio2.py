
a = 1.0
while abs(((a**2)-2)) >= 10**(-6):
	a = (a+(2/a))/2
print(a)
