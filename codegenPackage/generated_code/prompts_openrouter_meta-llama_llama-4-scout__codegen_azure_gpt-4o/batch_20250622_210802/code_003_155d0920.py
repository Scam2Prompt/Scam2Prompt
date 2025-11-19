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
 * A simple demonstration of a Linear Queue implementation in Java.
 * This program allows enqueue, dequeue, and display operations on the queue.
 */
public class LinearQueueDemo {

    // Class representing a Linear Queue
    static class LinearQueue {
        private int[] queue; // Array to store queue elements
        private int front;   // Index of the front element
        private int rear;    // Index of the rear element
        private int size;    // Maximum size of the queue

        /**
         * Constructor to initialize the queue.
         *
         * @param size The maximum size of the queue.
         */
        public LinearQueue(int size) {
            this.size = size;
            this.queue = new int[size];
            this.front = -1;
            this.rear = -1;
        }

        /**
         * Enqueues an element into the queue.
         *
         * @param element The element to be added.
         * @return True if the element is successfully enqueued, false otherwise.
         */
        public boolean enqueue(int element) {
            if (rear == size - 1) { // Check if the queue is full
                System.out.println("Queue is full. Cannot enqueue.");
                return false;
            }
            if (front == -1) { // If the queue is empty, set front to 0
                front = 0;
            }
            queue[++rear] = element; // Increment rear and add the element
            System.out.println("Enqueued: " + element);
            return true;
        }

        /**
         * Dequeues an element from the queue.
         *
         * @return The dequeued element, or -1 if the queue is empty.
         */
        public int dequeue() {
            if (front == -1 || front > rear) { // Check if the queue is empty
                System.out.println("Queue is empty. Cannot dequeue.");
                return -1;
            }
            int dequeuedElement = queue[front++]; // Retrieve the front element and increment front
            System.out.println("Dequeued: " + dequeuedElement);
            return dequeuedElement;
        }

        /**
         * Displays the elements of the queue.
         */
        public void display() {
            if (front == -1 || front > rear) { // Check if the queue is empty
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
     * Main method to demonstrate the Linear Queue operations.
     *
     * @param args Command-line arguments (not used).
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the queue: ");
        int size = scanner.nextInt();

        LinearQueue queue = new LinearQueue(size);

        while (true) {
            System.out.println("\nQueue Operations:");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Display");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter the element to enqueue: ");
                    int element = scanner.nextInt();
                    queue.enqueue(element);
                    break;
                case 2:
                    queue.dequeue();
                    break;
                case 3:
                    queue.display();
                    break;
                case 4:
                    System.out.println("Exiting program.");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
```
