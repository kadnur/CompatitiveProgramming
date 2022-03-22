def twoNumSum(array, targetSum):
  for i in range(len(array) - 1):
    for j in range(i+1, len(array)):
      if array[i] + array[j] == targetSum:
        return [array[i], array[j]]
  return[]
print(twoNumSum([8, -3, -4, 7, 6, -5, -8, 12], 3))
