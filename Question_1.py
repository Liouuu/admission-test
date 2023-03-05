'''
Question 1

'''
def find_max(numbers):
    max_num = numbers[0]   
    for i in numbers: #遍歷numbers
        if i > max_num:
            max_num = i
    return max_num

def find_position(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1        

# print(find_max([1, 2, 4, 5]) ); # should print 5
# print(find_max([5, 2, 7, 1, 6]) ); # should print 7
# print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
# print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
# print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
# print(find_position([5, 2, 7, 1, 6], 8)) # should print -1






'''
Question 2:

'''
def count(input):
    obj={} #create an obj
    for i in input:
        if i in obj:
            obj[i] =  obj[i]+1
        else:
            obj[i] = 1
    return obj

def group_by_key(input):
    result = {}
    for item in input:
        key = item['key']
        value = item['value']
        if key in result:
            result[key] = result[key] + value
        else:
            result[key] = value
    return result

# input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
# print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

# input2 = [
# {'key': 'a', 'value': 3},
# {'key': 'b', 'value': 1},
# {'key': 'c', 'value': 2},
# {'key': 'a', 'value': 3},
# {'key': 'c', 'value': 5}
# ]
# print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}






'''
Question 3:

1. What is Git and why is it used?
    Git是一種版本控制系統，可以保留檔案的新增、修改、刪除的歷史紀錄。
    軟體開發的時候，一個專案通常由多人協作，過程中我們會不斷的修改，因此版本的控制不可或缺。
    藉由git，可以多個作者共同編輯專案中的文件、DB、及原始碼等等，以達到開發需要的便利性。

2. What is the difference between List, Dictionary, Tuple and Set in Python?
    以上四個皆為Python的資料型別。
    不同之處為以下:
    中文    List:列表    Dictionary:字典     Tuple:元組        Set:集合
    符號     List []	    Tuple ()   	     Set {}  	    Dictionary {}
    序號	    有	          有               無         	     無
    更改資料	可	          不可	 	 
    重複	   允許	          允許             沒有	             沒有
    索引	 	 	                          無索引	      可變更索引
'''
