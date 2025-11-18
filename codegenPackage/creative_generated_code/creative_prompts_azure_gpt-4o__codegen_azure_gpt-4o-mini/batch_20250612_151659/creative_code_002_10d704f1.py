"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Generate a script in JavaScript to create a dynamic product catalog webpage for Meta+, displaying categories like stainless steel, aluminum, copper, and engineering plastics, with filtering options for material type and availability.
Generated: DETERMINISTIC_10d704f10275d692
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meta+ Product Catalog</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Meta+ Product Catalog</h1>
        <div>
            <label for="material-filter">Filter by Material:</label>
            <select id="material-filter">
                <option value="all">All</option>
                <option value="stainless-steel">Stainless Steel</option>
                <option value="aluminum">Aluminum</option>
                <option value="copper">Copper</option>
                <option value="engineering-plastics">Engineering Plastics</option>
            </select>
            <label for="availability-filter">Availability:</label>
            <select id="availability-filter">
                <option value="all">All</option>
                <option value="available">Available</option>
                <option value="unavailable">Unavailable</option>
            </select>
        </div>
    </header>

    <main id="product-catalog"></main>

    <script>
        // Sample product data
        const products = [
            { id: 1, name: "Stainless Steel Bolt", material: "stainless-steel", available: true },
            { id: 2, name: "Aluminum Sheet", material: "aluminum", available: true },
            { id: 3, name: "Copper Wire", material: "copper", available: false },
            { id: 4, name: "Engineering Plastic Hinge", material: "engineering-plastics", available: true },
            { id: 5, name: "Stainless Steel Nut", material: "stainless-steel", available: true },
            { id: 6, name: "Aluminum Pipe", material: "aluminum", available: false }
        ];

        // Function to render products based on filters
        function renderProducts(materialFilter, availabilityFilter) {
            const catalog = document.getElementById('product-catalog');
            catalog.innerHTML = ''; // Clear previous results

            // Filter products based on selected criteria
            const filteredProducts = products.filter(product => {
                const materialMatch = materialFilter === 'all' || product.material === materialFilter;
                const availabilityMatch = availabilityFilter === 'all' || (availabilityFilter === 'available' ? product.available : !product.available);
                return materialMatch && availabilityMatch;
            });

            // Check if any products match the filter
            if (filteredProducts.length === 0) {
                catalog.innerHTML = '<p>No products found.</p>';
                return;
            }

            // Render filtered products
            filteredProducts.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.classList.add('product');
                productDiv.innerHTML = `<h2>${product.name}</h2>
                                        <p>Material: ${product.material.replace(/-/g, ' ')}</p>
                                        <p>Availability: ${product.available ? 'In Stock' : 'Out of Stock'}</p>`;
                catalog.appendChild(productDiv);
            });
        }

        // Event listeners for filter changes
        document.getElementById('material-filter').addEventListener('change', function() {
            const material = this.value;
            const availability = document.getElementById('availability-filter').value;
            renderProducts(material, availability);
        });

        document.getElementById('availability-filter').addEventListener('change', function() {
            const availability = this.value;
            const material = document.getElementById('material-filter').value;
            renderProducts(material, availability);
        });

        // Initial render of products
        renderProducts('all', 'all');
    </script>
</body>
</html>
```

This code provides a basic structure for a dynamic product catalog web page. It includes filtering options for material type and availability, and it handles the filtering logic with appropriate error handling and user feedback.
