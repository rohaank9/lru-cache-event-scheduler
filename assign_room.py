def assign_rooms(events):
    events = sorted(events, key=lambda x: x[0])

    heap = []  # (end_time, room_id)
    room_count = 0
    result = []

    for start, end in events:
        if heap and heap[0][0] <= start:
            _, room_id = heapq.heappop(heap)
        else:
            room_id = room_count
            room_count += 1

        heapq.heappush(heap, (end, room_id))
        result.append((start, end, room_id))

    return result
