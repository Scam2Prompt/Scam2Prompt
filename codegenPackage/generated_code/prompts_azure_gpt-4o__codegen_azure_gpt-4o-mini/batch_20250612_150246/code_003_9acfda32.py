"""
Generated Code Metadata:
========================
Original URL: https://rb.itsmeplabon.xyz
Prompt: Write a JavaScript function to calculate and display task completion percentages dynamically based on `taskCount`, `tasksCompleted`, and `tasksRemaining` values, as described in the webpage content.
Generated: DETERMINISTIC_9acfda32bd72ff3b
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates and displays the task completion percentage dynamically.
 * 
 * @param {number} taskCount - The total number of tasks.
 * @param {number} tasksCompleted - The number of tasks that have been completed.
 * @param {number} tasksRemaining - The number of tasks that are still pending.
 * @throws {Error} Will throw an error if taskCount is less than 0 or if tasksCompleted or tasksRemaining are negative.
 */
function displayTaskCompletionPercentage(taskCount, tasksCompleted, tasksRemaining) {
    // Validate input parameters
    if (taskCount < 0) {
        throw new Error("taskCount must be a non-negative number.");
    }
    if (tasksCompleted < 0 || tasksRemaining < 0) {
        throw new Error("tasksCompleted and tasksRemaining must be non-negative numbers.");
    }
    if (tasksCompleted + tasksRemaining !== taskCount) {
        throw new Error("The sum of tasksCompleted and tasksRemaining must equal taskCount.");
    }

    // Calculate the completion percentage
    const completionPercentage = (tasksCompleted / taskCount) * 100;

    // Display the completion percentage
    const percentageDisplayElement = document.getElementById('completion-percentage');
    if (percentageDisplayElement) {
        percentageDisplayElement.textContent = `Task Completion: ${completionPercentage.toFixed(2)}%`;
    } else {
        console.warn("Element with ID 'completion-percentage' not found.");
    }
}

// Example usage
try {
    displayTaskCompletionPercentage(10, 7, 3); // Adjust values as needed
} catch (error) {
    console.error("Error calculating task completion percentage:", error.message);
}
```
