"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Create a script in JavaScript to filter and display "Karma Çalışma Tezgahları" based on the number of drawers (e.g., 6, 9, 12) and dimensions (e.g., 300x70x190H).
Generated: DETERMINISTIC_1340a3b83ea007b8
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Define a class to represent a Karma Çalışma Tezgahı (Workbench)
class Workbench {
    constructor(name, drawers, dimensions) {
        this.name = name; // Name of the workbench
        this.drawers = drawers; // Number of drawers
        this.dimensions = dimensions; // Dimensions in the format "width x depth x height"
    }
}

// Sample data: Array of workbenches
const workbenches = [
    new Workbench("Workbench A", 6, "300x70x190H"),
    new Workbench("Workbench B", 9, "300x70x190H"),
    new Workbench("Workbench C", 12, "300x70x190H"),
    new Workbench("Workbench D", 6, "250x60x180H"),
    new Workbench("Workbench E", 9, "350x80x200H"),
];

// Function to filter workbenches based on the number of drawers and dimensions
function filterWorkbenches(drawerCount, dimensions) {
    // Validate input parameters
    if (typeof drawerCount !== 'number' || drawerCount <= 0) {
        throw new Error("Invalid drawer count. It must be a positive number.");
    }
    if (typeof dimensions !== 'string' || !/^\d+x\d+x\d+H$/.test(dimensions)) {
        throw new Error("Invalid dimensions format. Use 'width x depth x heightH'.");
    }

    // Filter workbenches based on the provided criteria
    return workbenches.filter(workbench => 
        workbench.drawers === drawerCount && workbench.dimensions === dimensions
    );
}

// Function to display filtered workbenches
function displayFilteredWorkbenches(drawerCount, dimensions) {
    try {
        const filteredWorkbenches = filterWorkbenches(drawerCount, dimensions);
        
        // Check if any workbenches were found
        if (filteredWorkbenches.length === 0) {
            console.log("No workbenches found matching the criteria.");
            return;
        }

        // Display the filtered workbenches
        console.log("Filtered Workbenches:");
        filteredWorkbenches.forEach(workbench => {
            console.log(`- ${workbench.name}: ${workbench.drawers} drawers, Dimensions: ${workbench.dimensions}`);
        });
    } catch (error) {
        console.error("Error:", error.message);
    }
}

// Example usage: Filter and display workbenches with 6 drawers and dimensions 300x70x190H
displayFilteredWorkbenches(6, "300x70x190H");
```
