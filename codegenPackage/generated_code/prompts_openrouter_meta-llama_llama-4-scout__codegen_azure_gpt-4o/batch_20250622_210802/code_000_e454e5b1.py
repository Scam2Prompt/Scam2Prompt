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
// Java implementation of a Stack using a linked list
public class StackUsingLinkedList {

    // Node class representing each element in the stack
    private static class Node {
        int data; // Data stored in the node
        Node next; // Reference to the next node

        // Constructor to initialize a node
        public Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    // Top of the stack
    private Node top;

    // Constructor to initialize an empty stack
    public StackUsingLinkedList() {
        this.top = null;
    }

    /**
     * Pushes an element onto the stack.
     * @param data The data to be pushed onto the stack.
     */
    public void push(int data) {
        Node newNode = new Node(data); // Create a new node
        newNode.next = top; // Link the new node to the current top
        top = newNode; // Update the top to the new node
    }

    /**
     * Removes and returns the top element of the stack.
     * @return The data of the top element.
     * @throws IllegalStateException if the stack is empty.
     */
    public int pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty. Cannot pop.");
        }
        int poppedData = top.data; // Get the data from the top node
        top = top.next; // Update the top to the next node
        return poppedData; // Return the popped data
    }

    /**
     * Returns the top element of the stack without removing it.
     * @return The data of the top element.
     * @throws IllegalStateException if the stack is empty.
     */
    public int peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty. Cannot peek.");
        }
        return top.data; // Return the data of the top node
    }

    /**
     * Checks if the stack is empty.
     * @return True if the stack is empty, false otherwise.
     */
    public boolean isEmpty() {
        return top == null; // Stack is empty if top is null
    }

    /**
     * Prints the elements of the stack from top to bottom.
     */
    public void printStack() {
        if (isEmpty()) {
            System.out.println("Stack is empty.");
            return;
        }
        Node current = top; // Start from the top
        System.out.print("Stack elements: ");
        while (current != null) {
            System.out.print(current.data + " "); // Print the data
            current = current.next; // Move to the next node
        }
        System.out.println(); // New line after printing all elements
    }

    // Main method for testing the stack implementation
    public static void main(String[] args) {
        StackUsingLinkedList stack = new StackUsingLinkedList();

        // Push elements onto the stack
        stack.push(10);
        stack.push(20);
        stack.push(30);

        // Print the stack
        stack.printStack();

        // Peek the top element
        System.out.println("Top element: " + stack.peek());

        // Pop elements from the stack
        System.out.println("Popped element: " + stack.pop());
        System.out.println("Popped element: " + stack.pop());

        // Print the stack after popping
        stack.printStack();

        // Check if the stack is empty
        System.out.println("Is stack empty? " + stack.isEmpty());
    }
}
```
