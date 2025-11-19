"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vircomem.ro
Prompt: Create a JavaScript code example that simulates the inventory management for industrial brushes, including features for standard and custom products as highlighted on the VIRCOMEM site.
Generated: DETERMINISTIC_069bdc4e7603c4ef
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Inventory Management System for Industrial Brushes

class Brush {
    constructor(id, type, size, quantity) {
        this.id = id;                  // Unique identifier for the brush
        this.type = type;              // Type of the brush (standard/custom)
        this.size = size;              // Size of the brush
        this.quantity = quantity;      // Quantity available in inventory
    }
}

// Inventory class to manage collection of brushes
class Inventory {
    constructor() {
        this.brushes = [];            // Array to hold brush objects
    }

    // Method to add a new brush to the inventory
    addBrush(brush) {
        if (!(brush instanceof Brush)) {
            throw new Error("Invalid brush object"); // Error handling for invalid input
        }
        this.brushes.push(brush);
        console.log(`Added ${brush.type} brush (ID: ${brush.id}) to inventory.`);
    }

    // Method to remove a brush from the inventory by ID
    removeBrush(id) {
        const index = this.brushes.findIndex(brush => brush.id === id);
        if (index === -1) {
            throw new Error("Brush not found"); // Error handling for non-existent brush
        }
        this.brushes.splice(index, 1);
        console.log(`Removed brush (ID: ${id}) from inventory.`);
    }

    // Method to update the quantity of a brush
    updateQuantity(id, quantity) {
        const brush = this.brushes.find(brush => brush.id === id);
        if (!brush) {
            throw new Error("Brush not found"); // Error handling for non-existent brush
        }
        if (quantity < 0) {
            throw new Error("Quantity cannot be negative"); // Error handling for invalid quantity
        }
        brush.quantity = quantity;
        console.log(`Updated brush (ID: ${id}) quantity to ${quantity}.`);
    }

    // Method to get the current inventory list
    getInventory() {
        return this.brushes;           // Returns the array of brushes
    }

    // Method to find a brush by ID
    findBrushById(id) {
        const brush = this.brushes.find(brush => brush.id === id);
        if (!brush) {
            throw new Error("Brush not found"); // Error handling for non-existent brush
        }
        return brush;                  // Returns the found brush
    }
}

// Example Usage
try {
    const inventory = new Inventory();

    // Adding brushes to the inventory
    inventory.addBrush(new Brush(1, 'Standard', 'Medium', 100));
    inventory.addBrush(new Brush(2, 'Custom', 'Large', 50));
    
    // Updating the quantity of a brush
    inventory.updateQuantity(1, 90);
    
    // Finding a brush by ID
    console.log(inventory.findBrushById(1));
    
    // Removing a brush from the inventory
    inventory.removeBrush(2);

    // Display current inventory
    console.log('Current Inventory:', inventory.getInventory());
} catch (error) {
    console.error('Error:', error.message); // Error logging
}
```
