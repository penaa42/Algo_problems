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
    counter1 = 0
    counter2 = 0
    final_score = []
    print(list1)
    print(list2)
    for i in list1:
        if i > list2[i]:
            print(f'second print {i}')
            counter1 += 1
        elif list1[i] < list2[i]:
            counter2 += 1
        else:
            print('Tied score, no point awarded')
    final_score.append(counter1)
    final_score.append(counter2)
    print(final_score)
    return final_score
print(list_position(a,b))
# if a[i] < b[i]:
# counter1
# counter2
# store into an array


# correct indexing problem for loop