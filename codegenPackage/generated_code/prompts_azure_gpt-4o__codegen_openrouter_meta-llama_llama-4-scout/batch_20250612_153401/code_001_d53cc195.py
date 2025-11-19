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
 * A class representing a circular queue data structure.
 *
 * @param <T> The type of elements in the queue.
 */
public class CircularQueue<T> {

    private final Object[] queue;
    private int front;
    private int rear;
    private int size;
    private int capacity;

    /**
     * Constructs a new circular queue with the given capacity.
     *
     * @param capacity The maximum number of elements the queue can hold.
     */
    @SuppressWarnings("unchecked")
    public CircularQueue(int capacity) {
        this.capacity = capacity;
        this.queue = new Object[capacity];
        this.front = 0;
        this.rear = 0;
        this.size = 0;
    }

    /**
     * Adds an element to the end of the queue.
     *
     * @param element The element to add.
     * @throws IllegalStateException if the queue is full.
     */
    public void enqueue(T element) {
        if (isFull()) {
            throw new IllegalStateException("Queue is full");
        }
        queue[rear] = element;
        rear = (rear + 1) % capacity;
        size++;
    }

    /**
     * Removes an element from the front of the queue.
     *
     * @return The removed element.
     * @throws NoSuchElementException if the queue is empty.
     */
    @SuppressWarnings("unchecked")
    public T dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty");
        }
        T element = (T) queue[front];
        queue[front] = null;
        front = (front + 1) % capacity;
        size--;
        return element;
    }

    /**
     * Returns the element at the front of the queue without removing it.
     *
     * @return The element at the front of the queue.
     * @throws NoSuchElementException if the queue is empty.
     */
    @SuppressWarnings("unchecked")
    public T peek() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty");
        }
        return (T) queue[front];
    }

    /**
     * Checks if the queue is empty.
     *
     * @return True if the queue is empty, false otherwise.
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Checks if the queue is full.
     *
     * @return True if the queue is full, false otherwise.
     */
    public boolean isFull() {
        return size == capacity;
    }

    /**
     * Returns the number of elements in the queue.
     *
     * @return The number of elements in the queue.
     */
    public int size() {
        return size;
    }

    public static void main(String[] args) {
        CircularQueue<Integer> queue = new CircularQueue<>(5);

        // Enqueue elements
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        queue.enqueue(4);
        queue.enqueue(5);

        // Attempt to enqueue when full
        try {
            queue.enqueue(6);
        } catch (IllegalStateException e) {
            System.out.println(e.getMessage()); // Queue is full
        }

        // Dequeue elements
        System.out.println(queue.dequeue()); // 1
        System.out.println(queue.dequeue()); // 2

        // Peek at the front element
        System.out.println(queue.peek()); // 3

        // Check queue size
        System.out.println(queue.size()); // 3

        // Check if queue is empty
        System.out.println(queue.isEmpty()); // false

        // Check if queue is full
        System.out.println(queue.isFull()); // false
    }
}
```
