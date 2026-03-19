class HashTable:
    """
    Hash Table implementation using chaining for collision resolution.
    Each bucket stores a list of (key, value) pairs.
    """

    def __init__(self, size=10):
        # Initialize hash table with given size
        self.size = size
        self.table = [[] for _ in range(size)]  # List of buckets (chains)
        self.count = 0  # Number of elements stored

    def hash_function(self, key):
        """
        Computes index for a given key using Python's built-in hash function.
        Modulo operation ensures index stays within table size.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.
        If key already exists, update its value.
        """

        index = self.hash_function(key)
        bucket = self.table[index]

        # Check if key already exists → update value
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # If key not found → append new key-value pair
        bucket.append((key, value))
        self.count += 1

        # Resize table if load factor exceeds threshold (0.75)
        if self.count / self.size > 0.75:
            self.resize()

    def search(self, key):
        """
        Searches for a key in the hash table.
        Returns the associated value if found, else returns None.
        """

        index = self.hash_function(key)
        bucket = self.table[index]

        # Traverse the chain to find key
        for k, v in bucket:
            if k == key:
                return v

        return None  # Key not found

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table.
        Returns True if deletion is successful, else False.
        """

        index = self.hash_function(key)
        bucket = self.table[index]

        # Search for key and remove it
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True

        return False  # Key not found

    def resize(self):
        """
        Doubles the size of the hash table and rehashes all elements.
        This helps maintain a low load factor and improves performance.
        """

        new_size = self.size * 2
        new_table = HashTable(new_size)

        # Reinsert all existing elements into new table
        for bucket in self.table:
            for k, v in bucket:
                new_table.insert(k, v)

        # Update current table to new table
        self.size = new_table.size
        self.table = new_table.table