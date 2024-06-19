class MyHashSet:
    def __init__(self):
        self.primary = 1000
        self.secondary = 1000
        self.storage = [None] * self.primary

    def _hash1(self, key: int) -> int:
        return key % self.primary

    def _hash2(self, key: int) -> int:
        return key // self.secondary

    def add(self, key: int) -> None:
        bucket = self._hash1(key)
        bucketItem = self._hash2(key)
        if self.storage[bucket] is None:
            if bucket == 0:
                self.storage[bucket] = [False] * (self.secondary + 1)
            else:
                self.storage[bucket] = [False] * self.secondary
        self.storage[bucket][bucketItem] = True

    def remove(self, key: int) -> None:
        bucket = self._hash1(key)
        bucketItem = self._hash2(key)
        if self.storage[bucket] is not None:
            self.storage[bucket][bucketItem] = False

    def contains(self, key: int) -> bool:
        bucket = self._hash1(key)
        bucketItem = self._hash2(key)
        return self.storage[bucket] is not None and self.storage[bucket][bucketItem]




