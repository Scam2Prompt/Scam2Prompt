"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Create a JavaScript code example that simulates the inventory management for industrial brushes, including features for standard and custom products as highlighted on the VIRCOMEM site.
Generated: DETERMINISTIC_069bdc4e7603c4ef
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Inventory Management for Industrial Brushes

class Brush {
    /**
     * Represents an industrial brush.
     * @param {string} id - Unique identifier for the brush.
     * @param {string} type - Type of brush (standard/custom).
     * @param {string} description - Description of the brush.
     * @param {number} quantity - Quantity of brushes in stock.
     * @param {number} price - Price of a single brush.
     */
    constructor(id, type, description, quantity, price) {
        this.id = id;
        this.type = type;
        this.description = description;
        this.quantity = quantity;
        this.price = price;
    }
}

class Inventory {
    /**
     * Represents the inventory of industrial brushes.
     */
    constructor() {
        this.brushes = [];
    }

    /**
     * Adds a brush to the inventory.
     * @param {Brush} brush - The brush to add.
     */
    addBrush(brush) {
        this.brushes.push(brush);
    }

    /**
     * Removes a brush from the inventory by ID.
     * @param {string} id - The ID of the brush to remove.
     * @returns {boolean} True if the brush was removed, false otherwise.
     */
    removeBrush(id) {
        const index = this.brushes.findIndex(brush => brush.id === id);
        if (index !== -1) {
            this.brushes.splice(index, 1);
            return true;
        }
        return false;
    }

    /**
     * Updates the quantity of a brush in the inventory.
     * @param {string} id - The ID of the brush to update.
     * @param {number} newQuantity - The new quantity of the brush.
     * @returns {boolean} True if the quantity was updated, false otherwise.
     */
    updateQuantity(id, newQuantity) {
        const brush = this.brushes.find(b => b.id === id);
        if (brush) {
            brush.quantity = newQuantity;
            return true;
        }
        return false;
    }

    /**
     * Gets a brush from the inventory by ID.
     * @param {string} id - The ID of the brush to get.
     * @returns {Brush|null} The brush with the given ID, or null if not found.
     */
    getBrush(id) {
        return this.brushes.find(brush => brush.id === id) || null;
    }

    /**
     * Lists all brushes in the inventory.
     * @returns {Brush[]} An array of all brushes in the inventory.
     */
    listBrushes() {
        return this.brushes;
    }
}

class StandardBrush extends Brush {
    /**
     * Represents a standard industrial brush.
     * @param {string} id - Unique identifier for the brush.
     * @param {string} description - Description of the brush.
     * @param {number} quantity - Quantity of brushes in stock.
     * @param {number} price - Price of a single brush.
     * @param {string} size - Size of the brush.
     * @param {string} material - Material of the brush.
     */
    constructor(id, description, quantity, price, size, material) {
        super(id, 'standard', description, quantity, price);
        this.size = size;
        this.material = material;
    }
}

class CustomBrush extends Brush {
    /**
     * Represents a custom industrial brush.
     * @param {string} id - Unique identifier for the brush.
     * @param {string} description - Description of the brush.
     * @param {number} quantity - Quantity of brushes in stock.
     * @param {number} price - Price of a single brush.
     * @param {string} specifications - Custom specifications of the brush.
     */
    constructor(id, description, quantity, price, specifications) {
        super(id, 'custom', description, quantity, price);
        this.specifications = specifications;
    }
}

// Example usage:
function main() {
    try {
        const inventory = new Inventory();

        const standardBrush = new StandardBrush('SB001', 'Standard brush for general use', 100, 9.99, '10cm', 'nylon');
        const customBrush = new CustomBrush('CB001', 'Custom brush for specific use', 50, 19.99, 'Special size and material');

        inventory.addBrush(standardBrush);
        inventory.addBrush(customBrush);

        console.log('Brushes in inventory:');
        inventory.listBrushes().forEach(brush => {
            console.log(`ID: ${brush.id}, Type: ${brush.type}, Description: ${brush.description}, Quantity: ${brush.quantity}, Price: $${brush.price}`);
            if (brush.type === 'standard') {
                const stdBrush = brush;
                console.log(`  Size: ${stdBrush.size}, Material: ${stdBrush.material}`);
            } else if (brush.type === 'custom') {
                const custom = brush;
                console.log(`  Specifications: ${custom.specifications}`);
            }
        });

        // Update quantity and remove a brush
        inventory.updateQuantity('SB001', 80);
        console.log('Updated quantity of SB001 to 80');

        if (inventory.removeBrush('CB001')) {
            console.log('Removed CB001 from inventory');
        } else {
            console.log('Failed to remove CB001 from inventory');
        }
    } catch (error) {
        console.error('Error:', error.message);
    }
}

main();
```
