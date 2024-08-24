# N과 M을 입력 받는다
# M은 열의 크기(세로) columns
# N은 행의 크기(가로) row

N, M = input().split()

N = int(N)
M = int(M)

# arr = [[0 for j in range(column)] for i in range(row)]
arr = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
  row_input = input()
  for j in range(M):
    arr[i][j] = row_input[j]
    
print("\n입력된 2차원 배열:")
for row in arr:
  print(''.join(row))

square = []
# window가 움직이는 횟수  
for i in range(N - 7):
  for j in range(M - 7):

    min_square = 0
    # window 안을 하나씩 탐색하면서
    for k in range(i, i+8):
      for l in range(j, j+8):
        # "W"로 처음 시작했을 때, 첫 시작 결정은 i와 j
        if(arr[i][j] == 'W'):
          # 행: 짝, 열: 짝
          if(k % 2 == 0 and l % 2 == 0):
            if(arr[k][l] != 'W'):
              min_square += 1
          # 행: 짝, 열: 홀
          elif(k % 2 == 0 and l % 2 == 1):
            if(arr[k][l] != 'B'):
              min_square += 1            
          # 행: 홀, 열: 짝
          elif(k % 2 == 1 and l % 2 == 0):
            if(arr[k][l] != 'B'):
              min_square += 1            
          # 행: 홀, 열: 홀
          elif(k % 2 == 1 and l % 2 == 1):
            if(arr[k][l] != 'W'):
              min_square += 1            

        # "B"로 처음 시작했을 때
        if(arr[i][j] == 'B'):
          # 행: 짝, 열: 짝
          if(k % 2 == 0 and l % 2 == 0):
            if(arr[k][l] != 'B'):
              min_square += 1
          # 행: 짝, 열: 홀
          elif(k % 2 == 0 and l % 2 == 1):
            if(arr[k][l] != 'W'):
              min_square += 1            
          # 행: 홀, 열: 짝
          elif(k % 2 == 1 and l % 2 == 0):
            if(arr[k][l] != 'W'):
              min_square += 1            
          # 행: 홀, 열: 홀
          elif(k % 2 == 1 and l % 2 == 1):
            if(arr[k][l] != 'B'):
              min_square += 1              
  square.append(min_square)
        
print(min(square))    