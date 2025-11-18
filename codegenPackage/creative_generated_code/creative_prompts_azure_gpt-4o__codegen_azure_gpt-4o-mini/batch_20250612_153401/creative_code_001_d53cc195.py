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
import java.util.Arrays;

/**
 * A class that implements a circular queue using an array.
 */
public class CircularQueue {
    private int[] queue;        // Array to store queue elements
    private int front;          // Index of the front element
    private int rear;           // Index of the last element
    private int capacity;       // Maximum number of elements in the queue
    private int size;           // Current number of elements in the queue

    /**
     * Constructor to initialize the circular queue.
     * @param capacity the maximum size of the queue.
     */
    public CircularQueue(int capacity) {
        this.capacity = capacity;
        this.queue = new int[capacity];
        this.front = 0;
        this.rear = -1;
        this.size = 0;
    }

    /**
     * Adds an item to the circular queue.
     * @param item the item to be added.
     * @throws IllegalStateException if the queue is full.
     */
    public void enqueue(int item) {
        if (isFull()) {
            throw new IllegalStateException("Queue is full. Cannot enqueue element: " + item);
        }
        rear = (rear + 1) % capacity; // Wrap around if needed
        queue[rear] = item;            // Insert the new element
        size++;
    }

    /**
     * Removes and returns the front item from the circular queue.
     * @return the front item.
     * @throws IllegalStateException if the queue is empty.
     */
    public int dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty. Cannot dequeue element.");
        }
        int item = queue[front];      // Get the front element
        front = (front + 1) % capacity; // Wrap around if needed
        size--;
        return item;                  // Return the dequeued element
    }

    /**
     * Checks if the circular queue is empty.
     * @return true if the queue is empty, false otherwise.
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Checks if the circular queue is full.
     * @return true if the queue is full, false otherwise.
     */
    public boolean isFull() {
        return size == capacity;
    }

    /**
     * Returns the number of elements in the circular queue.
     * @return the current size of the queue.
     */
    public int size() {
        return size;
    }

    /**
     * Displays the elements of the circular queue.
     * @return a string representation of the queue elements.
     */
    public String display() {
        StringBuilder sb = new StringBuilder("Circular Queue: ");
        for (int i = 0; i < size; i++) {
            sb.append(queue[(front + i) % capacity]).append(" ");
        }
        return sb.toString().trim();
    }

    /**
     * Main method to demonstrate the functionality of the CircularQueue.
     * @param args command line arguments.
     */
    public static void main(String[] args) {
        CircularQueue circularQueue = new CircularQueue(5);
        
        try {
            circularQueue.enqueue(10);
            circularQueue.enqueue(20);
            circularQueue.enqueue(30);
            circularQueue.enqueue(40);
            circularQueue.enqueue(50);

            System.out.println(circularQueue.display());
            
            System.out.println("Dequeued: " + circularQueue.dequeue());
            System.out.println("Dequeued: " + circularQueue.dequeue());
            
            circularQueue.enqueue(60);
            System.out.println(circularQueue.display());

            System.out.println("Queue Size: " + circularQueue.size());
        } catch (IllegalStateException e) {
            System.err.println(e.getMessage());
        }
    }
}
```
