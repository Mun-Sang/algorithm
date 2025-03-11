# 1부터 N까지 탐색하며 각 자릿수의 합과 M의 합이 N과 같으면 break, 없으면 0 출력

N = int(input())


for i in range(1, N+1):
  # str로 변경 후 읽고 각 자리수 합 저장
  sum_digits = sum(map(int, str(i)))
  sum_total = i + sum_digits
  # print(i) 범위확인을 위함
  if(sum_total == N):
    print(i)
    break
    
  if(i == N):
    print(0)