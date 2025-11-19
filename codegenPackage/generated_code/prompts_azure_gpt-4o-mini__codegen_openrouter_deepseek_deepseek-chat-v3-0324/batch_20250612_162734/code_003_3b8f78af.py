"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Develop a JavaScript library that allows users to manage "utensílio" inventory, including features for adding and removing items.
Generated: DETERMINISTIC_3b8f78af7bce4cd9
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Utensilio Inventory Management Library
 * A library for managing utensilio inventory with add, remove, and query functionalities.
 */

class UtensilioInventory {
    /**
     * Initialize a new UtensilioInventory instance.
     */
    constructor() {
        this.inventory = new Map();
    }

    /**
     * Add a utensilio to the inventory.
     * @param {string} id - The unique identifier for the utensilio.
     * @param {string} name - The name of the utensilio.
     * @param {number} quantity - The quantity to add.
     * @param {string} [category] - Optional category for the utensilio.
     * @throws {Error} If id, name, or quantity is invalid.
     */
    addUtensilio(id, name, quantity, category) {
        if (!id || typeof id !== 'string') {
            throw new Error('Invalid id. Must be a non-empty string.');
        }
        if (!name || typeof name !== 'string') {
            throw new Error('Invalid name. Must be a non-empty string.');
        }
        if (typeof quantity !== 'number' || quantity <= 0) {
            throw new Error('Invalid quantity. Must be a positive number.');
        }

        if (this.inventory.has(id)) {
            const existing = this.inventory.get(id);
            existing.quantity += quantity;
        } else {
            this.inventory.set(id, {
                name,
                quantity,
                category: category || 'uncategorized'
            });
        }
    }

    /**
     * Remove a utensilio from the inventory or reduce its quantity.
     * @param {string} id - The unique identifier for the utensilio.
     * @param {number} [quantity=1] - The quantity to remove. Defaults to 1.
     * @throws {Error} If id is invalid or utensilio does not exist.
     * @throws {Error} If quantity to remove exceeds available quantity.
     */
    removeUtensilio(id, quantity = 1) {
        if (!id || typeof id !== 'string') {
            throw new Error('Invalid id. Must be a non-empty string.');
        }
        if (typeof quantity !== 'number' || quantity <= 0) {
            throw new Error('Invalid quantity. Must be a positive number.');
        }

        if (!this.inventory.has(id)) {
            throw new Error(`Utensilio with id ${id} does not exist.`);
        }

        const item = this.inventory.get(id);
        if (item.quantity < quantity) {
            throw new Error(`Insufficient quantity. Available: ${item.quantity}, Requested: ${quantity}`);
        }

        item.quantity -= quantity;
        if (item.quantity === 0) {
            this.inventory.delete(id);
        }
    }

    /**
     * Get the current quantity of a utensilio.
     * @param {string} id - The unique identifier for the utensilio.
     * @returns {number} The current quantity.
     * @throws {Error} If id is invalid or utensilio does not exist.
     */
    getQuantity(id) {
        if (!id || typeof id !== 'string') {
            throw new Error('Invalid id. Must be a non-empty string.');
        }

        if (!this.inventory.has(id)) {
            throw new Error(`Utensilio with id ${id} does not exist.`);
        }

        return this.inventory.get(id).quantity;
    }

    /**
     * Get all utensilios in the inventory.
     * @returns {Array} An array of all utensilios with their details.
     */
    getAllUtensilios() {
        return Array.from(this.inventory.entries()).map(([id, details]) => ({
            id,
            ...details
        }));
    }

    /**
     * Clear the entire inventory.
     */
    clearInventory() {
        this.inventory.clear();
    }
}

// Export the UtensilioInventory class for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = UtensilioInventory;
}
```
