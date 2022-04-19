# encoding=utf-8
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
import itertools

total = 0
for i in range(1, 5):
  for j in range(1, 5):
    for k in range(1, 5):
      if i != j and j != k and k != i:
        total += 1
        print(i, j, k)
print(total)

total2  = 0
a = [1,2,3,4]
for i in itertools.permutations(a, 3):
  print(i)
  total2 += 1
print(total2)
