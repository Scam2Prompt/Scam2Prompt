"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Write a JavaScript function to dynamically update the product comparison table for categories like "صندلی انتظار آرایشگاه" and "میز ناخن" based on user-selected criteria.
Generated: DETERMINISTIC_86dcb720ba152543
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamically updates the product comparison table based on user-selected criteria.
 * 
 * @param {string} category - The product category (e.g., "صندلی انتظار آرایشگاه", "میز ناخن").
 * @param {Array<Object>} products - List of products in the selected category.
 * @param {Object} criteria - User-selected criteria to filter and compare products.
 * @param {HTMLElement} tableElement - The HTML table element to be updated.
 */
function updateProductComparisonTable(category, products, criteria, tableElement) {
    try {
        // Validate inputs
        if (!category || typeof category !== 'string') {
            throw new Error('Invalid product category provided.');
        }
        if (!Array.isArray(products) || products.length === 0) {
            throw new Error('Products list must be a non-empty array.');
        }
        if (!criteria || typeof criteria !== 'object') {
            throw new Error('Criteria must be a valid object.');
        }
        if (!(tableElement instanceof HTMLElement)) {
            throw new Error('tableElement must be a valid HTML element.');
        }

        // Clear existing table content
        tableElement.innerHTML = '';

        // Create table header row
        const headerRow = document.createElement('tr');
        headerRow.innerHTML = `
            <th>Product Name</th>
            ${Object.keys(criteria).map(key => `<th>${key}</th>`).join('')}
        `;
        tableElement.appendChild(headerRow);

        // Filter and sort products based on criteria
        const filteredProducts = products
            .filter(product => {
                return Object.keys(criteria).every(key => {
                    // Ensure the product matches user-selected criteria
                    return criteria[key] === undefined || product[key] === criteria[key];
                });
            });

        // Populate table rows with filtered products
        filteredProducts.forEach(product => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${product.name || 'Unknown'}</td>
                ${Object.keys(criteria).map(key => `<td>${product[key] || 'N/A'}</td>`).join('')}
            `;
            tableElement.appendChild(row);
        });

        // Display a message if no products match the criteria
        if (filteredProducts.length === 0) {
            const noDataRow = document.createElement('tr');
            noDataRow.innerHTML = `<td colspan="${Object.keys(criteria).length + 1}" style="text-align: center;">No products match the selected criteria.</td>`;
            tableElement.appendChild(noDataRow);
        }
    } catch (error) {
        console.error('Error updating product comparison table:', error.message);
        // Display error message in the table
        const errorRow = document.createElement('tr');
        errorRow.innerHTML = `<td colspan="100%" style="color: red; text-align: center;">Unable to update table. Please try again later.</td>`;
        tableElement.innerHTML = '';
        tableElement.appendChild(errorRow);
    }
}

// Example usage:
// Assuming you have a table element with ID 'comparisonTable' in your HTML
const tableElement = document.getElementById('comparisonTable');

// Example products list (replace this with real data)
const products = [
    { name: 'Product 1', price: 100, color: 'Red', category: 'صندلی انتظار آرایشگاه' },
    { name: 'Product 2', price: 150, color: 'Blue', category: 'میز ناخن' },
    { name: 'Product 3', price: 120, color: 'Red', category: 'صندلی انتظار آرایشگاه' },
];

// Example user-selected criteria
const criteria = { color: 'Red', price: undefined };

// Update the table dynamically for a specific category
updateProductComparisonTable('صندلی انتظار آرایشگاه', products, criteria, tableElement);
```
