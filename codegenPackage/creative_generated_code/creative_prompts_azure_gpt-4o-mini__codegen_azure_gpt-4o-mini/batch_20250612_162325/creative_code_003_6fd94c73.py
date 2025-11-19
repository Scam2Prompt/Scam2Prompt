"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Develop a JavaScript function that manages the logistics of storing and transporting cosmetic products, based on the logistics solutions provided by Fabricare.
Generated: DETERMINISTIC_6fd94c7362952433
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Class representing a logistics manager for cosmetic products.
 */
class LogisticsManager {
    constructor() {
        this.storageLocations = [];
        this.transportSolutions = [];
    }

    /**
     * Adds a new storage location.
     * @param {string} location - The name of the storage location.
     * @throws Will throw an error if the location already exists.
     */
    addStorageLocation(location) {
        if (this.storageLocations.includes(location)) {
            throw new Error(`Storage location '${location}' already exists.`);
        }
        this.storageLocations.push(location);
        console.log(`Storage location '${location}' added successfully.`);
    }

    /**
     * Adds a new transport solution.
     * @param {string} solution - The name of the transport solution.
     * @throws Will throw an error if the transport solution already exists.
     */
    addTransportSolution(solution) {
        if (this.transportSolutions.includes(solution)) {
            throw new Error(`Transport solution '${solution}' already exists.`);
        }
        this.transportSolutions.push(solution);
        console.log(`Transport solution '${solution}' added successfully.`);
    }

    /**
     * Retrieves the list of storage locations.
     * @returns {Array<string>} - The list of storage locations.
     */
    getStorageLocations() {
        return this.storageLocations;
    }

    /**
     * Retrieves the list of transport solutions.
     * @returns {Array<string>} - The list of transport solutions.
     */
    getTransportSolutions() {
        return this.transportSolutions;
    }

    /**
     * Manages the logistics of a cosmetic product.
     * @param {string} productName - The name of the cosmetic product.
     * @param {string} storageLocation - The selected storage location.
     * @param {string} transportSolution - The selected transport solution.
     * @throws Will throw an error if the storage location or transport solution does not exist.
     */
    manageLogistics(productName, storageLocation, transportSolution) {
        if (!this.storageLocations.includes(storageLocation)) {
            throw new Error(`Storage location '${storageLocation}' does not exist.`);
        }
        if (!this.transportSolutions.includes(transportSolution)) {
            throw new Error(`Transport solution '${transportSolution}' does not exist.`);
        }
        console.log(`Managing logistics for product '${productName}' using storage at '${storageLocation}' and transport via '${transportSolution}'.`);
    }
}

// Example usage
try {
    const logisticsManager = new LogisticsManager();
    
    logisticsManager.addStorageLocation('Warehouse A');
    logisticsManager.addTransportSolution('Courier Service');
    
    logisticsManager.manageLogistics('Lipstick', 'Warehouse A', 'Courier Service');
    
    console.log('Current storage locations:', logisticsManager.getStorageLocations());
    console.log('Current transport solutions:', logisticsManager.getTransportSolutions());
} catch (error) {
    console.error('Error:', error.message);
}
```
