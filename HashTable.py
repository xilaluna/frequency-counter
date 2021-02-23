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
        number_hash = hash(key.lower())
        index = number_hash % self.size
        return index

    # 3️⃣ TODO: Complete the insert method.

    # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

    def insert(self, key, value):
        new_data = (key, value)
        key_hash = self.hash_func(key)
        ll = self.arr[key_hash]
        if ll.find(key) == -1:
            print(f"{key} was not found")
            ll.append(new_data)
        else:
            ll.update(key, value)

    def print_key_values(self):
        for ll in self.arr:
            ll.print_nodes()
