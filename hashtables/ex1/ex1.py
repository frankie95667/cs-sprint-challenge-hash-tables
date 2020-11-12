def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    if len(weights) < 2:
        return None

    hashed_weights = {}

    for i in range(len(weights)):
        if limit - weights[i] in hashed_weights:
            return (i, hashed_weights[limit - weights[i]])
        hashed_weights[weights[i]] = i

    return None
