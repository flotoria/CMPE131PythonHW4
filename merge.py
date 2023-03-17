def merge(list1, list2): 
    
    list = [] 
    counter1 = 0
    counter2 = 0

    while counter1 < len(list1) and counter2 < len(list2): 
        if list1[counter1] < list2[counter2]:
            list.append(list1[counter1])
            counter1 += 1
        else: 
            list.append(list2[counter2])
            counter2 += 1

    while counter1 < len(list1):
        list.append(list1[counter1])
        counter1 += 1

    while counter2 < len(list2):
        list.append(list2[counter2])
        counter2 += 1

    return list
