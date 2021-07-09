def sorted_list(item_value):
    item_length = len(item_value)

    for i in range(item_length - 1):
        mid_index = i
        for j in range(i+1, item_length):
            if item_value[j] < item_value[mid_index]:
                mid_index = j

        if mid_index != i:
            result = item_value[i]
            item_value[i] = item_value[mid_index]
            item_value[mid_index] = result

if __name__ == "__main__":
    item_value = [23, 68, 78 ,75, 45, 50]
    sorted_list(item_value)
    print("sorted item_value is: ", item_value)