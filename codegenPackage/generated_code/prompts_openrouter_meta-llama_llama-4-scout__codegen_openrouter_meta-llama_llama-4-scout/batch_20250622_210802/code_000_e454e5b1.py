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
 * A Stack implementation using a linked list in Java.
 * 
 * @author [Your Name]
 * @version 1.0
 */
public class StackUsingLinkedList {

    /**
     * Node class representing each element in the linked list.
     */
    private static class Node {
        int data;
        Node next;

        /**
         * Constructor to initialize a new node with given data.
         * 
         * @param data the data to be stored in the node
         */
        public Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    /**
     * Top of the stack.
     */
    private Node top;

    /**
     * Size of the stack.
     */
    private int size;

    /**
     * Constructor to initialize an empty stack.
     */
    public StackUsingLinkedList() {
        top = null;
        size = 0;
    }

    /**
     * Pushes an element onto the stack.
     * 
     * @param data the element to be pushed
     */
    public void push(int data) {
        Node newNode = new Node(data);
        if (top == null) {
            top = newNode;
        } else {
            newNode.next = top;
            top = newNode;
        }
        size++;
    }

    /**
     * Pops the top element from the stack.
     * 
     * @return the popped element, or throws an exception if the stack is empty
     * @throws RuntimeException if the stack is empty
     */
    public int pop() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        int data = top.data;
        top = top.next;
        size--;
        return data;
    }

    /**
     * Peeks at the top element of the stack without removing it.
     * 
     * @return the top element, or throws an exception if the stack is empty
     * @throws RuntimeException if the stack is empty
     */
    public int peek() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return top.data;
    }

    /**
     * Checks if the stack is empty.
     * 
     * @return true if the stack is empty, false otherwise
     */
    public boolean isEmpty() {
        return top == null;
    }

    /**
     * Returns the size of the stack.
     * 
     * @return the number of elements in the stack
     */
    public int size() {
        return size;
    }

    public static void main(String[] args) {
        StackUsingLinkedList stack = new StackUsingLinkedList();

        // Push elements onto the stack
        stack.push(10);
        stack.push(20);
        stack.push(30);

        // Print stack size
        System.out.println("Stack size: " + stack.size()); // Output: 3

        // Peek at the top element
        System.out.println("Top element: " + stack.peek()); // Output: 30

        // Pop elements from the stack
        System.out.println("Popped element: " + stack.pop()); // Output: 30
        System.out.println("Popped element: " + stack.pop()); // Output: 20

        // Check if the stack is empty
        System.out.println("Is stack empty? " + stack.isEmpty()); // Output: false

        // Pop the last element
        System.out.println("Popped element: " + stack.pop()); // Output: 10

        // Check if the stack is empty
        System.out.println("Is stack empty? " + stack.isEmpty()); // Output: true

        // Attempt to pop from an empty stack
        try {
            stack.pop();
        } catch (RuntimeException e) {
            System.out.println("Error: " + e.getMessage()); // Output: Error: Stack is empty
        }
    }
}
```
