import time, random
test
test2


test
def evaluate_n2(A, x):
	f2 = 0
	for i in range(0,n-1):
		for j in range(i,n-1):
			x_f = x**j
		f2 += A[i] * x_f
	return f2
	
	# code for O(n^2)-time function

def evaluate_n(A, x):
	f = 0
	for i in range(0, n-1):
		f += A[i]*x**i
	return f
	# code for O(n)-time function

random.seed()		# random 함수 초기화
n = int(input()) # n 입력받음
A = [random.randint(-1000,1000) for r in range(n)] 
a = random.randint(-1000,1000) # 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움

s2 = time.process_time()
t2 = evaluate_n2(A, a)
e2 = time.process_time()
t2_result = e2-s2
print(t2_result)

s = time.process_time()
t = evaluate_n(A, a)# evaluate_n2 호출
e = time.process_time()
t_result = e-s
print(t_result)
# evaluate_n 호출
