# This is the first line of our numbers assignment program

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
new_list = ['aaa', 'bbb', 'ccc', 555, 222, 999]

# for i in range(0,6):
#     print("new listin", i,". elemanı =", new_list[i])
    
# print("program bitti")



# numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
# repeated_num = sorted(numbers, key=numbers.count)
# how_many = repeated_num.count(repeated_num[-1])
# print("The most frequent number is {} and it was {} times repeated".format(repeated_num[-1], how_many))

test_list = [1, 3, 7, 4, 3, 0, 3, 6, 3]
res = max(set(test_list), key = test_list.count) 
mes = test_list.count(res)
print ("the most frequent number is "+ str(res)+' and it was '+str(mes)+' times repeated' )
