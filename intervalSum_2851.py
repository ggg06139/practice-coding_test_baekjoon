mushroom_list = []

for i in range(10):
  mushroom_list.append(int(input()))

result = 0
for i in mushroom_list:
  result += i
  if result >= 100:
    if abs(100-result) <= abs(100-(result-i)):
      break
    else:
      result -= i
      break
      
print(result)
