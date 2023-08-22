# Jin YuHan Burgess
######################################
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
