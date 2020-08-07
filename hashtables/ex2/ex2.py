#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []
    hashed_flight = {}
    for i in range(length):
        hashed_flight[tickets[i].source] = tickets[i].destination

    key = "NONE"
    for item in hashed_flight.items():
        route.append(hashed_flight[key])
        key = hashed_flight[key]
        
    return route
