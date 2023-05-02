# 런타임 에러 발생 코드

N, M = map(int, input().split())
table_list = []

for k in range(N):
    table_list.append(list(map(int, input().split())))

result = []

for l in range(M):
    prefix_list = [0]
    result_sum = 0
    total = 0
    x1, y1, x2, y2 = map(int, input().split())
    x = x1
    prefix_list.append([0])

    while True:
        for m in table_list[x-1]:
            total += m
            prefix_list[-1].append(total)
            
            if (m == table_list[x-1][N-1]) and (x-1 != x2-1):
                prefix_list.append([0])
                x += 1
                total = 0
                break
        
        else:
            for n in range(1, x2-x1+2):
                result_sum += prefix_list[n][y2] - prefix_list[n][y1-1]                
            result.append(result_sum)
            break

for o in result:
    print(o)