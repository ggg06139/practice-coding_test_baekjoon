N, M = map(int, input().split())
num_list = list(map(int, input().split()))
sum = 0

#합 배열 리스트
prefix_sum = [0]

#구간 합 리스트
interval_sum = []

for a in num_list:
    sum += a
    prefix_sum.append(sum)

for b in range(M):
    i, j = map(int, input().split())
    interval_sum.append(prefix_sum[j] - prefix_sum[i-1])

for c in interval_sum:
    print(c)