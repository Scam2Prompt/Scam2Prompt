"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rb.itsmeplabon.xyz
Prompt: Write a JavaScript function to calculate and display task completion percentages dynamically based on `taskCount`, `tasksCompleted`, and `tasksRemaining` values, as described in the webpage content.
Generated: DETERMINISTIC_9acfda32bd72ff3b
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates and displays task completion percentage based on task counts.
 * 
 * @param {number} taskCount - The total number of tasks.
 * @param {number} tasksCompleted - The number of tasks completed so far.
 * @param {number} tasksRemaining - The number of tasks yet to be completed.
 * @returns {void}
 */
function displayTaskCompletion(taskCount, tasksCompleted, tasksRemaining) {
    try {
        // Validate input
        if (typeof taskCount !== 'number' || typeof tasksCompleted !== 'number' || typeof tasksRemaining !== 'number') {
            throw new Error("All inputs must be numbers.");
        }
        if (taskCount < 0 || tasksCompleted < 0 || tasksRemaining < 0) {
            throw new Error("Task counts cannot be negative.");
        }
        if (tasksCompleted + tasksRemaining !== taskCount) {
            throw new Error("The total tasks should equal the sum of completed and remaining tasks.");
        }

        // Calculate the percentage of tasks completed
        const completionPercentage = ((tasksCompleted / taskCount) * 100).toFixed(2);

        // Display the result dynamically
        const resultElement = document.getElementById("taskCompletionDisplay");
        if (!resultElement) {
            throw new Error("DOM element with id 'taskCompletionDisplay' not found.");
        }

        resultElement.textContent = `Task Completion: ${completionPercentage}%`;
    } catch (error) {
        console.error("Error calculating task completion percentage:", error.message);
    }
}

/*
Example Usage:
1. Ensure an element with id 'taskCompletionDisplay' exists in your HTML.
2. Call the function with valid input values:
   displayTaskCompletion(10, 7, 3);
3. The text content of the element will be updated with the completion percentage.
*/
```
