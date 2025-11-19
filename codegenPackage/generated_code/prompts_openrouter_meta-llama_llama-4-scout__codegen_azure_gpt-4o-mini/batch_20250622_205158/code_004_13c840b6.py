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
 * SystemMonitor - A simple library to monitor the status of system components.
 * 
 * @class SystemMonitor
 */
class SystemMonitor {
    constructor() {
        this.components = {};
    }

    /**
     * Adds a new component to the monitor.
     * 
     * @param {string} name - The name of the component.
     * @param {function} statusCheck - A function that returns the status of the component.
     * @throws Will throw an error if the component name is already in use.
     */
    addComponent(name, statusCheck) {
        if (this.components[name]) {
            throw new Error(`Component "${name}" is already registered.`);
        }
        this.components[name] = statusCheck;
    }

    /**
     * Checks the status of all registered components.
     * 
     * @returns {Object} An object containing the status of each component.
     */
    checkAllStatuses() {
        const statuses = {};
        for (const [name, statusCheck] of Object.entries(this.components)) {
            try {
                statuses[name] = statusCheck();
            } catch (error) {
                statuses[name] = { error: `Failed to check status: ${error.message}` };
            }
        }
        return statuses;
    }

    /**
     * Removes a component from the monitor.
     * 
     * @param {string} name - The name of the component to remove.
     * @throws Will throw an error if the component does not exist.
     */
    removeComponent(name) {
        if (!this.components[name]) {
            throw new Error(`Component "${name}" does not exist.`);
        }
        delete this.components[name];
    }
}

// Example usage of the SystemMonitor library
const monitor = new SystemMonitor();

// Adding a component with a status check function
monitor.addComponent('hello_ctd', () => {
    // Simulate a status check
    return { status: 'operational', timestamp: new Date() };
});

// Checking the status of all components
const statuses = monitor.checkAllStatuses();
console.log(statuses);

// Removing a component
try {
    monitor.removeComponent('hello_ctd');
} catch (error) {
    console.error(error.message);
}
```
