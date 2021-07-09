def sorted_list(item):
    item_length = len(item)

    for i in range(item_length - 1):
        start_index = i
        for j in range(i+1, item_length):
            if item[j] < item[start_index]:
                start_index = j
        
        if start_index != i:
            result = item[i]
            item[i] = item[start_index]
            item[start_index] = result

if __name__ == "__main__":
    item = [12, 42, 12, 5, 4, 5, 75, 50]
    sorted_list(item)
    print("sorted list", item)