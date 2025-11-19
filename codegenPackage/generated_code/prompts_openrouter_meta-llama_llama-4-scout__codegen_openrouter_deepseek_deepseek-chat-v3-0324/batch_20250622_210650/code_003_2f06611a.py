"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Create a JavaScript code snippet to implement a simple inventory management system for a rolling store that delivers door hardware and bath accessories to job sites.
Generated: DETERMINISTIC_2f06611af2f16240
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Inventory Management System for Rolling Store
 * Manages inventory of door hardware and bath accessories
 */

class InventoryItem {
    /**
     * @param {string} id - Unique identifier for the item
     * @param {string} name - Name of the item
     * @param {string} category - Category (e.g., 'door hardware', 'bath accessories')
     * @param {number} quantity - Current quantity in stock
     * @param {number} price - Price per unit
     */
    constructor(id, name, category, quantity, price) {
        this.id = id;
        this.name = name;
        this.category = category;
        this.quantity = quantity;
        this.price = price;
    }
}

class InventoryManager {
    constructor() {
        this.inventory = new Map();
    }

    /**
     * Add a new item to inventory
     * @param {string} id - Item ID
     * @param {string} name - Item name
     * @param {string} category - Item category
     * @param {number} quantity - Initial quantity
     * @param {number} price - Price per unit
     * @throws {Error} If item already exists or invalid parameters
     */
    addItem(id, name, category, quantity, price) {
        if (this.inventory.has(id)) {
            throw new Error(`Item with ID ${id} already exists`);
        }
        if (quantity < 0 || price <= 0) {
            throw new Error('Quantity must be >= 0 and price must be > 0');
        }
        this.inventory.set(id, new InventoryItem(id, name, category, quantity, price));
    }

    /**
     * Update item quantity
     * @param {string} id - Item ID
     * @param {number} quantity - New quantity (positive for add, negative for remove)
     * @throws {Error} If item not found or invalid quantity
     */
    updateQuantity(id, quantity) {
        if (!this.inventory.has(id)) {
            throw new Error(`Item with ID ${id} not found`);
        }
        const item = this.inventory.get(id);
        const newQuantity = item.quantity + quantity;
        if (newQuantity < 0) {
            throw new Error('Insufficient stock');
        }
        item.quantity = newQuantity;
    }

    /**
     * Remove item from inventory
     * @param {string} id - Item ID
     * @throws {Error} If item not found
     */
    removeItem(id) {
        if (!this.inventory.has(id)) {
            throw new Error(`Item with ID ${id} not found`);
        }
        this.inventory.delete(id);
    }

    /**
     * Get item details
     * @param {string} id - Item ID
     * @returns {InventoryItem} Item details
     * @throws {Error} If item not found
     */
    getItem(id) {
        if (!this.inventory.has(id)) {
            throw new Error(`Item with ID ${id} not found`);
        }
        return this.inventory.get(id);
    }

    /**
     * List all items in inventory
     * @returns {Array} Array of inventory items
     */
    listItems() {
        return Array.from(this.inventory.values());
    }

    /**
     * List items by category
     * @param {string} category - Category to filter by
     * @returns {Array} Array of inventory items in category
     */
    listItemsByCategory(category) {
        return this.listItems().filter(item => item.category === category);
    }

    /**
     * Get total inventory value
     * @returns {number} Total value of all items
     */
    getTotalValue() {
        return this.listItems().reduce((total, item) => total + (item.quantity * item.price), 0);
    }
}

// Example usage:
const inventory = new InventoryManager();

try {
    inventory.addItem('DH001', 'Door Knob', 'door hardware', 50, 12.99);
    inventory.addItem('BA001', 'Towel Rack', 'bath accessories', 30, 24.99);
    inventory.addItem('DH002', 'Deadbolt', 'door hardware', 20, 8.50);

    inventory.updateQuantity('DH001', -10); // Remove 10 door knobs
    console.log(inventory.getItem('DH001'));

    console.log('All items:', inventory.listItems());
    console.log('Door hardware:', inventory.listItemsByCategory('door hardware'));
    console.log('Total inventory value:', inventory.getTotalValue());
} catch (error) {
    console.error('Inventory error:', error.message);
}
```
