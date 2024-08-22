# 입력 받은 값은 문자열이고 split해도 문자열임
N, M = input().split()

N = int(N)
M = int(M)

# map(f, iterable): 각 요소에 f함수를 적용한 결과 출력 
number = list(map(int, input().split()))

max_sum = 0

# N개 데이터에서 3개 데이터 뽑기
# N의 개수가 달라지는 경우 그대로 사용하지만
# 뽑는 개수가 달라지는 경우 for문을 추가/감수 해야함

for i in range(N - 2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      sum = number[i] + number[j] + number[k]
      if(sum <= M and sum > max_sum):
        max_sum = sum


print(max_sum)
