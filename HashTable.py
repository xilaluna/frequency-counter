from LinkedList import LinkedList


class HashTable:

    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    def create_arr(self, size):
        arr = []
        for i in range(size):
            linked_list = LinkedList()
            arr.append(linked_list)
        return arr

    def hash_func(self, key):
        word = key.lower()
        number_hash = ord(word[0])
        index = number_hash % self.size
        return index

    def insert(self, key, value):
        new_data = (key, value)
        key_hash = self.hash_func(key)
        ll = self.arr[key_hash].update(key)
        if ll == -1:
            self.arr[key_hash].append(new_data)

    def print_key_values(self):
        for ll in self.arr:
            ll.print_nodes()
