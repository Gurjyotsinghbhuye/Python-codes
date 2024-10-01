# You are given an array of integers nums and an integer target. 
# Write a function that finds all the subarrays from the list that sum up to the target value.

# def ret_subarrray_sum(nums,target):
#     ls = []
#     for i in range(0,len(nums)):
#         for j in range(0,len(nums)):
#             if sum(nums[i:j+1]) == target:  #slices from i to j+1 and sums all elements 
#                 ls.append(nums[i:j+1])
#     return ls

# nums = [1, 2, 3, 4, 5]

# target = 5  
# print(ret_subarrray_sum(nums, target))
# Output: [[2, 3], [5]]

# for i in range(0, 15):
        # if i % 3 == 0 and i % 5 ==0:
        #     print('FizzBuzz')
        
        # elif i % 3 == 0 and i % 5 !=0:
        #     print('Fizz')
            
        # elif i % 3 != 0 and i % 5 ==0:
        #     print('Fizz')

        # else:
        #     print(i)

#  Find the Index of the First Occurrence in a String

haystack = "sadbutsad"
needle = "sad"


    # Find the first occurrence of the word
first_occurrence = haystack.find(needle)

if first_occurrence == -1:
    print('Word not found even once')

# Find the second occurrence, starting just after the first
second_occurrence = haystack.find(needle, first_occurrence + len(needle)) # to find second occurane we need to 
# skip already first found occurance and start from there which would be length of word
print(first_occurrence)
print(second_occurrence)


