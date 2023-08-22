# Jin YuHan Burgess
# 22 August 2023
# Assignment #2

# Objective: Implement "mean_min()" that takes in a lit of integers and returns a
# list with the first element being the mean of the input list and the second being
# the minimum value in the input list

###################################################################################
test_list = [4,7,12,6,15]

def mean_min(test_list):
    min_num = test_list[0]
    mean = 0
    dem = 0

    for i in range(len(test_list)):
        mean = mean + test_list[i]
        dem = dem + 1

        if test_list[i] < min_num:
            min_num = test_list[i]

    return((mean/dem), min_num)

print(mean_min(test_list))