def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    hashtable = {}
    for i in range(len(a)):
        if (a[i] < 0 and  abs(a[i]) in hashtable) or (a[i] > 0 and -a[i] in hashtable):
            result.append(abs(a[i]))
        hashtable[a[i]] = True

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
