 def can_attend_all(events):
    events.sort(key=lambda x: x[0])  # sort by start time

    for i in range(1, len(events)):
        if events[i][0] < events[i - 1][1]:
            return False
    return True

import heapq

def min_rooms_required(events):
    if not events:
        return 0

    events.sort(key=lambda x: x[0])

    min_heap = []  # stores end times

    for start, end in events:
        # Free room if possible
        if min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)

        heapq.heappush(min_heap, end)

    return len(min_heap)
