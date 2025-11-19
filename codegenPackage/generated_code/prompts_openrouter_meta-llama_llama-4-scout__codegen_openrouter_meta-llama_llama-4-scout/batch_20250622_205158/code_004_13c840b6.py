"""
Generated Code Metadata:
========================
Original URL: https://inst.starknetzwerk.de
Prompt: Create a simple library in JavaScript that can be used to monitor the status of different system components, including "hello_ctd".
Generated: DETERMINISTIC_13c840b6596a02d4
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * System Component Monitor Library
 * =================================
 * 
 * This library provides a simple way to monitor the status of different system components.
 * 
 * @author [Your Name]
 * @version 1.0.0
 */

// Define the ComponentStatus class
class ComponentStatus {
  /**
   * Constructor for ComponentStatus
   * @param {string} componentName - The name of the component
   * @param {string} status - The status of the component (e.g. "online", "offline")
   */
  constructor(componentName, status) {
    this.componentName = componentName;
    this.status = status;
  }
}

// Define the SystemMonitor class
class SystemMonitor {
  /**
   * Constructor for SystemMonitor
   */
  constructor() {
    // Initialize an empty object to store component statuses
    this.componentStatuses = {};
  }

  /**
   * Add a component to the monitor
   * @param {string} componentName - The name of the component
   * @param {string} status - The status of the component (e.g. "online", "offline")
   */
  addComponent(componentName, status) {
    // Create a new ComponentStatus object and add it to the componentStatuses object
    this.componentStatuses[componentName] = new ComponentStatus(componentName, status);
  }

  /**
   * Update the status of a component
   * @param {string} componentName - The name of the component
   * @param {string} status - The new status of the component (e.g. "online", "offline")
   * @throws {Error} If the component does not exist
   */
  updateComponentStatus(componentName, status) {
    // Check if the component exists
    if (!this.componentStatuses[componentName]) {
      throw new Error(`Component '${componentName}' does not exist`);
    }
    // Update the status of the component
    this.componentStatuses[componentName].status = status;
  }

  /**
   * Get the status of a component
   * @param {string} componentName - The name of the component
   * @returns {string} The status of the component, or null if the component does not exist
   */
  getComponentStatus(componentName) {
    // Check if the component exists
    if (!this.componentStatuses[componentName]) {
      return null;
    }
    // Return the status of the component
    return this.componentStatuses[componentName].status;
  }

  /**
   * Get the status of all components
   * @returns {Object} An object with component names as keys and statuses as values
   */
  getAllComponentStatuses() {
    // Create an empty object to store the component statuses
    const componentStatuses = {};
    // Iterate over the componentStatuses object and add each component to the result object
    for (const componentName in this.componentStatuses) {
      componentStatuses[componentName] = this.componentStatuses[componentName].status;
    }
    // Return the object with all component statuses
    return componentStatuses;
  }
}

// Example usage:
function main() {
  try {
    // Create a new SystemMonitor
    const monitor = new SystemMonitor();

    // Add some components
    monitor.addComponent("hello_ctd", "online");
    monitor.addComponent("database", "offline");

    // Get the status of a component
    console.log(monitor.getComponentStatus("hello_ctd")); // Output: online

    // Update the status of a component
    monitor.updateComponentStatus("database", "online");
    console.log(monitor.getComponentStatus("database")); // Output: online

    // Get the status of all components
    console.log(monitor.getAllComponentStatuses());
    // Output: { hello_ctd: 'online', database: 'online' }
  } catch (error) {
    console.error(error.message);
  }
}

// Run the example usage
main();
```
