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
import java.util.Scanner;

/**
 * A class that implements a Linear Queue using an array.
 */
class LinearQueue {
    private int[] queue; // Array to hold the queue elements
    private int front;   // Index of the front element
    private int rear;    // Index of the rear element
    private int capacity; // Maximum number of elements in the queue

    /**
     * Constructor to initialize the queue.
     * 
     * @param size The maximum size of the queue.
     */
    public LinearQueue(int size) {
        this.capacity = size;
        this.queue = new int[capacity];
        this.front = -1;
        this.rear = -1;
    }

    /**
     * Adds an element to the rear of the queue.
     * 
     * @param value The value to be added to the queue.
     * @throws IllegalStateException if the queue is full.
     */
    public void enqueue(int value) {
        if (isFull()) {
            throw new IllegalStateException("Queue is full. Cannot enqueue " + value);
        }
        if (front == -1) {
            front = 0; // Initialize front if it's the first element
        }
        rear++;
        queue[rear] = value;
        System.out.println("Enqueued: " + value);
    }

    /**
     * Removes and returns the front element of the queue.
     * 
     * @return The front element of the queue.
     * @throws IllegalStateException if the queue is empty.
     */
    public int dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty. Cannot dequeue.");
        }
        int value = queue[front];
        front++;
        if (front > rear) { // Reset the queue if it's empty after dequeue
            front = rear = -1;
        }
        System.out.println("Dequeued: " + value);
        return value;
    }

    /**
     * Checks if the queue is empty.
     * 
     * @return true if the queue is empty, false otherwise.
     */
    public boolean isEmpty() {
        return front == -1;
    }

    /**
     * Checks if the queue is full.
     * 
     * @return true if the queue is full, false otherwise.
     */
    public boolean isFull() {
        return rear == capacity - 1;
    }

    /**
     * Displays the current elements in the queue.
     */
    public void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty.");
            return;
        }
        System.out.print("Queue elements: ");
        for (int i = front; i <= rear; i++) {
            System.out.print(queue[i] + " ");
        }
        System.out.println();
    }
}

/**
 * Main class to demonstrate the Linear Queue functionality.
 */
public class LinearQueueDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the queue: ");
        int size = scanner.nextInt();

        LinearQueue queue = new LinearQueue(size);

        while (true) {
            System.out.println("\n1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Display");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();

            try {
                switch (choice) {
                    case 1:
                        System.out.print("Enter value to enqueue: ");
                        int value = scanner.nextInt();
                        queue.enqueue(value);
                        break;
                    case 2:
                        queue.dequeue();
                        break;
                    case 3:
                        queue.display();
                        break;
                    case 4:
                        System.out.println("Exiting...");
                        scanner.close();
                        return;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            } catch (IllegalStateException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
```
