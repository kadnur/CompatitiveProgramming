def array_1(array,sequence):
  j=0
  for num in array:
    if j == len(sequence):
      break
    if sequence[j] == num:
      j += 1
  return j == len(sequence)
print(array_1([6,-3,8,10,-2,5],[6,8,10]))