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
/**
 * Industrial Brush Inventory Management System
 * 
 * This script simulates inventory management for standard and custom industrial brushes.
 * It includes features for adding, updating, and querying brush inventory.
 */

class IndustrialBrush {
    /**
     * @param {string} sku - Stock Keeping Unit identifier
     * @param {string} name - Brush name/description
     * @param {string} type - Brush type (standard/custom)
     * @param {number} quantity - Current stock quantity
     * @param {number} price - Unit price
     * @param {Object} [specs] - Additional specifications (for custom brushes)
     */
    constructor(sku, name, type, quantity, price, specs = {}) {
        this.sku = sku;
        this.name = name;
        this.type = type;
        this.quantity = quantity;
        this.price = price;
        this.specs = specs;
        this.lastUpdated = new Date();
    }

    /**
     * Updates brush inventory quantity
     * @param {number} amount - Positive to add, negative to subtract
     * @throws {Error} If resulting quantity would be negative
     */
    updateQuantity(amount) {
        if (this.quantity + amount < 0) {
            throw new Error(`Insufficient stock for ${this.sku}. Current: ${this.quantity}, Attempted: ${amount}`);
        }
        this.quantity += amount;
        this.lastUpdated = new Date();
    }

    /**
     * Returns brush details as an object
     * @returns {Object} Brush details
     */
    getDetails() {
        return {
            sku: this.sku,
            name: this.name,
            type: this.type,
            quantity: this.quantity,
            price: this.price,
            specs: this.specs,
            lastUpdated: this.lastUpdated
        };
    }
}

class BrushInventoryManager {
    constructor() {
        this.inventory = new Map();
    }

    /**
     * Adds a new brush to inventory
     * @param {IndustrialBrush} brush - Brush to add
     * @throws {Error} If SKU already exists
     */
    addBrush(brush) {
        if (this.inventory.has(brush.sku)) {
            throw new Error(`SKU ${brush.sku} already exists in inventory`);
        }
        this.inventory.set(brush.sku, brush);
    }

    /**
     * Gets brush by SKU
     * @param {string} sku - SKU to search for
     * @returns {IndustrialBrush|null} Found brush or null
     */
    getBrush(sku) {
        return this.inventory.get(sku) || null;
    }

    /**
     * Updates brush quantity by SKU
     * @param {string} sku - SKU to update
     * @param {number} amount - Amount to adjust by
     * @throws {Error} If brush not found or invalid quantity
     */
    updateBrushQuantity(sku, amount) {
        const brush = this.getBrush(sku);
        if (!brush) {
            throw new Error(`Brush with SKU ${sku} not found`);
        }
        brush.updateQuantity(amount);
    }

    /**
     * Gets all brushes of a specific type
     * @param {string} type - Brush type to filter by
     * @returns {Array} Array of matching brushes
     */
    getBrushesByType(type) {
        return Array.from(this.inventory.values()).filter(brush => brush.type === type);
    }

    /**
     * Generates inventory report
     * @returns {Object} Inventory summary
     */
    generateInventoryReport() {
        const report = {
            totalBrushes: this.inventory.size,
            totalQuantity: 0,
            totalValue: 0,
            byType: {
                standard: { count: 0, quantity: 0, value: 0 },
                custom: { count: 0, quantity: 0, value: 0 }
            }
        };

        this.inventory.forEach(brush => {
            const brushValue = brush.quantity * brush.price;
            report.totalQuantity += brush.quantity;
            report.totalValue += brushValue;

            const typeKey = brush.type.toLowerCase();
            if (report.byType[typeKey]) {
                report.byType[typeKey].count++;
                report.byType[typeKey].quantity += brush.quantity;
                report.byType[typeKey].value += brushValue;
            }
        });

        return report;
    }
}

// Example Usage
try {
    const inventoryManager = new BrushInventoryManager();

    // Add standard brushes
    inventoryManager.addBrush(new IndustrialBrush(
        'STD-001',
        'Standard Wire Brush',
        'standard',
        100,
        12.99
    ));

    inventoryManager.addBrush(new IndustrialBrush(
        'STD-002',
        'Nylon Bristle Brush',
        'standard',
        75,
        8.49
    ));

    // Add custom brushes
    inventoryManager.addBrush(new IndustrialBrush(
        'CUST-001',
        'Custom Steel Brush',
        'custom',
        25,
        24.99,
        {
            material: 'high-carbon steel',
            bristleLength: '50mm',
            handleType: 'ergonomic'
        }
    ));

    inventoryManager.addBrush(new IndustrialBrush(
        'CUST-002',
        'Specialty Cleaning Brush',
        'custom',
        15,
        32.50,
        {
            material: 'nylon/stainless steel',
            bristleLength: '75mm',
            handleType: 'long-reach'
        }
    ));

    // Update quantities
    inventoryManager.updateBrushQuantity('STD-001', -10); // Sell 10
    inventoryManager.updateBrushQuantity('CUST-001', 5); // Add 5 to stock

    // Generate report
    const report = inventoryManager.generateInventoryReport();
    console.log('Inventory Report:', report);

    // Get brush details
    const brushDetails = inventoryManager.getBrush('CUST-002').getDetails();
    console.log('Brush Details:', brushDetails);

} catch (error) {
    console.error('Inventory Error:', error.message);
}
```
