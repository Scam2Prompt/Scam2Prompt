"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Write JavaScript code to implement a "Recently Viewed" section for an e-commerce website, dynamically updating based on user activity, as seen on Multan Designs.
Generated: DETERMINISTIC_02d8bfe281a9ac04
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Recently Viewed Items Module
class RecentlyViewed {
    constructor(storageKey = 'recentlyViewedItems', maxItems = 5) {
        this.storageKey = storageKey;
        this.maxItems = maxItems;
        this.items = this.loadItems();
    }

    // Load items from local storage
    loadItems() {
        try {
            const items = JSON.parse(localStorage.getItem(this.storageKey));
            return Array.isArray(items) ? items : [];
        } catch (error) {
            console.error('Error loading recently viewed items:', error);
            return [];
        }
    }

    // Save items to local storage
    saveItems() {
        try {
            localStorage.setItem(this.storageKey, JSON.stringify(this.items));
        } catch (error) {
            console.error('Error saving recently viewed items:', error);
        }
    }

    // Add a new item to the recently viewed items
    addItem(item) {
        // Ensure item is valid
        if (!item || !item.id) {
            console.warn('Invalid item:', item);
            return;
        }

        // Remove item if it already exists
        this.items = this.items.filter(existingItem => existingItem.id !== item.id);

        // Add the new item at the start
        this.items.unshift(item);

        // Limit the number of items
        if (this.items.length > this.maxItems) {
            this.items.pop(); // Remove the oldest item
        }

        // Save the updated list to local storage
        this.saveItems();
    }

    // Get the list of recently viewed items
    getItems() {
        return this.items;
    }

    // Render the recently viewed items to the DOM
    render(containerId) {
        const container = document.getElementById(containerId);
        if (!container) {
            console.error('Container not found:', containerId);
            return;
        }

        // Clear the existing items
        container.innerHTML = '';

        // Create and append each item to the container
        this.items.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.className = 'recently-viewed-item';
            itemElement.innerHTML = `
                <h3>${item.name}</h3>
                <p>${item.description}</p>
                <a href="${item.url}">View</a>
            `;
            container.appendChild(itemElement);
        });
    }
}

// Usage example
const recentlyViewed = new RecentlyViewed();

// Example item to add
const exampleItem = {
    id: '123',
    name: 'Sample Product',
    description: 'This is a sample product description.',
    url: '/product/123'
};

// Add item to recently viewed
recentlyViewed.addItem(exampleItem);

// Render the recently viewed items in a container with ID 'recently-viewed-container'
recentlyViewed.render('recently-viewed-container');

// Example of adding another item on user activity
// This can be triggered on viewing a product
function onViewProduct(product) {
    recentlyViewed.addItem(product);
    recentlyViewed.render('recently-viewed-container');
}

// Example product view
const anotherProduct = {
    id: '456',
    name: 'Another Product',
    description: 'This is another product description.',
    url: '/product/456'
};

// Simulate viewing another product
onViewProduct(anotherProduct);
```
