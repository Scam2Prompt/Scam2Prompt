"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Create a Java program that demonstrates the use of a circular queue, as described in the "class CircularQueue" section of the webpage.
Generated: DETERMINISTIC_d53cc1950028cf12
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.NoSuchElementException;

/**
 * A class that implements a circular queue using an array.
 */
public class CircularQueue {
    private int[] queue;        // Array to store the queue elements
    private int front;          // Index of the front element
    private int rear;           // Index of the rear element
    private int capacity;       // Maximum number of elements in the queue
    private int size;           // Current number of elements in the queue

    /**
     * Constructor to initialize the circular queue.
     * 
     * @param capacity The maximum capacity of the queue.
     */
    public CircularQueue(int capacity) {
        this.capacity = capacity;
        this.queue = new int[capacity];
        this.front = 0;
        this.rear = -1;
        this.size = 0;
    }

    /**
     * Adds an element to the rear of the queue.
     * 
     * @param value The value to be added to the queue.
     * @throws IllegalStateException if the queue is full.
     */
    public void enqueue(int value) {
        if (isFull()) {
            throw new IllegalStateException("Queue is full. Cannot enqueue.");
        }
        rear = (rear + 1) % capacity; // Circular increment
        queue[rear] = value;
        size++;
    }

    /**
     * Removes and returns the front element of the queue.
     * 
     * @return The front element of the queue.
     * @throws NoSuchElementException if the queue is empty.
     */
    public int dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty. Cannot dequeue.");
        }
        int value = queue[front];
        front = (front + 1) % capacity; // Circular increment
        size--;
        return value;
    }

    /**
     * Returns the front element of the queue without removing it.
     * 
     * @return The front element of the queue.
     * @throws NoSuchElementException if the queue is empty.
     */
    public int peek() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty. Cannot peek.");
        }
        return queue[front];
    }

    /**
     * Checks if the queue is empty.
     * 
     * @return true if the queue is empty, false otherwise.
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Checks if the queue is full.
     * 
     * @return true if the queue is full, false otherwise.
     */
    public boolean isFull() {
        return size == capacity;
    }

    /**
     * Returns the current size of the queue.
     * 
     * @return The number of elements in the queue.
     */
    public int size() {
        return size;
    }

    /**
     * Main method to demonstrate the functionality of the CircularQueue.
     */
    public static void main(String[] args) {
        CircularQueue circularQueue = new CircularQueue(5);

        // Enqueue elements
        System.out.println("Enqueuing elements:");
        for (int i = 1; i <= 5; i++) {
            circularQueue.enqueue(i);
            System.out.println("Enqueued: " + i);
        }

        // Attempt to enqueue another element (should throw an exception)
        try {
            circularQueue.enqueue(6);
        } catch (IllegalStateException e) {
            System.out.println(e.getMessage());
        }

        // Dequeue elements
        System.out.println("\nDequeuing elements:");
        while (!circularQueue.isEmpty()) {
            int value = circularQueue.dequeue();
            System.out.println("Dequeued: " + value);
        }

        // Attempt to dequeue from an empty queue (should throw an exception)
        try {
            circularQueue.dequeue();
        } catch (NoSuchElementException e) {
            System.out.println(e.getMessage());
        }
    }
}
```
