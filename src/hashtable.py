class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):

      

        return hash(key)


    def _hash_mod(self, key):
        
        
        return self._hash(key) % self.capacity


    def insert(self, key, value):

        current = None
        index = self._hash_mod(key)

        if self.storage[index] != None:
            if self.storage[index].next == None:
                self.storage[index].next = LinkedPair(key, value)
            else: 
                self.insert(self.storage[index].next)
        else:
            self.storage[index] = LinkedPair(key, value)

        return



        # if self.storage[index] == None:
        #     self.storage[index] = LinkedPair(key, value)
        # elif self.storage[index].next == None:
        #     self.storage[index].next = LinkedPair(key, value)
        # else:
        #     while self.storage[index].next != None:
                
        #         current = self.storage[index].next
        #         current.insert(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] != None:
            if self.storage[index].key == key:
                self.storage[index] = None
            else:
                print(f"Collision at {index}")
        else:
            print(f"Warning key {key} not found")

        return

        # current = None

        # if self.storage[self._hash_mod(key)] != None:
        #     if self.storage[self._hash_mod(key)].key == key:
        #         self.storage[self._hash_mod(key)].value = None
        #     elif self.storage[self._hash_mod(key)].next != None:
        #         current = self.storage[self._hash_mod(key)].next
        #         current.remove(key)
        # else:
        #     print("Key not found.")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] != None:
            if self.storage[index].key == key:
                return self.storage[index].value
            else:
                print(f"Collision at {index}")
        else:
            return None

        return


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for item in old_storage:
            self.insert(item.key, item.value)



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

    