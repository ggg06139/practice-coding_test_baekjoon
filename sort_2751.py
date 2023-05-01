import sys
input = sys.stdin.readline

N = int(input())
unsorted_list = []

for i in range(N):
    unsorted_list.append(int(input()))

sorted_list = sorted(unsorted_list)

for j in range(len(sorted_list)):
    print(sorted_list[j])

# 반복문 코드 단축
# for j in sorted_list:
#     print(j)