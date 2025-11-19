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
 * 3D Printing Simulation Class
 * Simulates a 3D printing process with configurable parameters
 */
class ThreeDPrinterSimulation {
    /**
     * @param {Object} config - Configuration object
     * @param {number} config.printSpeed - Printing speed in mm/s
     * @param {number} config.layerThickness - Layer thickness in mm
     * @param {string} config.materialType - Printing material type
     * @param {Object} materialProperties - Material properties
     * @param {number} materialProperties.meltingPoint - Material melting point in °C
     * @param {number} materialProperties.density - Material density in g/cm³
     * @param {number} materialProperties.thermalConductivity - Thermal conductivity in W/m·K
     */
    constructor(config, materialProperties) {
        if (!config || !materialProperties) {
            throw new Error('Configuration and material properties are required');
        }

        this.printSpeed = config.printSpeed || 50;
        this.layerThickness = config.layerThickness || 0.2;
        this.materialType = config.materialType || 'PLA';
        this.materialProperties = materialProperties;

        this.currentLayer = 0;
        this.totalLayers = 0;
        this.printTime = 0;
        this.isPrinting = false;
        this.printProgress = 0;
    }

    /**
     * Calculate total print time based on model height
     * @param {number} modelHeight - Model height in mm
     * @returns {number} Total print time in seconds
     */
    calculatePrintTime(modelHeight) {
        if (modelHeight <= 0) {
            throw new Error('Model height must be greater than 0');
        }

        this.totalLayers = Math.ceil(modelHeight / this.layerThickness);
        const timePerLayer = 1000 / this.printSpeed; // Simplified estimation
        return this.totalLayers * timePerLayer;
    }

    /**
     * Start the printing simulation
     * @param {number} modelHeight - Model height in mm
     * @param {Function} progressCallback - Callback for progress updates
     * @returns {Promise<void>} Resolves when printing is complete
     */
    async startPrinting(modelHeight, progressCallback) {
        if (this.isPrinting) {
            throw new Error('Printing is already in progress');
        }

        this.isPrinting = true;
        this.printTime = this.calculatePrintTime(modelHeight);
        this.currentLayer = 0;
        this.printProgress = 0;

        const layerInterval = this.printTime / this.totalLayers;

        return new Promise((resolve) => {
            const printInterval = setInterval(() => {
                this.currentLayer++;
                this.printProgress = (this.currentLayer / this.totalLayers) * 100;

                if (progressCallback) {
                    progressCallback({
                        layer: this.currentLayer,
                        totalLayers: this.totalLayers,
                        progress: this.printProgress,
                        timeElapsed: this.currentLayer * layerInterval
                    });
                }

                if (this.currentLayer >= this.totalLayers) {
                    clearInterval(printInterval);
                    this.isPrinting = false;
                    resolve();
                }
            }, layerInterval * 1000);
        });
    }

    /**
     * Pause the printing process
     */
    pausePrinting() {
        if (!this.isPrinting) {
            throw new Error('No active print job to pause');
        }
        this.isPrinting = false;
    }

    /**
     * Resume the printing process
     */
    resumePrinting() {
        if (this.isPrinting) {
            throw new Error('Printing is already in progress');
        }
        this.isPrinting = true;
    }

    /**
     * Get current print status
     * @returns {Object} Current print status
     */
    getStatus() {
        return {
            isPrinting: this.isPrinting,
            currentLayer: this.currentLayer,
            totalLayers: this.totalLayers,
            progress: this.printProgress,
            printSpeed: this.printSpeed,
            layerThickness: this.layerThickness,
            materialType: this.materialType
        };
    }
}

// Example usage:
/*
const printerConfig = {
    printSpeed: 60,
    layerThickness: 0.15,
    materialType: 'ABS'
};

const materialProps = {
    meltingPoint: 240,
    density: 1.04,
    thermalConductivity: 0.18
};

const printer = new ThreeDPrinterSimulation(printerConfig, materialProps);

printer.startPrinting(20, (status) => {
    console.log(`Layer ${status.layer} of ${status.totalLayers} - ${status.progress.toFixed(1)}% complete`);
}).then(() => {
    console.log('Printing completed!');
}).catch((err) => {
    console.error('Printing error:', err);
});
*/
```
