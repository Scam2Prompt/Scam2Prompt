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
 * Calculates the percentage of tasks completed based on the provided counts.
 * @param {number} taskCount - The total number of tasks.
 * @param {number} tasksCompleted - The number of completed tasks.
 * @param {number} tasksRemaining - The number of remaining tasks.
 * @returns {number} - The percentage of tasks completed.
 * @throws Will throw an error if any of the input values are negative or if taskCount is zero.
 */
function calculateCompletionPercentage(taskCount, tasksCompleted, tasksRemaining) {
    // Input validation
    if (taskCount < 0 || tasksCompleted < 0 || tasksRemaining < 0) {
        throw new Error('Task counts must be non-negative.');
    }
    if (taskCount === 0) {
        throw new Error('Task count cannot be zero.');
    }

    // Calculate the completion percentage
    const completionPercentage = (tasksCompleted / taskCount) * 100;

    return parseFloat(completionPercentage.toFixed(2)); // Return value rounded to two decimal places
}

/**
 * Updates the display of task completion percentage on the webpage.
 * @param {number} taskCount - The total number of tasks.
 * @param {number} tasksCompleted - The number of completed tasks.
 * @param {number} tasksRemaining - The number of remaining tasks.
 */
function updateCompletionDisplay(taskCount, tasksCompleted, tasksRemaining) {
    try {
        const percentage = calculateCompletionPercentage(taskCount, tasksCompleted, tasksRemaining);

        // Select the display element (assuming an element with id 'completionDisplay' exists)
        const displayElement = document.getElementById('completionDisplay');
        if (!displayElement) {
            throw new Error('Display element not found.');
        }

        // Update the inner text of the display element
        displayElement.innerText = `Tasks Completed: ${percentage}%`;
    } catch (error) {
        console.error('Error updating completion display:', error.message);
    }
}

// Example usage:
// Assuming there is an HTML element with id 'completionDisplay'
updateCompletionDisplay(100, 30, 70); // Updates the display to show 30% completed
```
