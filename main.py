from lru_cache import LRUCache
from event_scheduler import can_attend_all, min_rooms_required
from assign_room import assign_rooms   


def test_lru():
    print("LRU Cache Test")

    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)

    print("Get 1:", cache.get(1))  # 10

    cache.put(3, 30)  # evicts 2
    print("Get 2:", cache.get(2))  # -1


def test_scheduler():
    print("\nEvent Scheduler Test")

    events = [(9, 10), (10, 11), (10, 12)]

    print("Can attend all:", can_attend_all(events))
    print("Min rooms:", min_rooms_required(events))


def test_room_assignment():
    print("\nRoom Assignment Test")

    events_list = [
        [(9, 10), (10, 11), (11, 12)],
        [(9, 11), (10, 12)],
        [(1, 4), (2, 5), (7, 9)]
    ]

    for i, events in enumerate(events_list, 1):
        print(f"\nTest Case {i}: {events}")
        assigned = assign_rooms(events)

        for start, end, room in assigned:
            print(f"Event {start}-{end} -> Room {room}")


if __name__ == "__main__":
    print("===== RUNNING TESTS =====\n")

    test_lru()
    test_scheduler()
    test_room_assignment()

    print("\n===== DONE =====")
