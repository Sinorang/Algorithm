class HashNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None


class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash_function(self, key):
        return key % self.size

    def put(self, key, val):
        idx = self._hash_function(key)
        if self.table[idx] is None:
            self.table[idx] = HashNode(key, val)
        else:
            node = self.table[idx]
            while node.next is not None:
                node = node.next
            node.next = HashNode(key, val)

    def get(self, key):
        idx = self._hash_function(key)
        node = self.table[idx]
        while node is not None:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key):
        idx = self._hash_function(key)
        node = self.table[idx]
        prev_node = None

        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.table[idx] = node.next
                else:
                    prev_node.next = node.next
                return
            prev_node = node
            node = node.next
