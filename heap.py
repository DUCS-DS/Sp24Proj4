
class MinHeap:
    """Custom min-heap implementation.

    The keys here are tuples, (only) the first elements of which must
    be comparable.
    """

    def __init__(self):
        self.list = [0]
        self.size = 0

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.list[i][0] < self.list[i // 2][0]:
                tmp = self.list[i // 2]
                self.list[i // 2] = self.list[i]
                self.list[i] = tmp
            i = i // 2

    def insert(self, tup):
        self.list.append(tup)
        self.size = self.size + 1
        self.percolate_up(self.size)

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            mc = self.min_child(i)
            if self.list[i][0] > self.list[mc][0]:
                tmp = self.list[i]
                self.list[i] = self.list[mc]
                self.list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.list[i * 2][0] < self.list[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def remove(self):
        retval = self.list[1]
        self.list[1] = self.list[self.size]
        self.size = self.size - 1
        self.list.pop()
        self.percolate_down(1)
        return retval

    def build_heap(self, lst):
        i = len(lst) // 2
        self.size = len(lst)
        self.list = [0] + lst[:]
        while i > 0:
            self.percolate_down(i)
            i = i - 1


if __name__ == "__main__":

    h = MinHeap()
    h.build_heap(
        [(9, MinHeap()), (5, MinHeap()), (6, MinHeap()), (2, MinHeap()), (3, MinHeap())]
    )
    assert h.size == 5
    h.remove()
    h.remove()
    h.remove()
    h.remove()
    h.remove()
    assert h.size == 0

    h = MinHeap()
    h.insert((5, "a"))
    h.insert((1, "b"))
    assert h.size == 2
    assert h.remove() == (1, "b")
