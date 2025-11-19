"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Write a Java implementation of a Stack using a linked list, similar to the `stack_using_linkList` example provided.
Generated: DETERMINISTIC_e454e5b1425b3fc8
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * A simple implementation of a Stack using a singly linked list.
 * This stack supports basic operations: push, pop, peek, and isEmpty.
 */
public class LinkedListStack<T> {
    
    // Node class representing each element in the stack
    private static class Node<T> {
        T data; // Data stored in the node
        Node<T> next; // Reference to the next node in the stack

        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node<T> top; // Reference to the top node of the stack
    private int size; // Size of the stack

    // Constructor to initialize an empty stack
    public LinkedListStack() {
        this.top = null;
        this.size = 0;
    }

    /**
     * Pushes an element onto the top of the stack.
     * 
     * @param item The item to be pushed onto the stack
     */
    public void push(T item) {
        Node<T> newNode = new Node<>(item); // Create a new node
        newNode.next = top; // Link the new node to the previous top
        top = newNode; // Update the top to the new node
        size++; // Increment the size of the stack
    }

    /**
     * Removes and returns the top element of the stack.
     * 
     * @return The top element of the stack
     * @throws IllegalStateException if the stack is empty
     */
    public T pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty. Cannot pop.");
        }
        T item = top.data; // Get the data from the top node
        top = top.next; // Update the top to the next node
        size--; // Decrement the size of the stack
        return item; // Return the popped item
    }

    /**
     * Returns the top element of the stack without removing it.
     * 
     * @return The top element of the stack
     * @throws IllegalStateException if the stack is empty
     */
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty. Cannot peek.");
        }
        return top.data; // Return the data from the top node
    }

    /**
     * Checks if the stack is empty.
     * 
     * @return true if the stack is empty, false otherwise
     */
    public boolean isEmpty() {
        return size == 0; // Return true if size is 0
    }

    /**
     * Returns the current size of the stack.
     * 
     * @return The number of elements in the stack
     */
    public int size() {
        return size; // Return the size of the stack
    }

    /**
     * Main method for testing the LinkedListStack implementation.
     */
    public static void main(String[] args) {
        LinkedListStack<Integer> stack = new LinkedListStack<>();

        // Push elements onto the stack
        stack.push(10);
        stack.push(20);
        stack.push(30);

        // Peek at the top element
        System.out.println("Top element: " + stack.peek()); // Should print 30

        // Pop elements from the stack
        System.out.println("Popped element: " + stack.pop()); // Should print 30
        System.out.println("Popped element: " + stack.pop()); // Should print 20

        // Check if the stack is empty
        System.out.println("Is stack empty? " + stack.isEmpty()); // Should print false

        // Pop the last element
        System.out.println("Popped element: " + stack.pop()); // Should print 10

        // Check if the stack is empty again
        System.out.println("Is stack empty? " + stack.isEmpty()); // Should print true
    }
}
```
