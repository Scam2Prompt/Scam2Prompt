"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgnexts.top
Prompt: Generate a script in JavaScript to filter and display UCI-approved track cycling products, such as helmets and wheels, based on user selection.
Generated: DETERMINISTIC_fa5b91adc7bd02dc
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Product filtering script for UCI-approved track cycling products

// Sample data representing UCI-approved cycling products
const products = [
    { id: 1, name: 'Aero Helmet', type: 'helmet', approved: true },
    { id: 2, name: 'Lightweight Wheels', type: 'wheels', approved: true },
    { id: 3, name: 'Mountain Bike Helmet', type: 'helmet', approved: false },
    { id: 4, name: 'Track Racing Wheels', type: 'wheels', approved: true },
    { id: 5, name: 'Casual Helmet', type: 'helmet', approved: false },
];

// Function to filter products based on user-selected type
function filterProducts(selectedType) {
    // Validate user input
    if (typeof selectedType !== 'string' || !selectedType) {
        console.error('Invalid product type selected. Please select "helmet" or "wheels".');
        return [];
    }

    // Filter products for the selected type and UCI approval
    const filteredProducts = products.filter(product => 
        product.type === selectedType && product.approved
    );

    return filteredProducts;
}

// Function to display filtered products
function displayProducts(filteredProducts) {
    // Check if there are products to display
    if (filteredProducts.length === 0) {
        console.log('No UCI-approved products found for the selected type.');
        return;
    }

    // Display the filtered products
    console.log('UCI-approved Products:');
    filteredProducts.forEach(product => {
        console.log(`- ${product.name} (${product.type})`);
    });
}

// Example usage: Filtering and displaying UCI-approved helmets
const selectedType = 'helmet'; // User selected type can be 'helmet' or 'wheels'
const filteredProducts = filterProducts(selectedType);
displayProducts(filteredProducts);

// Note: The user can change the value of `selectedType` to filter for different product types.
```
