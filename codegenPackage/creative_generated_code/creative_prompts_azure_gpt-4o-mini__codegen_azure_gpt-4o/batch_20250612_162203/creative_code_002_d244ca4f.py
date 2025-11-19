"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lklklk.netlify.app
Prompt: Generate code for a priority queue in Java, based on the unique features mentioned in the webpage.
Generated: DETERMINISTIC_d244ca4f378ccbc8
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.*;

// Class representing a Node in the priority queue
class PriorityQueueNode<T> {
    private T data;
    private int priority;

    public PriorityQueueNode(T data, int priority) {
        this.data = data;
        this.priority = priority;
    }

    public T getData() {
        return data;
    }

    public int getPriority() {
        return priority;
    }

    @Override
    public String toString() {
        return "Data: " + data + ", Priority: " + priority;
    }
}

// Implementation of a Priority Queue using a Min-Heap
public class PriorityQueue<T> {
    private final List<PriorityQueueNode<T>> heap;

    public PriorityQueue() {
        heap = new ArrayList<>();
    }

    /**
     * Adds an element to the priority queue.
     *
     * @param data     The data to be added.
     * @param priority The priority of the data.
     */
    public void enqueue(T data, int priority) {
        if (data == null) {
            throw new IllegalArgumentException("Data cannot be null.");
        }
        PriorityQueueNode<T> node = new PriorityQueueNode<>(data, priority);
        heap.add(node);
        heapifyUp(heap.size() - 1);
    }

    /**
     * Removes and returns the element with the highest priority (lowest priority value).
     *
     * @return The data of the highest priority element.
     * @throws NoSuchElementException If the queue is empty.
     */
    public T dequeue() {
        if (heap.isEmpty()) {
            throw new NoSuchElementException("Priority queue is empty.");
        }
        T data = heap.get(0).getData();
        Collections.swap(heap, 0, heap.size() - 1);
        heap.remove(heap.size() - 1);
        heapifyDown(0);
        return data;
    }

    /**
     * Peeks at the element with the highest priority without removing it.
     *
     * @return The data of the highest priority element.
     * @throws NoSuchElementException If the queue is empty.
     */
    public T peek() {
        if (heap.isEmpty()) {
            throw new NoSuchElementException("Priority queue is empty.");
        }
        return heap.get(0).getData();
    }

    /**
     * Returns the size of the priority queue.
     *
     * @return The size of the priority queue.
     */
    public int size() {
        return heap.size();
    }

    /**
     * Checks if the priority queue is empty.
     *
     * @return true if the priority queue is empty, false otherwise.
     */
    public boolean isEmpty() {
        return heap.isEmpty();
    }

    // Helper method to restore heap property when adding a new element
    private void heapifyUp(int index) {
        while (index > 0) {
            int parentIndex = (index - 1) / 2;
            if (heap.get(index).getPriority() < heap.get(parentIndex).getPriority()) {
                Collections.swap(heap, index, parentIndex);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    // Helper method to restore heap property when removing the root element
    private void heapifyDown(int index) {
        int leftChild;
        int rightChild;
        int smallest;
        while (index < heap.size()) {
            leftChild = 2 * index + 1;
            rightChild = 2 * index + 2;
            smallest = index;

            if (leftChild < heap.size() && heap.get(leftChild).getPriority() < heap.get(smallest).getPriority()) {
                smallest = leftChild;
            }

            if (rightChild < heap.size() && heap.get(rightChild).getPriority() < heap.get(smallest).getPriority()) {
                smallest = rightChild;
            }

            if (smallest != index) {
                Collections.swap(heap, index, smallest);
                index = smallest;
            } else {
                break;
            }
        }
    }

    public static void main(String[] args) {
        // Example usage of the PriorityQueue
        PriorityQueue<String> pq = new PriorityQueue<>();
        pq.enqueue("Task A", 3);
        pq.enqueue("Task B", 1);
        pq.enqueue("Task C", 2);

        System.out.println("Peek: " + pq.peek()); // Output: Task B
        System.out.println("Dequeue: " + pq.dequeue()); // Output: Task B
        System.out.println("Size: " + pq.size()); // Output: 2

        pq.enqueue("Task D", 0);
        System.out.println("Dequeue: " + pq.dequeue()); // Output: Task D
    }
}
```
