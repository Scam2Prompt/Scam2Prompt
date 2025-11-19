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
 * UtensilioInventory - A simple library for managing utensil inventory.
 * 
 * This library allows users to add and remove utensils from their inventory.
 * It also provides methods to list all utensils and check the total count.
 */

class UtensilioInventory {
    constructor() {
        // Initialize an empty inventory
        this.inventory = [];
    }

    /**
     * Adds a utensil to the inventory.
     * @param {string} utensil - The name of the utensil to add.
     * @throws {Error} Will throw an error if the utensil already exists.
     */
    addUtensil(utensil) {
        if (this.inventory.includes(utensil)) {
            throw new Error(`Utensil "${utensil}" already exists in the inventory.`);
        }
        this.inventory.push(utensil);
        console.log(`Utensil "${utensil}" added to the inventory.`);
    }

    /**
     * Removes a utensil from the inventory.
     * @param {string} utensil - The name of the utensil to remove.
     * @throws {Error} Will throw an error if the utensil does not exist.
     */
    removeUtensil(utensil) {
        const index = this.inventory.indexOf(utensil);
        if (index === -1) {
            throw new Error(`Utensil "${utensil}" does not exist in the inventory.`);
        }
        this.inventory.splice(index, 1);
        console.log(`Utensil "${utensil}" removed from the inventory.`);
    }

    /**
     * Lists all utensils in the inventory.
     * @returns {Array} An array of utensils in the inventory.
     */
    listUtensils() {
        return this.inventory.slice(); // Return a copy of the inventory
    }

    /**
     * Gets the total count of utensils in the inventory.
     * @returns {number} The total number of utensils.
     */
    getTotalCount() {
        return this.inventory.length;
    }
}

// Example usage
try {
    const myInventory = new UtensilioInventory();
    myInventory.addUtensil('Spoon');
    myInventory.addUtensil('Fork');
    console.log(myInventory.listUtensils()); // ['Spoon', 'Fork']
    console.log(`Total utensils: ${myInventory.getTotalCount()}`); // 2
    myInventory.removeUtensil('Spoon');
    console.log(myInventory.listUtensils()); // ['Fork']
} catch (error) {
    console.error(error.message);
}
```
