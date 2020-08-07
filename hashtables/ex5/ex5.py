# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    hashtable = {}
    for i in range(len(queries)):
        hashtable[queries[i]] = True
    
    for file in files:
        split_file = file.split("/")
        if split_file[-1] in hashtable:
            result.append(file)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
