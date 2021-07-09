def sorted_list(list):
    n = len(list)

    for i in range(n-1):
        mid = i
        for j in range(i+1, n):
            if list[j] < list[mid]:
                mid = j
            
        if mid != i:
            temp = list[i]
            list[i] = list[mid]
            list[mid] = temp


if __name__ == "__main__":
    list = [12, 5, 87, 4, 65, 5]
    sorted_list(list)
    print("sorted list", list)