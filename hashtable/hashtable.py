class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.nums = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        
        
        load_factor = self.nums / self.capacity
        return load_factor
            


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash =((hash << 5) + hash) + ord(x)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """        
        # hash key
        index = self.hash_index(key)        
        items = 0
        
        for item in self.storage:
            if item is not None:
                items += 1
        return items > len(self.storage) / 2
        
        # check if key is present
        # if self.storage[index][0] == key
        
        # if storage is empty
        # if node is None:
        #     self.storage[index] = HashTableEntry(key, value)
        #     return None
        # # insert into linked list
        # prev = node
        # # while storage is not empty
        # while node is not None:
        #     if node[0] == key:
        #         node[0] = key
        #     prev = node
        #     node = node.next
        # prev.next = HashTableEntry(key, value)
        # self.nums += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        
        # hash index
        index = self.hash_index(key)
        # if sotrage is not empty
        if self.storage[index] is not None:
            # if the hashed key is found in index 0
            if self.storage[index] == key:
                return 
            else:
                node = self.storage[index]
                # while array is not empty
                while node is None and node.key != key:
                    # pointer to to prev node
                    prev = node
                    node = node.next
                    # if node is empty
                    if node is None:
                        return 
                    # else node is not empty
                    else:
                        self.nums -= 1
                        result = node.value
                    if prev is None:
                        node = None
                    else:
                        prev.next = node.next.next
                    return result
        else:
            print("WARNING: key not found!")
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # hash index
        index = self.hash_index(key)
        node = self.storage[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        curr = None
        
        for item in old_storage:
            curr = item
            while curr is not None:
                self.put(curr.key, curr.value)
                curr = curr.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
