"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lklklk.netlify.app
Prompt: Create a Java program that demonstrates the use of a circular queue, as described in the "class CircularQueue" section of the webpage.
Generated: DETERMINISTIC_d53cc1950028cf12
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.NoSuchElementException;

/**
 * A class that implements a circular queue data structure in Java
 */
public class CircularQueue {
    private int[] queue; // Array to store queue elements
    private int front;   // Index of the front element
    private int rear;    // Index of the last element
    private int size;    // Current size of the queue
    private int capacity; // Maximum capacity of the queue

    /**
     * Constructor to initialize the circular queue
     * @param capacity The maximum number of elements the circular queue can hold
     */
    public CircularQueue(int capacity) {
        if (capacity <= 0) {
            throw new IllegalArgumentException("Queue capacity must be greater than 0");
        }
        this.capacity = capacity;
        this.queue = new int[capacity];
        this.front = -1; // Initialize as empty
        this.rear = -1;  // Initialize as empty
        this.size = 0;   // Empty queue has size 0
    }

    /**
     * Adds an element to the circular queue
     * @param element The element to be added
     * @throws IllegalStateException if the queue is full
     */
    public void enqueue(int element) {
        if (isFull()) {
            throw new IllegalStateException("Queue is full");
        }
        if (isEmpty()) {
            front = 0; // First element sets front to 0
        }
        rear = (rear + 1) % capacity; // Move rear to the next position circularly
        queue[rear] = element;
        size++;
    }

    /**
     * Removes and returns the front element of the circular queue
     * @return The element that was removed
     * @throws NoSuchElementException if the queue is empty
     */
    public int dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty");
        }
        int removedElement = queue[front];
        front = (front + 1) % capacity; // Move front to the next position circularly
        size--;
        // Reset front and rear if the queue becomes empty
        if (isEmpty()) {
            front = -1;
            rear = -1;
        }
        return removedElement;
    }

    /**
     * Returns the front element of the circular queue without removing it
     * @return The front element
     * @throws NoSuchElementException if the queue is empty
     */
    public int peek() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty");
        }
        return queue[front];
    }

    /**
     * Returns true if the circular queue is empty
     * @return true if the queue is empty, false otherwise
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Returns true if the circular queue is full
     * @return true if the queue is full, false otherwise
     */
    public boolean isFull() {
        return size == capacity;
    }

    /**
     * Returns the current size of the circular queue
     * @return The number of elements in the queue
     */
    public int getSize() {
        return size;
    }

    /**
     * A simple main method to demonstrate the usage of the CircularQueue class
     */
    public static void main(String[] args) {
        try {
            CircularQueue queue = new CircularQueue(5);

            // Enqueue elements
            queue.enqueue(10);
            queue.enqueue(20);
            queue.enqueue(30);
            queue.enqueue(40);
            queue.enqueue(50);

            System.out.println("Front element: " + queue.peek()); // Output: 10

            // Dequeue elements
            System.out.println("Dequeued element: " + queue.dequeue()); // Output: 10
            System.out.println("Dequeued element: " + queue.dequeue()); // Output: 20

            // Enqueue more elements to show circular behavior
            queue.enqueue(60);
            queue.enqueue(70);

            // Display all elements in the queue
            while (!queue.isEmpty()) {
                System.out.println("Dequeued element: " + queue.dequeue());
            }
        } catch (Exception ex) {
            System.err.println("Error: " + ex.getMessage());
        }
    }
}
```
