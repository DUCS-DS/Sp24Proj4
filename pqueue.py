from heap import MinHeap


class PriorityQueue:
    """Custom priority queue.

    Items are tuples for which only the first entries need be comparable.
    """

    def __init__(self):
        self.heap = MinHeap()

    def enqueue(self, item):
        self.heap.insert(item)

    def dequeue(self):
        return self.heap.remove()

    def length(self):
        return self.heap.size


if __name__ == "__main__":

    q = PriorityQueue()
    q.enqueue((1, "z"))
    q.enqueue((4, "r"))
    q.enqueue((7, "c"))
    q.enqueue((2, "c"))
    assert q.length() == 4
    assert q.dequeue() == (1, "z")
    assert q.dequeue() == (2, "c")
    assert q.length() == 2
    q.dequeue()
    q.dequeue()
    assert q.length() == 0
