"""Implementation sorted list..."""

def sorted_list(data):
    data_length = len(data)

    for i in range(data_length - 1):
        start_index = i
        for j in range(i+1, data_length):
            if data[j] < data[start_index]:
                start_index = j

        if start_index != i:
            result = data[i]
            data[i] = data[start_index]
            data[start_index] = result
if __name__ == "__main__":
    data = [5, 10, 8, 50, 75, 42, 32, 15, 20]
    sorted_list(data)
    print("sorted list: ", data)
