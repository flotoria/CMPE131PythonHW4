def cacti_number(arr):
    num = 0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == 0:
                # general case
                if row - 1 >= 0 and col - 1 >= 0 and row + 1 < len(arr) and col + 1 < len(arr[0]) and arr[row + 1][col] == 0 and arr[row - 1][col] == 0 and arr[row][col + 1] == 0 and arr [row - 1][col] == 0:
                    num += 1 
                    arr[row][col] = 1
                
                # edges 
                if arr[row][col] == 0 and (row == 0 or col == 0 or row == len(arr) - 1 or col == len(arr[0]) - 1): 
                    if row == 0 and col != 0 and col != len(arr[0]) - 1 and arr[row][col - 1] == 0 and arr[row][col + 1] == 0 and arr[row + 1][col] == 0:
                        num += 1
                        arr[row][col] = 1
                    elif col == 0 and row != 0 and row != len(arr) - 1 and arr[row - 1][col] == 0 and arr[row + 1][col] == 0 and arr[row][col + 1] == 0: 
                        num += 1
                        arr[row][col] = 1
                    elif row == len(arr) - 1 and col != 0 and col != len(arr[0]) - 1 and arr[row - 1][col] == 0 and arr[row][col - 1] == 0 and arr[row][col + 1] == 0:
                        num += 1
                        arr[row][col] = 1
                    elif col == len(arr[0]) - 1 and row != 0 and row != len(arr) - 1 and arr[row + 1][col] == 0 and arr[row - 1][col] == 0 and arr[row][col - 1] == 0:
                        num += 1
                        arr[row][col] = 1
                    elif row == 0 and col == 0 and arr[row + 1][col] == 0 and arr[row][col + 1] == 0:
                        num += 1
                        arr[row][col] = 1
                    elif row == len(arr) - 1 and col == 0 and arr[row - 1][col] == 0 and arr[row][col + 1] == 0:
                        num += 1
                        arr[row][col] = 1
                    elif row == 0 and col == len(arr[0]) - 1 and arr[row][col - 1] == 0 and arr[row + 1][col] == 0: 
                        num += 1
                        arr[row][col] = 1
                    else:
                        if row == len(arr) - 1 and col == len(arr[0]) - 1 and arr[row - 1][col] == 0 and arr[row][col - 1] == 0:
                            num += 1
                            arr[row][col] = 1

    return num

                
