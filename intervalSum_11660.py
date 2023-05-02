# N, M = map(int, input().split())
# table_list = []

# for k in range(N):
#     table_list.append(list(map(int, input().split())))

table_list = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
N = 4
M = 3
result = []

for l in range(M):
    prefix_list = [0]
    sum = 0
    x1, y1, x2, y2 = map(int, input().split())
    x = x1
    prefix_list.append([0])

    for m in table_list[x-1]:
        sum += m
        prefix_list[-1].append(sum)
        
        if (m == table_list[x-1][N-1]) and (x-1 != x2-1):
            prefix_list.append([0])
            x += 1
            sum = 0
            
    for p in prefix_list:
        print(p)

print(table_list)