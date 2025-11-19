"""
Generated Code Metadata:
========================
Original URL: https://tabriz3dprint.ir
Prompt: Develop a JavaScript code to simulate the 3D printing process, taking into account the print speed, layer thickness, and material properties, similar to those used by Tabriz 3D Print.
Generated: DETERMINISTIC_bbfa6b34572449ab
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * 3DPrinter class simulates the 3D printing process.
 */
class 3DPrinter {
    constructor(printSpeed, layerThickness, materialProperties) {
        this.printSpeed = printSpeed; // in mm/s
        this.layerThickness = layerThickness; // in mm
        this.materialProperties = materialProperties; // object containing material properties
        this.currentLayer = 0; // tracks the current layer being printed
        this.totalLayers = 0; // total layers to print
    }

    /**
     * Initializes the printing process.
     * @param {number} totalHeight - The total height of the object to be printed in mm.
     */
    startPrinting(totalHeight) {
        if (totalHeight <= 0) {
            throw new Error("Total height must be greater than zero.");
        }

        this.totalLayers = Math.ceil(totalHeight / this.layerThickness);
        console.log(`Starting print: ${this.totalLayers} layers to print.`);
        
        this.printLayers();
    }

    /**
     * Simulates the printing of each layer.
     */
    printLayers() {
        for (this.currentLayer = 1; this.currentLayer <= this.totalLayers; this.currentLayer++) {
            this.printLayer(this.currentLayer);
        }
        console.log("Printing completed successfully.");
    }

    /**
     * Simulates the printing of a single layer.
     * @param {number} layer - The current layer number being printed.
     */
    printLayer(layer) {
        console.log(`Printing layer ${layer}...`);
        
        // Simulate the time taken to print the layer
        const timeToPrint = this.layerThickness / this.printSpeed; // in seconds
        this.simulateDelay(timeToPrint);
        
        console.log(`Layer ${layer} printed successfully.`);
    }

    /**
     * Simulates a delay for the printing process.
     * @param {number} seconds - The time to delay in seconds.
     */
    simulateDelay(seconds) {
        const start = Date.now();
        while (Date.now() - start < seconds * 1000) {
            // Busy-waiting to simulate delay
        }
    }
}

// Example usage:
try {
    const materialProperties = {
        name: "PLA",
        density: 1.24, // g/cm^3
        meltingPoint: 180 // degrees Celsius
    };

    const printer = new 3DPrinter(50, 0.2, materialProperties);
    printer.startPrinting(20); // Print an object with a total height of 20 mm
} catch (error) {
    console.error("Error during printing:", error.message);
}
```
