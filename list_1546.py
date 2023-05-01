N = int(input())
score_list = list(map(int,input().split()))
sum_score = sum(score_list)

score_list = sorted(score_list)
best_score = score_list[-1]

average_score = sum_score * 100 / best_score / N
print(average_score)