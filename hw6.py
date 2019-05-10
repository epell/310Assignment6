# CSC310 Assignment 6
# Priority Queue and Heap
# Ethan Pellittiere
# 4/2/19


class PrioQueue:
    head = None

    def __init__(self):
        None

    def push(self, datum, priority):
        if self.head is None:
            self.head = self.PQ(datum, priority)
        else:
            if priority < self.head.prio:
                print("p")
                self.head = self.PQ(datum, priority, self.head)
            else:
                current = self.head
                while current.next is not None:
                    if current.next.prio > priority:
                        current.next = self.PQ(datum, priority, current.next)
                        return
                    current = current.next
                current.next = self.PQ(datum, priority)

    def pop(self):
        if self.head is None:
            return "End of Queue"
        ofTheKing = self.head.datum
        self.head = self.head.next
        return ofTheKing

    class PQ:
        def __init__(self, datum, priority, next=None):
            self.datum = datum
            self.prio = priority
            self.next = next


def heapSort(unsorted):
    import math
    heap = []
    for value in unsorted:
        heap.append(value)
        child = len(heap)-1
        while child > 0:
            parent = math.floor((child-1)/2)
            if heap[child] <= heap[parent]:
                break
            temp = heap[parent]
            heap[parent] = heap[child]
            heap[child] = temp
            child = parent
    ofTheJedi = [] # 9 7 5 2 6 4
    while len(heap) > 1:
        ofTheJedi.append(heap[0])
        heap[0] = heap.pop(-1)
        parent = 0
        while 1:
            left_swap = False
            right_swap = False
            left = parent*2 + 1
            right = parent*2 + 2
            if left < len(heap) and heap[parent] < heap[left]:
                left_swap = True
            if right < len(heap) and heap[parent] < heap[right]:
                right_swap = True
            if left_swap and right_swap:
                if heap[left] > heap[right]:
                    temp = heap[parent]
                    heap[parent] = heap[left]
                    heap[left] = temp
                    parent = left
                else:
                    temp = heap[parent]
                    heap[parent] = heap[right]
                    heap[right] = temp
                    parent = right
            elif left_swap:
                temp = heap[parent]
                heap[parent] = heap[left]
                heap[left] = temp
                parent = left
            elif right_swap:
                temp = heap[parent]
                heap[parent] = heap[right]
                heap[right] = temp
                parent = right
            else:
                break
    ofTheJedi.append(heap.pop())
    return ofTheJedi


class MinHeap:
    import math

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.upheap()

    def find_min(self):
        return self.heap[0]

    def del_min(self):
        if self.is_empty():
            return "Error: Heap is empty"
        valOut = self.heap[0]
        if self.size() > 1:
            self.heap[0] = self.heap.pop(-1)
            self.downheap()
        else:
            self.heap = []
        return valOut

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def upheap(self):
        child = len(self.heap) - 1
        while child > 0:
            parent = self.math.floor((child - 1) / 2)
            if self.heap[child] >= self.heap[parent]:
                break
            temp = self.heap[parent]
            self.heap[parent] = self.heap[child]
            self.heap[child] = temp
            child = parent

    def downheap(self):
        parent = 0
        while 1:
            left_swap = False
            right_swap = False
            left = parent * 2 + 1
            right = parent * 2 + 2
            if left < len(self.heap) and self.heap[parent] > self.heap[left]:
                left_swap = True
            if right < len(self.heap) and self.heap[parent] > self.heap[right]:
                right_swap = True
            if left_swap and right_swap:
                if self.heap[left] < self.heap[right]:
                    temp = self.heap[parent]
                    self.heap[parent] = self.heap[left]
                    self.heap[left] = temp
                    parent = left
                else:
                    temp = self.heap[parent]
                    self.heap[parent] = self.heap[right]
                    self.heap[right] = temp
                    parent = right
            elif left_swap:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[left]
                self.heap[left] = temp
                parent = left
            elif right_swap:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[right]
                self.heap[right] = temp
                parent = right
            else:
                break

    def build_heap(self, val_list):
        self.heap = []
        for x in val_list:
            self.insert(x)


def main():
    # Insertion sort using a priority queue
    p_q = PrioQueue()
    print("Priority Queue: Enter unsorted list, separated by spaces:")
    unsorted = list(map(int, input().split()))
    if unsorted:
        print("Input:", end=" ")
        for val in unsorted:
            p_q.push(val, val)
            print(str(val), end=" ")
        print()
        print("Output:", end=" ")
        for x in range(0, len(unsorted)):
            print(str(p_q.pop()), end=" ")
        print()

    print("Heap Sort: Enter unsorted list, separated by spaces:")
    unsorted = list(map(int, input().split()))
    if unsorted:
        print("Sorted: " + str(heapSort(unsorted)))

    mh = MinHeap()
    while 1:
        print("1: Insert value")
        print("2: Build new heap from list")
        print("3: Find Minimum")
        print("4: Delete Minimum")
        print("5: Check Emptiness")
        print("6: Check Size")
        print("Q/q: Exit")
        user_in = input()

        if user_in == "1":
            mh.insert(int(input("Value to insert: ")))
        elif user_in == "2":
            print("Enter list, separated by spaces:")
            mh.build_heap(list(map(int, input().split())))
        elif user_in == "3":
            print("Minimum Value: " + str(mh.find_min()))
        elif user_in == "4":
            print("Deleted Value: " + str(mh.del_min()))
        elif user_in == "5":
            print("Is Heap empty?: " + str(mh.is_empty()))
        elif user_in == "6":
            print("Size of heap: " + str(mh.size()))
        elif user_in == "q" or user_in == "Q":
            break;
        print()
        input("Press any key to continue:")

main()