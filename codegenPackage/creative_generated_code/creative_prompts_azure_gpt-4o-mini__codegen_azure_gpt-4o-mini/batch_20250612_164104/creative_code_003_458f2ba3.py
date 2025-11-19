"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatask.co.kr
Prompt: What are the best practices for using the META Task library in a JavaScript application?
Generated: DETERMINISTIC_458f2ba3628a1628
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the META Task library
import { Task, ParallelTask, SequentialTask } from 'meta-task-library';

/**
 * Example of using the META Task library in a JavaScript application.
 * This code demonstrates best practices for creating and managing tasks.
 */

// Function to simulate an asynchronous operation (e.g., API call)
const asyncOperation = (duration) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // Simulating a possible failure
            if (Math.random() > 0.8) {
                reject(new Error('Operation failed!'));
            } else {
                resolve(`Operation completed in ${duration}ms`);
            }
        }, duration);
    });
};

/**
 * Main function to demonstrate the use of META Task library.
 */
async function main() {
    try {
        // Create individual tasks
        const task1 = new Task(() => asyncOperation(1000));
        const task2 = new Task(() => asyncOperation(1500));
        const task3 = new Task(() => asyncOperation(500));

        // Create a parallel task to run tasks concurrently
        const parallelTask = new ParallelTask([task1, task2, task3]);

        // Execute the parallel task and wait for completion
        const results = await parallelTask.run();

        // Log results of all tasks
        console.log('All tasks completed successfully:', results);

        // Optionally, create a sequential task
        const sequentialTask = new SequentialTask([task1, task2, task3]);

        // Execute the sequential task and wait for completion
        const sequentialResults = await sequentialTask.run();

        // Log results of sequential tasks
        console.log('All sequential tasks completed successfully:', sequentialResults);
    } catch (error) {
        // Proper error handling for task failures
        console.error('An error occurred during task execution:', error.message);
    }
}

// Run the main function
main();
```
