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
 * @param {Array} products - An array of product objects to be compared.
 * @param {Object} criteria - An object representing user-selected criteria for filtering.
 * @returns {void}
 */
function updateProductComparisonTable(products, criteria) {
    // Validate inputs
    if (!Array.isArray(products) || typeof criteria !== 'object') {
        console.error('Invalid input: products must be an array and criteria must be an object.');
        return;
    }

    // Get the comparison table element
    const comparisonTable = document.getElementById('comparisonTable');
    if (!comparisonTable) {
        console.error('Comparison table element not found.');
        return;
    }

    // Clear the existing table rows
    comparisonTable.innerHTML = '';

    // Add table headers
    const headers = ['Product Name', 'Category', 'Price', 'Rating'];
    const headerRow = document.createElement('tr');
    headers.forEach(headerText => {
        const header = document.createElement('th');
        header.textContent = headerText;
        headerRow.appendChild(header);
    });
    comparisonTable.appendChild(headerRow);

    // Filter products based on criteria
    const filteredProducts = products.filter(product => {
        return Object.keys(criteria).every(key => {
            return product[key] === criteria[key];
        });
    });

    // Check if any products match the criteria
    if (filteredProducts.length === 0) {
        const noResultsRow = document.createElement('tr');
        const noResultsCell = document.createElement('td');
        noResultsCell.colSpan = headers.length;
        noResultsCell.textContent = 'No products match the selected criteria.';
        noResultsRow.appendChild(noResultsCell);
        comparisonTable.appendChild(noResultsRow);
        return;
    }

    // Populate the table with filtered products
    filteredProducts.forEach(product => {
        const row = document.createElement('tr');

        const nameCell = document.createElement('td');
        nameCell.textContent = product.name;
        row.appendChild(nameCell);

        const categoryCell = document.createElement('td');
        categoryCell.textContent = product.category;
        row.appendChild(categoryCell);

        const priceCell = document.createElement('td');
        priceCell.textContent = product.price.toFixed(2) + ' $';
        row.appendChild(priceCell);

        const ratingCell = document.createElement('td');
        ratingCell.textContent = product.rating.toFixed(1);
        row.appendChild(ratingCell);

        comparisonTable.appendChild(row);
    });
}

// Example usage
const products = [
    { name: 'صندلی انتظار کلاسیک', category: 'صندلی انتظار آرایشگاه', price: 150.00, rating: 4.5 },
    { name: 'میز ناخن مدرن', category: 'میز ناخن', price: 200.00, rating: 4.8 },
    { name: 'صندلی انتظار لوکس', category: 'صندلی انتظار آرایشگاه', price: 250.00, rating: 4.7 },
];

const userCriteria = { category: 'صندلی انتظار آرایشگاه' };
updateProductComparisonTable(products, userCriteria);
```
