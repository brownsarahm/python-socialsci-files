In the examples below, without running them try to predict why we will not get the desired answer.
Run each, one at a time, and then correct them. Remember that when the input next to a notebook cell is `[*]`` your python interpreter is still working.

# code
# while loop - summing the numbers 1 to 10
n = 10
cur_sum = 0
# sum of n  numbers
i = 0
while  i <= n :
   i = i + 1
   cur_sum = cur_sum + i

print("The sum of the numbers from 1 to", n, "is ", cur_sum)
# break cell here

# code
# while loop - summing the numbers 1 to 10
n = 10
cur_sum = 0
boolvalue = False
# sum of n  numbers
i = 0
while  i <= n and boolvalue:
   cur_sum = cur_sum + i
   i = i + 1

print("The sum of the numbers from 1 to", n, "is ", cur_sum)
# break cell here

# code
# while loop - summing the numbers 1 to 10
n = 10
cur_sum = 0
# sum of n  numbers
i = 0
while  i != n :
   cur_sum = cur_sum + i
   i = i + 1

print("The sum of the numbers from 1 to", n, "is ", cur_sum)
# break cell here

# code
# while loop - summing the numbers 1.1 to 9.9 i. steps of 1.1
n = 9.9
cur_sum = 0
# sum of n  numbers
i = 0
while  i != n :
   cur_sum = cur_sum + i
   i = i + 1.1
   print(i)

print("The sum of the numbers from 1.1 to", n, "is ", sum)
# break cell here