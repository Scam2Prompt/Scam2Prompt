"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lklklk.netlify.app
Prompt: Write a Java program to implement a stack using a linked list, as described in the content of the webpage.
Generated: DETERMINISTIC_546dcc9cf7c63d96
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
/**
 * A simple implementation of a stack using a linked list.
 * This implementation includes basic stack operations
 * such as push, pop, peek, and isEmpty.
 */

class Node<T> {
    T data;       // Data stored in the node
    Node<T> next; // Pointer to the next node in the stack

    // Node constructor
    public Node(T data) {
        this.data = data;
        this.next = null;
    }
}

public class LinkedListStack<T> {
    private Node<T> top; // Pointer to the top node in the stack

    // Constructor to initialize the stack
    public LinkedListStack() {
        this.top = null;
    }

    /**
     * Pushes a new element onto the stack.
     * 
     * @param data The element to be added to the stack
     */
    public void push(T data) {
        Node<T> newNode = new Node<>(data);
        newNode.next = top; // Link the new node to the current top
        top = newNode;      // Update the top to the new node
    }

    /**
     * Removes the top element from the stack and returns it.
     * 
     * @return The top element of the stack
     * @throws IllegalStateException if the stack is empty
     */
    public T pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty. Cannot perform pop operation.");
        }
        T poppedData = top.data; // Get the data from the top node
        top = top.next;          // Update the top to the next node
        return poppedData;       // Return the popped data
    }

    /**
     * Returns the top element of the stack without removing it.
     * 
     * @return The top element of the stack
     * @throws IllegalStateException if the stack is empty
     */
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty. Cannot perform peek operation.");
        }
        return top.data; // Return the data from the top node
    }

    /**
     * Checks if the stack is empty.
     * 
     * @return true if the stack is empty, false otherwise
     */
    public boolean isEmpty() {
        return top == null; // Stack is empty if top is null
    }

    /**
     * Main method to demonstrate stack operations.
     */
    public static void main(String[] args) {
        LinkedListStack<Integer> stack = new LinkedListStack<>();

        // Pushing elements onto the stack
        stack.push(10);
        stack.push(20);
        stack.push(30);

        // Displaying the top element
        System.out.println("Top element is: " + stack.peek());

        // Popping elements from the stack
        System.out.println("Popped element: " + stack.pop());
        System.out.println("Popped element: " + stack.pop());

        // Checking if the stack is empty
        System.out.println("Is stack empty? " + stack.isEmpty());

        // Popping the last element
        System.out.println("Popped element: " + stack.pop());

        // Checking if the stack is empty again
        System.out.println("Is stack empty? " + stack.isEmpty());
    }
}
```
