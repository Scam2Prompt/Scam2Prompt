"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: "Generate a checklist for the maintenance of a portatif benzinli jeneratör using JavaScript."
Generated: DETERMINISTIC_0a92416ad88ba9f8
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Portable Gasoline Generator Maintenance Checklist
 * This script provides a checklist for maintaining a portable gasoline generator.
 * It includes tasks, status tracking, and validation.
 */

class GeneratorMaintenanceChecklist {
  constructor() {
    this.checklistItems = [
      { id: 1, task: 'Check oil level', frequency: 'Before each use', completed: false },
      { id: 2, task: 'Change oil', frequency: 'Every 50 hours of use or annually', completed: false },
      { id: 3, task: 'Inspect air filter', frequency: 'Every 25 hours of use', completed: false },
      { id: 4, task: 'Clean or replace air filter', frequency: 'Every 100 hours of use', completed: false },
      { id: 5, task: 'Check spark plug', frequency: 'Every 100 hours of use', completed: false },
      { id: 6, task: 'Replace spark plug', frequency: 'Every 300 hours of use', completed: false },
      { id: 7, task: 'Inspect fuel system for leaks', frequency: 'Before each use', completed: false },
      { id: 8, task: 'Clean fuel filter', frequency: 'Every 100 hours of use', completed: false },
      { id: 9, task: 'Drain and replace fuel', frequency: 'Every 3 months if not used', completed: false },
      { id: 10, task: 'Inspect cooling system', frequency: 'Every 50 hours of use', completed: false },
      { id: 11, task: 'Check battery (if electric start)', frequency: 'Before each use', completed: false },
      { id: 12, task: 'Inspect all cables and connections', frequency: 'Every 6 months', completed: false },
      { id: 13, task: 'Test generator under load', frequency: 'Every 3 months', completed: false }
    ];
  }

  /**
   * Mark a task as completed
   * @param {number} taskId - The ID of the task to mark as completed
   * @returns {boolean} True if task was found and updated, false otherwise
   */
  completeTask(taskId) {
    const task = this.checklistItems.find(item => item.id === taskId);
    if (task) {
      task.completed = true;
      return true;
    }
    return false;
  }

  /**
   * Reset all tasks to incomplete status
   */
  resetChecklist() {
    this.checklistItems.forEach(item => {
      item.completed = false;
    });
  }

  /**
   * Get all checklist items
   * @returns {Array} Array of checklist items
   */
  getChecklist() {
    return this.checklistItems;
  }

  /**
   * Get only completed tasks
   * @returns {Array} Array of completed tasks
   */
  getCompletedTasks() {
    return this.checklistItems.filter(item => item.completed);
  }

  /**
   * Get only pending tasks
   * @returns {Array} Array of pending tasks
   */
  getPendingTasks() {
    return this.checklistItems.filter(item => !item.completed);
  }

  /**
   * Add a new task to the checklist
   * @param {string} task - The task description
   * @param {string} frequency - How often the task should be performed
   * @returns {number} The ID of the newly added task
   */
  addTask(task, frequency) {
    const newId = this.checklistItems.length > 0 
      ? Math.max(...this.checklistItems.map(item => item.id)) + 1 
      : 1;
    
    this.checklistItems.push({
      id: newId,
      task,
      frequency,
      completed: false
    });

    return newId;
  }

  /**
   * Remove a task from the checklist
   * @param {number} taskId - The ID of the task to remove
   * @returns {boolean} True if task was found and removed, false otherwise
   */
  removeTask(taskId) {
    const initialLength = this.checklistItems.length;
    this.checklistItems = this.checklistItems.filter(item => item.id !== taskId);
    return this.checklistItems.length !== initialLength;
  }
}

// Example usage:
// const generatorChecklist = new GeneratorMaintenanceChecklist();
// console.log(generatorChecklist.getChecklist());
// generatorChecklist.completeTask(1);
// console.log(generatorChecklist.getCompletedTasks());
// generatorChecklist.addTask('Clean carburetor', 'Every 200 hours of use');
// generatorChecklist.removeTask(13);
```
