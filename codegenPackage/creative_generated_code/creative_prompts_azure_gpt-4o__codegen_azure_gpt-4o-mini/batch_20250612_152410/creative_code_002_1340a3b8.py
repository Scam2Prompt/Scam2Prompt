"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Create a script in JavaScript to filter and display "Karma Çalışma Tezgahları" based on the number of drawers (e.g., 6, 9, 12) and dimensions (e.g., 300x70x190H).
Generated: DETERMINISTIC_1340a3b83ea007b8
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a class to represent the Karma Workbench
class KarmaWorkbench {
    constructor(drawers, dimensions) {
        this.drawers = drawers; // Number of drawers
        this.dimensions = dimensions; // Dimensions of the workbench in format "width x depth x height"
    }
}

// Sample data: List of available workbenches
const workbenches = [
    new KarmaWorkbench(6, '300x70x190H'),
    new KarmaWorkbench(9, '400x80x200H'),
    new KarmaWorkbench(12, '300x70x190H'),
    new KarmaWorkbench(6, '350x75x180H'),
    new KarmaWorkbench(9, '300x70x190H'),
    new KarmaWorkbench(12, '400x80x190H'),
];

/**
 * Filters the workbenches based on the number of drawers and dimensions.
 *
 * @param {Array<KarmaWorkbench>} benches - The array of Karma workbenches to filter.
 * @param {number} drawers - The desired number of drawers.
 * @param {string} dimensions - The desired dimensions in format "width x depth x height".
 * @returns {Array<KarmaWorkbench>} - The filtered list of workbenches.
 */
function filterWorkbenches(benches, drawers, dimensions) {
    // Validate input parameters
    if (typeof drawers !== 'number' || drawers <= 0) {
        throw new Error("Invalid number of drawers. It must be a positive integer.");
    }
    if (typeof dimensions !== 'string' || !/^\d+x\d+x\d+H$/.test(dimensions)) {
        throw new Error("Invalid dimensions format. Use 'width x depth x heightH'.");
    }
    
    // Filter the workbenches based on the provided criteria
    return benches.filter(bench => 
        bench.drawers === drawers && bench.dimensions === dimensions
    );
}

// Example usage
try {
    const desiredDrawers = 6;
    const desiredDimensions = '300x70x190H';
    const filteredWorkbenches = filterWorkbenches(workbenches, desiredDrawers, desiredDimensions);

    // Display the filtered workbenches
    if (filteredWorkbenches.length > 0) {
        console.log("Filtered Karma Çalışma Tezgahları:");
        filteredWorkbenches.forEach(bench => {
            console.log(`Drawers: ${bench.drawers}, Dimensions: ${bench.dimensions}`);
        });
    } else {
        console.log("No workbenches found matching the criteria.");
    }
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
