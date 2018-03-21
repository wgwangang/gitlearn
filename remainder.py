
def main():
	rl = []
	for i in range(0, 1000):
		r18 = i % 18
		r33 = i % 33
		if r18 == r33:
			rl.append(i)
	#print(rl)
	print(len(rl))

	a = 16520
	b = 14903
	c = 14177

	r = 0

	for i in range(1, c):
		ra = a % i
		rb = b % i
		rc = c % i 

		if ra == rb and rb == rc:
			r = i

	print(r)

if __name__ == '__main__':
	main()