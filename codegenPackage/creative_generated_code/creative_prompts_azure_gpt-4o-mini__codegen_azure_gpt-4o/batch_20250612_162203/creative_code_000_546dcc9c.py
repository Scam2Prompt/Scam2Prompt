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
// Stack implementation using a Linked List in Java
public class LinkedListStack {

    // Node class representing each element in the stack
    private static class Node {
        int data; // Value stored in the node
        Node next; // Reference to the next node

        // Constructor to initialize the node
        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    // Top of the stack
    private Node top;

    // Constructor to initialize an empty stack
    public LinkedListStack() {
        this.top = null;
    }

    // Push method to add an element to the stack
    public void push(int data) {
        Node newNode = new Node(data); // Create a new node
        newNode.next = top; // Link the new node to the current top
        top = newNode; // Set the new node as the top
    }

    // Pop method to remove the top element from the stack
    public int pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack underflow: Attempted to pop from an empty stack.");
        }
        int poppedData = top.data; // Get the data of the top node
        top = top.next; // Move top to the next node
        return poppedData; // Return the popped data
    }

    // Peek method to view the top element of the stack without removing it
    public int peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty: Cannot peek.");
        }
        return top.data; // Return the data of the top node
    }

    // Method to check if the stack is empty
    public boolean isEmpty() {
        return top == null; // Return true if top is null
    }

    // Method to display the stack elements (for debugging/visualization)
    public void display() {
        if (isEmpty()) {
            System.out.println("Stack is empty.");
            return;
        }
        Node current = top;
        System.out.print("Stack elements: ");
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    // Main method to test the LinkedListStack class
    public static void main(String[] args) {
        LinkedListStack stack = new LinkedListStack();

        // Test pushing elements onto the stack
        stack.push(10);
        stack.push(20);
        stack.push(30);

        // Display the stack
        stack.display();

        // Test peeking the top element
        System.out.println("Top element: " + stack.peek());

        // Test popping elements from the stack
        System.out.println("Popped element: " + stack.pop());
        System.out.println("Popped element: " + stack.pop());

        // Display the stack after popping
        stack.display();

        // Test popping the last element
        System.out.println("Popped element: " + stack.pop());

        // Check if the stack is empty
        System.out.println("Is stack empty? " + stack.isEmpty());
    }
}
```
