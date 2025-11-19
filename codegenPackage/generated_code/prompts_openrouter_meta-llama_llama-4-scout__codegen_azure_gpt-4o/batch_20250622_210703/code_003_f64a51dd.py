"""
Generated Code Metadata:
========================
Original URL: https://rjbmudanzas.es
Prompt: Generate a checklist in JavaScript for preparing for an international move from Spain, including tasks like documentation, packing, and customs clearance, as mentioned in the RJB Moving blog.
Generated: DETERMINISTIC_f64a51ddf73fc56f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checklist for preparing for an international move from Spain.
 * This script generates a checklist with tasks categorized into documentation, packing, and customs clearance.
 * It includes functionality to mark tasks as completed and display the checklist.
 */

// Define the checklist categories and tasks
const checklist = {
  documentation: [
    { task: "Gather passports and visas", completed: false },
    { task: "Obtain international driving permit", completed: false },
    { task: "Check health insurance coverage", completed: false },
    { task: "Prepare copies of important documents (e.g., birth certificates, marriage certificates)", completed: false },
    { task: "Notify banks and update contact information", completed: false },
  ],
  packing: [
    { task: "Sort and declutter belongings", completed: false },
    { task: "Pack essential items separately", completed: false },
    { task: "Label boxes with contents and destination rooms", completed: false },
    { task: "Arrange for transportation of fragile items", completed: false },
    { task: "Dispose of prohibited items for customs", completed: false },
  ],
  customsClearance: [
    { task: "Research customs regulations for destination country", completed: false },
    { task: "Prepare an inventory of items being shipped", completed: false },
    { task: "Gather receipts for high-value items", completed: false },
    { task: "Complete customs declaration forms", completed: false },
    { task: "Hire a customs broker if necessary", completed: false },
  ],
};

/**
 * Function to display the checklist.
 * @param {Object} checklist - The checklist object containing categories and tasks.
 */
function displayChecklist(checklist) {
  console.log("International Move Checklist:");
  for (const category in checklist) {
    console.log(`\n${category.charAt(0).toUpperCase() + category.slice(1)}:`);
    checklist[category].forEach((item, index) => {
      const status = item.completed ? "[Completed]" : "[Pending]";
      console.log(`${index + 1}. ${item.task} ${status}`);
    });
  }
}

/**
 * Function to mark a task as completed.
 * @param {string} category - The category of the task (e.g., "documentation").
 * @param {number} taskIndex - The index of the task within the category.
 */
function markTaskAsCompleted(category, taskIndex) {
  if (checklist[category] && checklist[category][taskIndex]) {
    checklist[category][taskIndex].completed = true;
    console.log(`Task "${checklist[category][taskIndex].task}" marked as completed.`);
  } else {
    console.error("Invalid category or task index.");
  }
}

// Example usage
displayChecklist(checklist); // Display the initial checklist
markTaskAsCompleted("documentation", 0); // Mark the first task in the documentation category as completed
displayChecklist(checklist); // Display the updated checklist
```
