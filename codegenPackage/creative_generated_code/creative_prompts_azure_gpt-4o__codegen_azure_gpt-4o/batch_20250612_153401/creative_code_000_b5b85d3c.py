"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lklklk.netlify.app
Prompt: Write Java code to implement a stack using a linked list, referencing the example "stack_using_linkList" from the webpage content.
Generated: DETERMINISTIC_b5b85d3cbc8edfcf
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
// Package declaration (modify according to your project structure)
// package com.example.datastructures;

import java.util.EmptyStackException;

/**
 * A generic Stack implementation using a singly linked list.
 *
 * @param <T> The type of elements held in the stack.
 */
public class StackUsingLinkedList<T> {

    // Node class to represent each element in the stack.
    private static class Node<T> {
        T data;
        Node<T> next;

        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    // Top pointer for the stack.
    private Node<T> top;

    // Size of the stack.
    private int size;

    /**
     * Constructor initializes an empty stack.
     */
    public StackUsingLinkedList() {
        this.top = null;
        this.size = 0;
    }

    /**
     * Push an element onto the stack.
     *
     * @param data The element to be pushed.
     */
    public void push(T data) {
        Node<T> newNode = new Node<>(data);
        newNode.next = top; // Point the new node to the current top.
        top = newNode; // Update the top pointer.
        size++; // Increment the stack size.
    }

    /**
     * Pop an element from the stack.
     *
     * @return The popped element.
     * @throws EmptyStackException If the stack is empty.
     */
    public T pop() {
        if (isEmpty()) {
            throw new EmptyStackException(); // Throw exception if stack is empty.
        }
        T data = top.data; // Get the data from the top node.
        top = top.next; // Move the top pointer to the next node.
        size--; // Decrement the stack size.
        return data;
    }

    /**
     * Peek at the top element of the stack without removing it.
     *
     * @return The top element.
     * @throws EmptyStackException If the stack is empty.
     */
    public T peek() {
        if (isEmpty()) {
            throw new EmptyStackException(); // Throw exception if stack is empty.
        }
        return top.data; // Return the data of the top node.
    }

    /**
     * Check if the stack is empty.
     *
     * @return true if the stack is empty, false otherwise.
     */
    public boolean isEmpty() {
        return top == null; // Stack is empty if top is null.
    }

    /**
     * Get the size of the stack.
     *
     * @return The number of elements in the stack.
     */
    public int size() {
        return size;
    }

    /**
     * Clear the stack by resetting the top pointer and size.
     */
    public void clear() {
        top = null; // Remove all references to nodes.
        size = 0; // Reset size to zero.
    }

    /**
     * Main method for testing the stack implementation.
     */
    public static void main(String[] args) {
        StackUsingLinkedList<Integer> stack = new StackUsingLinkedList<>();

        // Push elements onto the stack.
        stack.push(10);
        stack.push(20);
        stack.push(30);

        // Display the top element using peek.
        System.out.println("Top element: " + stack.peek()); // Output: 30

        // Pop elements from the stack.
        System.out.println("Popped element: " + stack.pop()); // Output: 30
        System.out.println("Popped element: " + stack.pop()); // Output: 20

        // Check the size of the stack.
        System.out.println("Stack size: " + stack.size()); // Output: 1

        // Clear the stack.
        stack.clear();
        System.out.println("Is stack empty after clearing? " + stack.isEmpty()); // Output: true
    }
}
```
