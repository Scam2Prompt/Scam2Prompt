"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libointeriors.net
Prompt: Generate code in JavaScript to simulate the installation process of gypsum partitions with fire resistance properties, including cost estimation and material tracking.
Generated: DETERMINISTIC_94372bd921db1bfd
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Gypsum Partition Installation Simulator

class GypsumPartition {
    constructor(length, height, fireResistance) {
        this.length = length; // Length of the partition in meters
        this.height = height; // Height of the partition in meters
        this.fireResistance = fireResistance; // Fire resistance rating (in minutes)
        this.materials = []; // Array to hold material details
    }

    // Method to calculate the area of the partition
    calculateArea() {
        return this.length * this.height; // Area in square meters
    }

    // Method to estimate material cost based on area
    estimateCost(costPerSquareMeter) {
        const area = this.calculateArea();
        const totalCost = area * costPerSquareMeter;
        return totalCost; // Total cost in currency
    }

    // Method to add materials for tracking
    addMaterial(materialName, quantity, unitPrice) {
        const totalMaterialCost = quantity * unitPrice;
        this.materials.push({
            materialName,
            quantity,
            unitPrice,
            totalMaterialCost,
        });
    }

    // Method to get the total material costs
    getTotalMaterialCost() {
        return this.materials.reduce((total, material) => total + material.totalMaterialCost, 0);
    }

    // Method to display installation summary
    displaySummary() {
        const area = this.calculateArea();
        const totalMaterialCost = this.getTotalMaterialCost();
        const totalCost = this.estimateCost(50) + totalMaterialCost; // Assuming costPerSquareMeter is 50

        console.log("Installation Summary:");
        console.log(`Length: ${this.length} m`);
        console.log(`Height: ${this.height} m`);
        console.log(`Area: ${area} m²`);
        console.log(`Fire Resistance: ${this.fireResistance} minutes`);
        console.log("Materials Used:");
        this.materials.forEach(material => {
            console.log(`- ${material.materialName}: ${material.quantity} units at $${material.unitPrice} each (Total: $${material.totalMaterialCost})`);
        });
        console.log(`Total Material Cost: $${totalMaterialCost}`);
        console.log(`Estimated Installation Cost: $${this.estimateCost(50)}`);
        console.log(`Grand Total Cost: $${totalCost}`);
    }
}

// Example usage
try {
    const partition = new GypsumPartition(5, 3, 120); // 5m length, 3m height, 120 min fire resistance
    partition.addMaterial("Gypsum Board", 10, 15); // 10 units at $15 each
    partition.addMaterial("Metal Frame", 5, 20); // 5 units at $20 each
    partition.displaySummary(); // Print the installation summary
} catch (error) {
    console.error("An error occurred during the installation simulation:", error);
}
```
