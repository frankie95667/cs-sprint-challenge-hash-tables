def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    hashtable = {}
    # loop over array of arrays
    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            # add all elements in the first array of arrays as keys in the hashtable and set value to 1
            if i == 0:
                hashtable[arrays[i][j]] = 1
            # check if key is in hashtable at the current elements in the subarray
            elif arrays[i][j] in hashtable:
                # increment value by 1
                hashtable[arrays[i][j]] += 1

    # add keys to array that have values that equal the arrays length
    result = [key for key, value in hashtable.items() if value == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
