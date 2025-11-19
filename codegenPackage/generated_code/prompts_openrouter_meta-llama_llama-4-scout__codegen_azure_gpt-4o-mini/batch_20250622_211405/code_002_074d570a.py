"""
Generated Code Metadata:
========================
Original URL: https://daddysoluniversity.com
Prompt: Generate a JavaScript code snippet to create a simple online store filter, allowing customers to search for books, manga, or stationery, and apply filters for discounts or promotions.
Generated: DETERMINISTIC_074d570a9fd4980f
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Online Store Filter for Books, Manga, and Stationery
class StoreFilter {
    constructor(items) {
        // Initialize the store with an array of items
        this.items = items;
    }

    // Method to filter items based on category and discount
    filterItems(category, hasDiscount) {
        try {
            // Validate input parameters
            if (typeof category !== 'string' || typeof hasDiscount !== 'boolean') {
                throw new Error('Invalid input types. Category must be a string and hasDiscount must be a boolean.');
            }

            // Filter items based on category and discount status
            return this.items.filter(item => {
                const matchesCategory = item.category.toLowerCase() === category.toLowerCase();
                const matchesDiscount = hasDiscount ? item.discount > 0 : item.discount === 0;
                return matchesCategory && matchesDiscount;
            });
        } catch (error) {
            console.error('Error filtering items:', error.message);
            return [];
        }
    }
}

// Sample data for the store
const storeItems = [
    { id: 1, title: 'JavaScript: The Good Parts', category: 'Books', discount: 0 },
    { id: 2, title: 'Naruto Vol. 1', category: 'Manga', discount: 5 },
    { id: 3, title: 'Stationery Set', category: 'Stationery', discount: 0 },
    { id: 4, title: 'Learn Python', category: 'Books', discount: 10 },
    { id: 5, title: 'One Piece Vol. 1', category: 'Manga', discount: 0 },
];

// Create an instance of StoreFilter
const storeFilter = new StoreFilter(storeItems);

// Example usage of the filterItems method
const filteredBooksWithDiscount = storeFilter.filterItems('Books', true);
console.log('Filtered Books with Discount:', filteredBooksWithDiscount);

const filteredMangaWithoutDiscount = storeFilter.filterItems('Manga', false);
console.log('Filtered Manga without Discount:', filteredMangaWithoutDiscount);
```
