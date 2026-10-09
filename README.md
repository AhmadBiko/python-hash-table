# Python Hash Table 🗂️⚡

An Object-Oriented Python application implementing a custom Hash Table data structure that manages key-value pairs, computes ASCII/Unicode hash values, and resolves collisions using nested dictionaries.

## 🛠️ Technologies Used
- **Python:** Core data structure logic, iteration, and character encoding conversions (`ord()`).
- **Object-Oriented Programming (OOP):** Encapsulates storage attributes, mathematical hashing, lookup mechanics, and collision resolution into a cohesive class architecture.

## 🗂️ Project Structure
- **`main.py`**: The main executable script containing the `HashTable` class definition, core methods (`hash`, `add`, `remove`, `lookup`), and comprehensive test verification logic.

## 📊 Class Architecture & Core Methods
The entire system is managed by a primary class:
- **`HashTable`**: Manages the underlying `collection` storage dictionary. Computes integer hash indices using character Unicode summation and stores items in nested sub-dictionaries to cleanly handle collisions.

### Key Methods:
- **`hash(data)`**: Iterates over a string input and sums the Unicode/ASCII values of each character via `ord()` to generate a numeric index.
- **`add(key, value)`**: Hashes the provided key, initializes a sub-dictionary at that hash index if it doesn't already exist, and stores/updates the key-value pair inside it.
- **`lookup(key)`**: Searches for a key within its corresponding hash bucket and returns its associated value if present, or `None` if it does not exist.
- **`remove(key)`**: Deletes a specific key-value pair from its hash bucket without raising errors if the key isn't found and without destroying neighboring collided entries.

## 🚀 How to Run
1. Run the script in your terminal:
   ```bash
   python hash.py
