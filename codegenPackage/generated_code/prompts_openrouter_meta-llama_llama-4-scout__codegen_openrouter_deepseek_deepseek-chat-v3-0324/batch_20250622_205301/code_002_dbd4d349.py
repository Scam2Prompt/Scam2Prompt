"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Generate a checklist for diagnosing issues with fuel injector performance in diesel vehicles and provide a code snippet in JavaScript to create a simple diagnostic tool.
Generated: DETERMINISTIC_dbd4d34944643583
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Diesel Fuel Injector Diagnostic Checklist Tool
 * This tool helps diagnose common fuel injector performance issues in diesel vehicles.
 */

class DieselInjectorDiagnostic {
  constructor() {
    this.checklist = [
      {
        id: 1,
        description: "Check for fuel leaks around injectors",
        completed: false,
        severity: "high"
      },
      {
        id: 2,
        description: "Inspect injector electrical connections",
        completed: false,
        severity: "high"
      },
      {
        id: 3,
        description: "Measure injector resistance with multimeter",
        completed: false,
        severity: "medium"
      },
      {
        id: 4,
        description: "Perform injector balance test",
        completed: false,
        severity: "medium"
      },
      {
        id: 5,
        description: "Check fuel pressure at rail",
        completed: false,
        severity: "high"
      },
      {
        id: 6,
        description: "Inspect injector spray pattern",
        completed: false,
        severity: "medium"
      },
      {
        id: 7,
        description: "Check for DTCs (Diagnostic Trouble Codes)",
        completed: false,
        severity: "high"
      },
      {
        id: 8,
        description: "Verify fuel quality and contamination",
        completed: false,
        severity: "low"
      },
      {
        id: 9,
        description: "Inspect injector nozzles for wear",
        completed: false,
        severity: "medium"
      },
      {
        id: 10,
        description: "Check engine compression",
        completed: false,
        severity: "high"
      }
    ];
  }

  /**
   * Mark a checklist item as completed
   * @param {number} id - The ID of the checklist item
   * @throws {Error} If item ID is not found
   */
  completeItem(id) {
    const item = this.checklist.find(item => item.id === id);
    if (!item) {
      throw new Error(`Checklist item with ID ${id} not found`);
    }
    item.completed = true;
  }

  /**
   * Get all checklist items
   * @returns {Array} Array of checklist items
   */
  getChecklist() {
    return this.checklist;
  }

  /**
   * Get checklist items by severity
   * @param {string} severity - 'high', 'medium', or 'low'
   * @returns {Array} Filtered array of checklist items
   * @throws {Error} If severity is invalid
   */
  getItemsBySeverity(severity) {
    const validSeverities = ['high', 'medium', 'low'];
    if (!validSeverities.includes(severity)) {
      throw new Error(`Invalid severity. Must be one of: ${validSeverities.join(', ')}`);
    }
    return this.checklist.filter(item => item.severity === severity);
  }

  /**
   * Get completion percentage of the checklist
   * @returns {number} Percentage completed (0-100)
   */
  getCompletionPercentage() {
    const completed = this.checklist.filter(item => item.completed).length;
    return Math.round((completed / this.checklist.length) * 100);
  }

  /**
   * Reset all checklist items to incomplete
   */
  resetChecklist() {
    this.checklist.forEach(item => {
      item.completed = false;
    });
  }
}

// Example usage
const diagnosticTool = new DieselInjectorDiagnostic();

// Export for use in other modules if needed
module.exports = DieselInjectorDiagnostic;
```
