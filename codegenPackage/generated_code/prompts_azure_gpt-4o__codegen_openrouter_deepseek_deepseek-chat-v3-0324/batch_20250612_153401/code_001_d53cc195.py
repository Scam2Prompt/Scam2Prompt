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
/**
 * A class representing a circular queue data structure.
 * The circular queue avoids the problem of unused space in a linear queue implementation.
 */
public class CircularQueue {
    private int[] queue;
    private int front;
    private int rear;
    private int size;
    private int capacity;

    /**
     * Constructor to initialize the circular queue with a given capacity.
     * @param capacity The maximum number of elements the queue can hold.
     */
    public CircularQueue(int capacity) {
        this.capacity = capacity;
        this.queue = new int[capacity];
        this.front = -1;
        this.rear = -1;
        this.size = 0;
    }

    /**
     * Checks if the queue is empty.
     * @return true if the queue is empty, false otherwise.
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Checks if the queue is full.
     * @return true if the queue is full, false otherwise.
     */
    public boolean isFull() {
        return size == capacity;
    }

    /**
     * Adds an element to the rear of the queue.
     * @param item The element to be added.
     * @throws IllegalStateException if the queue is full.
     */
    public void enqueue(int item) {
        if (isFull()) {
            throw new IllegalStateException("Queue is full. Cannot enqueue.");
        }
        if (isEmpty()) {
            front = 0;
        }
        rear = (rear + 1) % capacity;
        queue[rear] = item;
        size++;
    }

    /**
     * Removes and returns the element at the front of the queue.
     * @return The element at the front of the queue.
     * @throws IllegalStateException if the queue is empty.
     */
    public int dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty. Cannot dequeue.");
        }
        int item = queue[front];
        if (front == rear) {
            front = -1;
            rear = -1;
        } else {
            front = (front + 1) % capacity;
        }
        size--;
        return item;
    }

    /**
     * Returns the element at the front of the queue without removing it.
     * @return The element at the front of the queue.
     * @throws IllegalStateException if the queue is empty.
     */
    public int peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty. Cannot peek.");
        }
        return queue[front];
    }

    /**
     * Returns the current size of the queue.
     * @return The number of elements in the queue.
     */
    public int size() {
        return size;
    }

    /**
     * Displays the elements of the queue.
     */
    public void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty.");
            return;
        }
        System.out.print("Queue: ");
        int i = front;
        do {
            System.out.print(queue[i] + " ");
            i = (i + 1) % capacity;
        } while (i != (rear + 1) % capacity);
        System.out.println();
    }

    /**
     * Main method to demonstrate the usage of the CircularQueue class.
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        CircularQueue cq = new CircularQueue(5);

        // Enqueue elements
        cq.enqueue(10);
        cq.enqueue(20);
        cq.enqueue(30);
        cq.enqueue(40);
        cq.enqueue(50);
        cq.display();

        // Try to enqueue when full
        try {
            cq.enqueue(60);
        } catch (IllegalStateException e) {
            System.out.println(e.getMessage());
        }

        // Dequeue elements
        System.out.println("Dequeued: " + cq.dequeue());
        System.out.println("Dequeued: " + cq.dequeue());
        cq.display();

        // Enqueue again
        cq.enqueue(60);
        cq.enqueue(70);
        cq.display();

        // Peek and size
        System.out.println("Front element: " + cq.peek());
        System.out.println("Queue size: " + cq.size());
    }
}
```
