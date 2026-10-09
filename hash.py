#[1] creating the class
class HashTable:
    #[2] initializing the parameters
    def __init__(self):
        self.collection = {
        }
    #[3] adding the methods hash, add, remove and lookup
    def hash(self, data: str):
        return sum(ord(c) for c in data)
    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        self.collection[hashed_key][key] = value
    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]
            if not self.collection[hashed_key]:
                del self.collection[hashed_key]
    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        else: return None

#[4] our testing data

ht = HashTable()

print("--- 1. Testing Hashing ---")
print("Hash of 'golf':", ht.hash('golf'))  
print("Hash of 'dear':", ht.hash('dear'))  
print("Hash of 'read':", ht.hash('read'))  

print("\n--- 2. Testing Add ---")
ht.add('golf', 'sport')
ht.add('dear', 'friend')
ht.add('read', 'book') 
print("Collection state:", ht.collection)

print("\n--- 3. Testing Lookup ---")
print("Lookup 'golf':", ht.lookup('golf'))      
print("Lookup 'dear':", ht.lookup('dear'))      
print("Lookup 'read':", ht.lookup('read'))      
print("Lookup 'apple':", ht.lookup('apple'))    

print("\n--- 4. Testing Remove ---")
ht.remove('dear')
print("Lookup 'dear' after removal:", ht.lookup('dear'))  
print("Lookup 'read' after removing 'dear':", ht.lookup('read'))  

ht.remove('non_existent_key')
print("\nFinal Collection state:", ht.collection)