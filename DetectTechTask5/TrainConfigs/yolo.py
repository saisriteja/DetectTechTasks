# Python3 code to demonstrate
# consecutive element pairing 
# using list comprehension
  
# initializing list
import numpy as np
test_list = np.arange(0,21,1)
  

# [27, 28], [28, 29], [29, 30],
# [31, 32], [32, 33], [33, 34], [34, 35],
# [36, 37], [37, 38], [38, 39], [39, 40], [40, 41],
# [42, 43], [43, 44], [44, 45], [45, 46], [46, 47],
# [48, 49], [49, 50], [50, 51], [51, 52], [52, 53], [53, 54], [54, 55], [55, 56], [56, 57], [57, 58], [58, 59],
# [61, 62], [62, 63], [63, 64], [64, 65], [65, 66], [66, 67]



# printing original list
print("The original list : " + str(test_list))
  
# using list comprehension
# consecutive element pairing 
res = [[test_list[i], test_list[i + 1]]
        for i in range(len(test_list) - 1)]
  
# print result
print("The consecutive element paired list is : " + str(res))



[[0, 1], [1, 2], [2, 3], [3, 4], 
[0, 5], [5, 6], [6, 7], [7, 8], 
[0, 9], [9, 10], [10, 11], [11, 12], 
[0, 13], [13, 14], [14, 15], [15, 16], 
[0, 17], [17, 18], [18, 19], [19, 20]]


# [27, 28], [28, 29], [29, 30],