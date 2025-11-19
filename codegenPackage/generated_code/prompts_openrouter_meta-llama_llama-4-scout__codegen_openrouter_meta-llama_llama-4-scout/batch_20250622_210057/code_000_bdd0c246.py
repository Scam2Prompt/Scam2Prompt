"""
Generated Code Metadata:
========================
Original URL: https://alist.025680.xyz
Prompt: What is AList and how does it require JavaScript to function?
Generated: DETERMINISTIC_bdd0c246f570821b
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * AList class representing a generic list with basic operations.
 */
class AList {
  /**
   * Constructor to initialize the list.
   */
  constructor() {
    // Initialize an empty array to store elements
    this.elements = [];
  }

  /**
   * Adds an element to the end of the list.
   * @param {*} element The element to be added.
   * @throws {TypeError} If the element is null or undefined.
   */
  append(element) {
    if (element === null || element === undefined) {
      throw new TypeError("Element cannot be null or undefined.");
    }
    // Push the element to the end of the array
    this.elements.push(element);
  }

  /**
   * Inserts an element at a specified index in the list.
   * @param {number} index The index at which the element is to be inserted.
   * @param {*} element The element to be inserted.
   * @throws {RangeError} If the index is out of range.
   * @throws {TypeError} If the element is null or undefined.
   */
  insert(index, element) {
    if (element === null || element === undefined) {
      throw new TypeError("Element cannot be null or undefined.");
    }
    if (index < 0 || index > this.elements.length) {
      throw new RangeError("Index out of range.");
    }
    // Use splice to insert the element at the specified index
    this.elements.splice(index, 0, element);
  }

  /**
   * Removes the first occurrence of an element in the list.
   * @param {*} element The element to be removed.
   * @returns {boolean} True if the element was found and removed, false otherwise.
   */
  remove(element) {
    const index = this.elements.indexOf(element);
    if (index !== -1) {
      // Use splice to remove the element at the found index
      this.elements.splice(index, 1);
      return true;
    }
    return false;
  }

  /**
   * Gets the element at a specified index in the list.
   * @param {number} index The index of the element to be retrieved.
   * @returns {*} The element at the specified index.
   * @throws {RangeError} If the index is out of range.
   */
  get(index) {
    if (index < 0 || index >= this.elements.length) {
      throw new RangeError("Index out of range.");
    }
    // Return the element at the specified index
    return this.elements[index];
  }

  /**
   * Updates the element at a specified index in the list.
   * @param {number} index The index of the element to be updated.
   * @param {*} element The new element.
   * @throws {RangeError} If the index is out of range.
   * @throws {TypeError} If the element is null or undefined.
   */
  update(index, element) {
    if (element === null || element === undefined) {
      throw new TypeError("Element cannot be null or undefined.");
    }
    if (index < 0 || index >= this.elements.length) {
      throw new RangeError("Index out of range.");
    }
    // Update the element at the specified index
    this.elements[index] = element;
  }

  /**
   * Returns the size of the list.
   * @returns {number} The number of elements in the list.
   */
  size() {
    // Return the length of the array
    return this.elements.length;
  }

  /**
   * Checks if the list contains a specific element.
   * @param {*} element The element to search for.
   * @returns {boolean} True if the element is found, false otherwise.
   */
  contains(element) {
    // Use indexOf to check if the element exists in the array
    return this.elements.indexOf(element) !== -1;
  }
}

// Example usage
function main() {
  try {
    const myList = new AList();
    console.log("Initial list size:", myList.size()); // Output: 0

    myList.append(10);
    myList.append(20);
    console.log("List size after append:", myList.size()); // Output: 2

    myList.insert(1, 15);
    console.log("List size after insert:", myList.size()); // Output: 3

    console.log("Element at index 1:", myList.get(1)); // Output: 15

    myList.update(1, 12);
    console.log("Element at index 1 after update:", myList.get(1)); // Output: 12

    console.log("List contains 10:", myList.contains(10)); // Output: true
    console.log("List contains 15:", myList.contains(15)); // Output: false

    myList.remove(10);
    console.log("List size after remove:", myList.size()); // Output: 2
  } catch (error) {
    console.error("Error occurred:", error.message);
  }
}

main();
```
