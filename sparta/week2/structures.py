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
