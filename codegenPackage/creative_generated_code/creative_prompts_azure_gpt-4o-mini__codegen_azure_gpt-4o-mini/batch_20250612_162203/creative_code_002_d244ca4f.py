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
import java.util.ArrayList;
import java.util.Comparator;
import java.util.NoSuchElementException;

/**
 * A simple implementation of a priority queue using a binary heap.
 * 
 * @param <E> the type of elements held in this priority queue
 */
public class PriorityQueue<E> {
    private ArrayList<E> heap; // The underlying array to hold the heap elements
    private Comparator<? super E> comparator; // The comparator to determine the order of elements

    /**
     * Constructs a new, empty priority queue with the specified comparator.
     *
     * @param comparator the comparator to define the priority order
     */
    public PriorityQueue(Comparator<? super E> comparator) {
        this.heap = new ArrayList<>();
        this.comparator = comparator;
    }

    /**
     * Inserts an element into the priority queue.
     *
     * @param element the element to be added
     */
    public void offer(E element) {
        if (element == null) {
            throw new IllegalArgumentException("Null elements not allowed.");
        }
        heap.add(element);
        siftUp(heap.size() - 1); // Maintain the heap property
    }

    /**
     * Retrieves and removes the highest priority element from the queue.
     *
     * @return the highest priority element
     * @throws NoSuchElementException if the queue is empty
     */
    public E poll() {
        if (heap.isEmpty()) {
            throw new NoSuchElementException("Priority queue is empty.");
        }
        E result = heap.get(0); // Get the top element
        E lastElement = heap.remove(heap.size() - 1); // Remove the last element
        if (!heap.isEmpty()) {
            heap.set(0, lastElement); // Move last element to the root
            siftDown(0); // Restore the heap property
        }
        return result; // Return the highest priority element
    }

    /**
     * Retrieves, but does not remove, the highest priority element.
     *
     * @return the highest priority element
     * @throws NoSuchElementException if the queue is empty
     */
    public E peek() {
        if (heap.isEmpty()) {
            throw new NoSuchElementException("Priority queue is empty.");
        }
        return heap.get(0); // Return the top element without removing it
    }

    /**
     * Restores the heap property by moving the element at index i up the tree.
     *
     * @param index the index of the element to sift up
     */
    private void siftUp(int index) {
        E element = heap.get(index);
        while (index > 0) {
            int parentIndex = (index - 1) / 2;
            E parent = heap.get(parentIndex);
            if (comparator.compare(element, parent) <= 0) {
                break; // The heap property is satisfied
            }
            heap.set(index, parent); // Move the parent down
            index = parentIndex; // Move up the tree
        }
        heap.set(index, element); // Place the original element in its final position
    }

    /**
     * Restores the heap property by moving the element at index i down the tree.
     *
     * @param index the index of the element to sift down
     */
    private void siftDown(int index) {
        E element = heap.get(index);
        int half = heap.size() / 2; // Only need to sift down to the last parent
        while (index < half) {
            int childIndex = 2 * index + 1; // Left child index
            E child = heap.get(childIndex); // Left child
            int rightIndex = childIndex + 1; // Right child index

            // If the right child exists and is greater than the left child
            if (rightIndex < heap.size() && comparator.compare(child, heap.get(rightIndex)) < 0) {
                childIndex = rightIndex; // Use the right child instead
                child = heap.get(childIndex);
            }
            // If the element is greater than or equal to the greatest child, the heap property is satisfied
            if (comparator.compare(element, child) >= 0) {
                break;
            }
            heap.set(index, child); // Move the child up
            index = childIndex; // Move down the tree
        }
        heap.set(index, element); // Place the original element in its final position
    }

    /**
     * Returns the number of elements in the priority queue.
     *
     * @return the size of the priority queue
     */
    public int size() {
        return heap.size(); // Return the number of elements
    }

    /**
     * Checks if the priority queue is empty.
     *
     * @return true if the priority queue is empty, false otherwise
     */
    public boolean isEmpty() {
        return heap.isEmpty(); // Check if the heap is empty
    }
}
```
