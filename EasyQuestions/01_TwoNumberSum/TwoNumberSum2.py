def twoNumberSum(array, target_sum):
  result_list = []
  for i in range(0, len(array) - 1):
    first_number = array[i]
    for j in range(i+1,len(array)):
      second_number=array[j]
      sum= first_number + second_number
      if sum == target_sum:
        result_list.append(first_number)
        result_list.append(second_number)
    return sorted(result_list)
  print(sorted(result_list))
print(twoNumberSum([8, -3, -4, 7, 6, -5, -8, 12], 3))