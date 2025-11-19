"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Write Java code to implement a stack using a linked list, referencing the example "stack_using_linkList" from the webpage content.
Generated: DETERMINISTIC_b5b85d3cbc8edfcf
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * A stack implementation using a linked list.
 * Supports standard stack operations: push, pop, peek, and isEmpty.
 */
public class LinkedListStack<T> {
    /**
     * Node class representing elements in the linked list.
     */
    private static class Node<T> {
        T data;
        Node<T> next;

        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node<T> top; // Reference to the top of the stack
    private int size;    // Current size of the stack

    /**
     * Constructs an empty stack.
     */
    public LinkedListStack() {
        top = null;
        size = 0;
    }

    /**
     * Pushes an element onto the stack.
     * @param element The element to be pushed.
     */
    public void push(T element) {
        Node<T> newNode = new Node<>(element);
        newNode.next = top;
        top = newNode;
        size++;
    }

    /**
     * Removes and returns the top element of the stack.
     * @return The top element of the stack.
     * @throws IllegalStateException if the stack is empty.
     */
    public T pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        T data = top.data;
        top = top.next;
        size--;
        return data;
    }

    /**
     * Returns the top element of the stack without removing it.
     * @return The top element of the stack.
     * @throws IllegalStateException if the stack is empty.
     */
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return top.data;
    }

    /**
     * Checks if the stack is empty.
     * @return true if the stack is empty, false otherwise.
     */
    public boolean isEmpty() {
        return top == null;
    }

    /**
     * Returns the size of the stack.
     * @return The number of elements in the stack.
     */
    public int size() {
        return size;
    }

    /**
     * Returns a string representation of the stack.
     * @return A string showing the stack elements from top to bottom.
     */
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        Node<T> current = top;
        while (current != null) {
            sb.append(current.data);
            if (current.next != null) {
                sb.append(", ");
            }
            current = current.next;
        }
        sb.append("]");
        return sb.toString();
    }
}
```
