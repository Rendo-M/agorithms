from functools import reduce

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def main():
    data = [-6,0, 1, 2, 3, 5, 7, 9]
    search_item = -3
    result = binary_search(data, search_item)
    print(f"Item {search_item} found at index {result}")

if __name__ == "__main__":
    main()
