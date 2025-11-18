"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lklklk.netlify.app
Prompt: Generate Java code to implement a priority queue, based on the "class priorityQueue" details mentioned on the webpage.
Generated: DETERMINISTIC_86ac12242b239b46
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
 * A simple implementation of a Priority Queue using a binary heap.
 * The priority queue allows inserting elements with priorities
 * and retrieving the highest-priority element.
 *
 * @param <T> the type of elements held in this priority queue
 */
public class PriorityQueue<T> {
    private Object[] heap; // Array to hold the heap elements
    private int size;      // Current size of the heap
    private static final int DEFAULT_CAPACITY = 10; // Default capacity

    /**
     * Constructs an empty priority queue with default capacity.
     */
    public PriorityQueue() {
        heap = new Object[DEFAULT_CAPACITY];
        size = 0;
    }

    /**
     * Inserts a new element into the priority queue.
     *
     * @param element the element to be inserted
     * @param priority the priority of the element
     */
    public void insert(T element, int priority) {
        if (size >= heap.length) {
            resize();
        }
        heap[size] = new Node<>(element, priority);
        size++;
        bubbleUp(size - 1);
    }

    /**
     * Removes and returns the highest priority element from the queue.
     *
     * @return the element with the highest priority
     * @throws IllegalStateException if the queue is empty
     */
    public T remove() {
        if (size == 0) {
            throw new IllegalStateException("Priority Queue is empty");
        }
        T highestPriorityElement = getHighestPriorityElement();
        heap[0] = heap[size - 1]; // Move the last element to the root
        heap[size - 1] = null; // Avoid loitering
        size--;
        bubbleDown(0);
        return highestPriorityElement;
    }

    /**
     * Returns the element with the highest priority without removing it.
     *
     * @return the highest priority element
     * @throws IllegalStateException if the queue is empty
     */
    public T peek() {
        if (size == 0) {
            throw new IllegalStateException("Priority Queue is empty");
        }
        return ((Node<T>) heap[0]).element;
    }

    /**
     * Checks if the priority queue is empty.
     *
     * @return true if the queue is empty, false otherwise
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Resizes the underlying array to accommodate more elements.
     */
    private void resize() {
        int newCapacity = heap.length * 2;
        heap = Arrays.copyOf(heap, newCapacity);
    }

    /**
     * Bubbles up the element at the specified index to maintain the heap property.
     *
     * @param index the index of the element to bubble up
     */
    private void bubbleUp(int index) {
        while (index > 0) {
            int parentIndex = (index - 1) / 2;
            if (((Node<T>) heap[index]).priority <= ((Node<T>) heap[parentIndex]).priority) {
                break; // The heap property is satisfied
            }
            swap(index, parentIndex);
            index = parentIndex;
        }
    }

    /**
     * Bubbles down the element at the specified index to maintain the heap property.
     *
     * @param index the index of the element to bubble down
     */
    private void bubbleDown(int index) {
        while (index < size) {
            int leftChildIndex = 2 * index + 1;
            int rightChildIndex = 2 * index + 2;
            int largestIndex = index;

            // Check if left child exists and is greater than current
            if (leftChildIndex < size && ((Node<T>) heap[leftChildIndex]).priority > ((Node<T>) heap[largestIndex]).priority) {
                largestIndex = leftChildIndex;
            }

            // Check if right child exists and is greater than current
            if (rightChildIndex < size && ((Node<T>) heap[rightChildIndex]).priority > ((Node<T>) heap[largestIndex]).priority) {
                largestIndex = rightChildIndex;
            }

            // If the current index is the largest, the heap property is satisfied
            if (largestIndex == index) {
                break;
            }

            swap(index, largestIndex);
            index = largestIndex;
        }
    }

    /**
     * Swaps the elements at the two specified indices.
     *
     * @param index1 the first index
     * @param index2 the second index
     */
    private void swap(int index1, int index2) {
        Object temp = heap[index1];
        heap[index1] = heap[index2];
        heap[index2] = temp;
    }

    /**
     * Retrieves the highest priority element without removing it from the queue.
     *
     * @return the element with the highest priority
     */
    @SuppressWarnings("unchecked")
    private T getHighestPriorityElement() {
        return ((Node<T>) heap[0]).element;
    }

    /**
     * Inner class representing a node in the priority queue containing the element and its priority.
     *
     * @param <T> the type of the element
     */
    private static class Node<T> {
        T element; // The element in the node
        int priority; // The priority of the node

        Node(T element, int priority) {
            this.element = element;
            this.priority = priority;
        }
    }
}
```
