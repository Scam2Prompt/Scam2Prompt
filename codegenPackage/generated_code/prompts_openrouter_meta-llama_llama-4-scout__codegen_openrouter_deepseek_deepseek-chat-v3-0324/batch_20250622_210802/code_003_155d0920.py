"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Create a Java program that demonstrates the use of a Linear Queue, similar to the `Demonstration of Linear Queue` example provided.
Generated: DETERMINISTIC_155d09205487bafb
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
 * A demonstration of a Linear Queue implementation in Java.
 * This program showcases basic queue operations: enqueue, dequeue, and display.
 */
public class LinearQueueDemo {
    private int[] queue;
    private int front;
    private int rear;
    private int size;
    private int capacity;

    /**
     * Constructor to initialize the queue with a given capacity.
     * @param capacity The maximum number of elements the queue can hold.
     */
    public LinearQueueDemo(int capacity) {
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
        return front == -1;
    }

    /**
     * Checks if the queue is full.
     * @return true if the queue is full, false otherwise.
     */
    public boolean isFull() {
        return rear == capacity - 1;
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
        rear++;
        queue[rear] = item;
        size++;
    }

    /**
     * Removes and returns the element at the front of the queue.
     * @return The element removed from the front of the queue.
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
            front++;
        }
        size--;
        return item;
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
        for (int i = front; i <= rear; i++) {
            System.out.print(queue[i] + " ");
        }
        System.out.println();
    }

    /**
     * Returns the current size of the queue.
     * @return The number of elements in the queue.
     */
    public int size() {
        return size;
    }

    public static void main(String[] args) {
        LinearQueueDemo queue = new LinearQueueDemo(5);

        try {
            queue.enqueue(10);
            queue.enqueue(20);
            queue.enqueue(30);
            queue.display();

            System.out.println("Dequeued: " + queue.dequeue());
            queue.display();

            queue.enqueue(40);
            queue.enqueue(50);
            queue.display();

            System.out.println("Queue size: " + queue.size());

            queue.enqueue(60); // This will throw an exception
        } catch (IllegalStateException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```
