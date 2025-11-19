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
 * International Move Checklist Generator
 * 
 * This script creates a checklist for preparing for an international move from Spain.
 * It includes tasks for documentation, packing, and customs clearance.
 */

class MoveChecklist {
  constructor() {
    this.checklist = {
      documentation: [],
      packing: [],
      customs: [],
      completed: []
    };
    this.initializeChecklist();
  }

  initializeChecklist() {
    // Documentation tasks
    this.checklist.documentation = [
      "Check passport validity (minimum 6 months)",
      "Obtain visa/residence permit for destination country",
      "Gather birth certificates and marriage certificates",
      "Collect medical records and vaccination documents",
      "Obtain international driver's license if needed",
      "Notify Spanish authorities of your move (padrón)",
      "Cancel or transfer utilities and subscriptions"
    ];

    // Packing tasks
    this.checklist.packing = [
      "Create inventory of belongings",
      "Sort items into keep/sell/donate categories",
      "Obtain packing materials (boxes, tape, bubble wrap)",
      "Pack non-essentials first",
      "Label boxes clearly with contents and destination room",
      "Pack essentials separately (first week box)",
      "Arrange for professional movers or rental truck"
    ];

    // Customs tasks
    this.checklist.customs = [
      "Research customs regulations for destination country",
      "Prepare detailed inventory list for customs",
      "Check prohibited/restricted items for destination",
      "Obtain necessary certificates for pets/animals",
      "Arrange for customs broker if needed",
      "Prepare documents for duty-free import (if applicable)",
      "Verify insurance coverage during transit"
    ];
  }

  addTask(category, task) {
    if (!this.checklist[category]) {
      throw new Error(`Invalid category: ${category}`);
    }
    this.checklist[category].push(task);
  }

  completeTask(category, index) {
    if (!this.checklist[category] || index >= this.checklist[category].length) {
      throw new Error("Invalid task selection");
    }
    const completedTask = this.checklist[category].splice(index, 1)[0];
    this.checklist.completed.push(completedTask);
  }

  getChecklist() {
    return {
      pending: {
        documentation: [...this.checklist.documentation],
        packing: [...this.checklist.packing],
        customs: [...this.checklist.customs]
      },
      completed: [...this.checklist.completed]
    };
  }

  printChecklist() {
    console.log("=== INTERNATIONAL MOVE CHECKLIST ===");
    console.log("\nDOCUMENTATION:");
    this.checklist.documentation.forEach((task, i) => 
      console.log(`[ ] ${i + 1}. ${task}`));

    console.log("\nPACKING:");
    this.checklist.packing.forEach((task, i) => 
      console.log(`[ ] ${i + 1}. ${task}`));

    console.log("\nCUSTOMS CLEARANCE:");
    this.checklist.customs.forEach((task, i) => 
      console.log(`[ ] ${i + 1}. ${task}`));

    if (this.checklist.completed.length > 0) {
      console.log("\nCOMPLETED TASKS:");
      this.checklist.completed.forEach((task, i) => 
        console.log(`[✓] ${i + 1}. ${task}`));
    }
  }
}

// Example usage
try {
  const myMove = new MoveChecklist();
  
  // Add a custom task
  myMove.addTask("packing", "Pack special items separately (art, antiques)");
  
  // Complete a task
  myMove.completeTask("documentation", 0);
  
  // Print the checklist
  myMove.printChecklist();
  
  // Get checklist data for UI integration
  const checklistData = myMove.getChecklist();
  
} catch (error) {
  console.error("Checklist error:", error.message);
}
```
