def sorted_list(data_item):
    length = len(data_item)

    for i in range(length - 1):
        start_index = i
        for j in range(i+1, length):
            if data_item[j] < data_item[start_index]:
                start_index = j

        if start_index != i:
            result = data_item[i]
            data_item[i] = data_item[start_index]
            data_item[start_index] = result

if __name__ == "__main__":
    data_item = [12, 54, 87, 45, 4, 55]
    sorted_list(data_item)
    print("sorted list is: ", data_item)