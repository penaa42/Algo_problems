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

#5
test_list = [1, 1, 0, -1, -1, 34, 2, -4, -1, 0, 0, 2, -1, -3, 4, -1, 0]

def plusMinus(any_list):
    pos_num = 0
    neg_num = 0
    zero_num = 0
    list_length = len(any_list)
    for num in any_list:
        if num > 0:
            pos_num += 1
        elif num < 0:
            neg_num += 1
        else:
            zero_num += 1
    pos_ratio = pos_num / list_length
    neg_ratio = neg_num / list_length
    zero_ratio = zero_num / list_length
    print('Postive number ratio: ' + ('%.6f' % pos_ratio))
    print('Negative number ratio: ' + ('%.6f' % neg_ratio))
    print('Zero number ratio: ' + ('%.6f' % zero_ratio))
    return pos_num, neg_num, zero_num, pos_ratio, neg_ratio, zero_ratio
# plusMinus(test_list)

#6
# staircase
def staircase(num):
    spaces = num
    for i in range(1, (num + 1)):
        print((' ' * (spaces - 1)) + ('#' * i))
        spaces -= 1
# staircase(5)

#7
test_list1 = [1,2,3,4,5]
test_list2 = [11,12,13,14,15]

def miniMaxSum(any_list):
    if len(any_list) != 5:
        return False
    min_sorted_list = sorted(any_list)
    min_sorted_list.pop(4)

    max_sorted_list = sorted(any_list)
    max_sorted_list.pop(0)

    min_sum = 0
    max_sum = 0
    
    for i in min_sorted_list:
        min_sum += i

    for i in max_sorted_list:
        max_sum += i

    print(min_sum, max_sum)
    return min_sum, max_sum

# miniMaxSum(test_list1)
# miniMaxSum(test_list2)

#8
candles = [4,4,1,3]
candles1 = [3,2,1,3,3]
candles2 = [2,4,3,6,3,5,3,6,7,6,7,7,-1]

def birthdayCakeCandles(any_list):
    tallest_height = 0
    count = 0

    for i in any_list:
        if i <= 0:
            return False

    for i in any_list:
        if i > tallest_height:
            tallest_height = i

        if i == tallest_height:
            count += 1

    print(count)
    return count

# birthdayCakeCandles(candles)
# birthdayCakeCandles(candles1)
# birthdayCakeCandles(candles2)

#9
# military time
s = '12:01:00PM'
s1 = '12:01:00AM'

# def timeConversion(standard_time):

test_time = '12:00:00PM'
military_time = ''

def test(math_test):
    AM_check = 'AM'
    PM_check = 'PM'
    add_hours = 12
    time_limit = 24

    if AM_check in test_time:
        convert_am = test_time
        new_convert_am = convert_am.replace('AM', '')
        am_hour_adjust = new_convert_am[:2]
        print(am_hour_adjust)


    if PM_check in test_time:
        convert_pm = test_time
        new_convert_pm = convert_pm.replace('PM', '')
        
        pm_hour_adjust = new_convert_pm[:2]
        # print(pm_hour_adjust)
        
        pm_hour_adjust = int(pm_hour_adjust)
        
        final_time = pm_hour_adjust + add_hours

        if final_time >= time_limit:
            final_time = (final_time - time_limit)
            print(final_time)
            print(type(final_time))
            # military_time =


test(test_time)
# timeConversion(s)

#10
