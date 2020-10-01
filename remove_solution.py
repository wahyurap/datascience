new_list = []
def remove_duplicate(list):
    i = 0
    j = 1
    while i < len(list):
        while j <len(list):
            if list[i]==list[j]:
                del list[j]
                j +=1
            else:
                j+=1
        i+=1
        j=i+1
    new_list = list[:]
    return new_list

def remove_duplicate_with_set(list):
    new_list = set(list)
    return new_list 

obj_list = [1, 2, 4, 6, 2, 1, 4, 5, 7, 8, 6]
print(remove_duplicate(obj_list))
print(remove_duplicate_with_set(obj_list))


