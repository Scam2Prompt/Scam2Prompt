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
import java.util.NoSuchElementException;

/**
 * A simple implementation of a Linear Queue in Java.
 *
 * @param <T> The type of elements in the queue.
 */
public class LinearQueue<T> {

    // Node class representing each element in the queue
    private static class Node<T> {
        T data;
        Node<T> next;

        public Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    // Front and rear pointers of the queue
    private Node<T> front;
    private Node<T> rear;

    // Size of the queue
    private int size;

    /**
     * Constructs an empty linear queue.
     */
    public LinearQueue() {
        front = null;
        rear = null;
        size = 0;
    }

    /**
     * Adds an element to the end of the queue.
     *
     * @param data The element to be added.
     */
    public void enqueue(T data) {
        Node<T> newNode = new Node<>(data);

        if (rear == null) {
            front = newNode;
            rear = newNode;
        } else {
            rear.next = newNode;
            rear = newNode;
        }

        size++;
    }

    /**
     * Removes an element from the front of the queue.
     *
     * @return The removed element.
     * @throws NoSuchElementException if the queue is empty.
     */
    public T dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty");
        }

        T data = front.data;
        front = front.next;

        if (front == null) {
            rear = null;
        }

        size--;
        return data;
    }

    /**
     * Returns the element at the front of the queue without removing it.
     *
     * @return The element at the front of the queue.
     * @throws NoSuchElementException if the queue is empty.
     */
    public T peek() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty");
        }

        return front.data;
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
     * Returns the size of the queue.
     *
     * @return The number of elements in the queue.
     */
    public int size() {
        return size;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        Node<T> temp = front;

        while (temp != null) {
            sb.append(temp.data);

            if (temp.next != null) {
                sb.append(", ");
            }

            temp = temp.next;
        }

        sb.append("]");
        return sb.toString();
    }

    public static void main(String[] args) {
        LinearQueue<Integer> queue = new LinearQueue<>();

        // Enqueue elements
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        queue.enqueue(4);
        queue.enqueue(5);

        System.out.println("Queue: " + queue); // [1, 2, 3, 4, 5]
        System.out.println("Size: " + queue.size()); // 5

        // Dequeue an element
        System.out.println("Dequeued: " + queue.dequeue()); // 1
        System.out.println("Queue: " + queue); // [2, 3, 4, 5]

        // Peek at the front element
        System.out.println("Front: " + queue.peek()); // 2

        // Check if the queue is empty
        System.out.println("Is empty? " + queue.isEmpty()); // false

        // Dequeue all elements
        while (!queue.isEmpty()) {
            System.out.println("Dequeued: " + queue.dequeue());
        }

        System.out.println("Is empty? " + queue.isEmpty()); // true

        try {
            queue.dequeue(); // This should throw an exception
        } catch (NoSuchElementException e) {
            System.out.println("Exception caught: " + e.getMessage()); // Queue is empty
        }
    }
}
```
