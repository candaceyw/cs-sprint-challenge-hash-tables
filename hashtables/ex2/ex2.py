#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # create dictionary for tickets
    ticket_dict = {}

    # loop through tickets
    for index in tickets:
        ticket_dict[index.source] = index.destination

    # destination's source is NONE then first flight
    # destination == source then route add to array
    # creates rout array and finds start ticket dest of NONE
    route = [ticket_dict["NONE"]]

    # find first flight and append it to route array
    # first flight ticket has a destination with a source of NONE, add to route

    # iterate routes array
    for _ in range(1, length):
        # add to end of dict
        route.append(ticket_dict[route[-1]])
    return route
