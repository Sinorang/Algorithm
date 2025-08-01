class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        if not self.top:
            return None

        node = self.top
        self.top = node.next
        return node.val

    def is_empty(self):
        return self.top is None


class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(value)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.val

    def is_empty(self):
        return self.front is None


class HashNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = HashNode(key, value)
        else:
            node = self.table[index]
            while node.next is not None:
                node = node.next
            node.next = HashNode(key, value)

    def get(self, key):
        index = self._hash_function(key)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key):
        index = self._hash_function(key)
        node = self.table[index]
        prev_node = None
        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.table[index] = node.next
                else:
                    prev_node.next = node.next
                return
            prev_node = node
            node = node.next
