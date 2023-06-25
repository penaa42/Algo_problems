# HackerRank

#1
def sum_two(num1, num2):
    sum = num1 + num2
    return sum
# print(sum_two(35, 188))

#2
def sum_list(any_list):
    sum = 0
    for num in any_list:
        sum = sum + num
    return sum
# print(sum_list([3,4,5,3,2,5,4,3]))

#3
a = [1,2,3]
b = [3,2,1]

def list_position(list1, list2):
    # method is used with lists of the same length
    counter1 = 0 # list1 counter
    counter2 = 0 # list2 counter
    # index 0 is for counter1 (list1); index 1 is for counter2 (list2)
    # final score will show the winner
    final_score = []
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            counter1 += 1
        elif list1[i] < list2[i]:
            counter2 += 1
        else:
            print('Tied score, no point awarded')
    final_score.append(counter1)
    final_score.append(counter2)
    return final_score
# print(list_position(a,b))

#4
def aVeryBigSum(any_list):
    list_sum = 0
    for num in any_list:
        list_sum = list_sum + num
    return list_sum
# print(aVeryBigSum([100000, 100001, 100002, 100003, 100004, 100005]))

