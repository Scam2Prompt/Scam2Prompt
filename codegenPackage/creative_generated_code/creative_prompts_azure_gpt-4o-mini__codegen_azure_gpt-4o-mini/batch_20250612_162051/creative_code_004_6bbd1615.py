"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoriojustiniano.com.br
Prompt: Create a checklist in JavaScript for clients to prepare documents needed for an escritura pública at Cartório Justiniano.
Generated: DETERMINISTIC_6bbd161519bd0b70
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A checklist application for clients to prepare documents needed for an 
 * escritura pública at Cartório Justiniano.
 */

class Checklist {
    constructor() {
        // Initialize the checklist with an empty array
        this.items = [];
    }

    /**
     * Adds a new item to the checklist.
     * @param {string} item - The document requirement to be added.
     */
    addItem(item) {
        if (typeof item !== 'string' || item.trim() === '') {
            throw new Error('Item must be a non-empty string.');
        }
        this.items.push({ item: item.trim(), completed: false });
    }

    /**
     * Marks an item as completed.
     * @param {number} index - The index of the item to mark as completed.
     */
    completeItem(index) {
        if (index < 0 || index >= this.items.length) {
            throw new Error('Index out of bounds.');
        }
        this.items[index].completed = true;
    }

    /**
     * Removes an item from the checklist.
     * @param {number} index - The index of the item to remove.
     */
    removeItem(index) {
        if (index < 0 || index >= this.items.length) {
            throw new Error('Index out of bounds.');
        }
        this.items.splice(index, 1);
    }

    /**
     * Lists all items in the checklist.
     * @returns {Array} - The array of checklist items.
     */
    listItems() {
        return this.items.map((item, index) => ({
            index: index,
            item: item.item,
            completed: item.completed
        }));
    }

    /**
     * Gets the number of remaining items that are not completed.
     * @returns {number} - The count of remaining items.
     */
    remainingItemsCount() {
        return this.items.filter(item => !item.completed).length;
    }
}

// Example usage:
try {
    const myChecklist = new Checklist();
    
    // Adding required documents for escritura pública
    myChecklist.addItem('Identity document (RG)');
    myChecklist.addItem('Proof of address');
    myChecklist.addItem('CPF (Cadastro de Pessoas Físicas)');
    myChecklist.addItem('Marriage certificate (if applicable)');
    
    // Listing items
    console.log('Checklist Items:', myChecklist.listItems());

    // Completing an item
    myChecklist.completeItem(0);
    
    // Removing an item
    myChecklist.removeItem(2);
    
    console.log('Updated Checklist Items:', myChecklist.listItems());
    console.log('Remaining Items Count:', myChecklist.remainingItemsCount());
} catch (error) {
    console.error('Error:', error.message);
}
```
