# lru-cache-event-scheduler
# LRU Cache & Event Scheduler (Python)

##  Overview
This repository contains solutions to two core data structure and algorithm problems:

1. LRU Cache Implementation
2. Event Scheduler System

The implementations are designed to be efficient and aligned with real-world system design principles.

---

#  Problem 1: LRU Cache

## Description
Implement a Least Recently Used (LRU) Cache with:
- `get(key)` → returns value if exists, else -1
- `put(key, value)` → inserts/updates key and evicts least recently used item if needed

## Approach
The solution uses:
- **Hash Map (Dictionary)** → O(1) lookup
- **OrderedDict (Python)** → maintains usage order

### Logic
- On `get`:
  - If key exists → move it to most recent position
- On `put`:
  - Insert/update key
  - If capacity exceeded → remove least recently used item

## Complexity
- Time:
  - get → O(1)
  - put → O(1)
- Space → O(capacity)

## Key Insight
Using only a hash map wouldn’t track usage order, and using only a list would make lookup O(n).  
Combining both ensures optimal performance.

---

#  Problem 2: Event Scheduler

## Description
Given a list of events `(start, end)`, determine:
- If all events can be attended
- Minimum number of meeting rooms required

---

## Part 1: Can Attend All Events

### Approach
- Sort events by start time
- Compare consecutive events

### Logic
- If `current.start < previous.end` → overlap → return False
- Else → continue

### Complexity
- Time → O(n log n)
- Space → O(1)

---

## Part 2: Minimum Rooms Required

### Approach
- Sort events by start time
- Use a **min-heap** to track ongoing meetings

### Logic
- If earliest ending meeting is finished → reuse room
- Else → allocate new room

### Key Insight
The heap always contains active meetings, so its size represents the number of rooms required.

### Complexity
- Time → O(n log n)
- Space → O(n)

---

#  Future Enhancement: Room Assignment

The scheduler is extended to assign room numbers using:
- Min-heap storing `(end_time, room_id)`

This allows:
- Efficient reuse of rooms
- Real-world applicability (meeting systems, booking systems)

---

# 📊 Final Complexity Summary

## LRU Cache
| Operation | Time | Space |
|----------|------|-------|
| get() | O(1) | |
| put() | O(1) | O(capacity) |

## Event Scheduler
| Function | Time | Space |
|----------|------|-------|
| can_attend_all | O(n log n) | O(1) |
| min_rooms_required | O(n log n) | O(n) |

---

# Design Trade-offs

- Only Hash Map → no order tracking  
- Only List → slow lookup O(n)  

 Combined:
- Hash Map → fast access  
- Ordered structure → efficient eviction  

---

#  Concurrency (Extension)

To make LRU cache thread-safe:
- Use a global lock (`threading.Lock`)
- Wrap `get` and `put` operations

---

#  Project Structure

- `lru_cache.py` → LRU Cache implementation  
- `event_scheduler.py` → Event scheduling logic  
- `room_assignment.py` → Room allocation extension  
- `main.py` → Test script  

---

#  How to Run

```bash
python main.py
