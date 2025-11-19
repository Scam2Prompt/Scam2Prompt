"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Create a product comparison feature using HTML, CSS, and JavaScript to compare the benefits and ingredients of different natural beauty products, such as "Bioliv Hair Oils" and "Bigclean Glass Cleaner".
Generated: DETERMINISTIC_5af23235953b9679
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's the complete code for the product comparison feature:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Natural Beauty Product Comparison</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f9f9f9;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
            color: #2c3e50;
        }

        /* Comparison table styles */
        .comparison-container {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }

        .comparison-header {
            display: flex;
            background: #3498db;
            color: white;
        }

        .comparison-header-item {
            flex: 1;
            padding: 15px;
            text-align: center;
            font-weight: bold;
            border-right: 1px solid rgba(255, 255, 255, 0.2);
        }

        .comparison-header-item:last-child {
            border-right: none;
        }

        .comparison-row {
            display: flex;
            border-bottom: 1px solid #eee;
        }

        .comparison-row:last-child {
            border-bottom: none;
        }

        .comparison-row-title {
            flex: 1;
            padding: 15px;
            font-weight: bold;
            background: #f5f5f5;
        }

        .comparison-row-item {
            flex: 1;
            padding: 15px;
            text-align: center;
        }

        .highlight {
            background-color: #e8f4fc;
            font-weight: bold;
        }

        /* Product selection */
        .product-selection {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
            gap: 20px;
            flex-wrap: wrap;
        }

        .product-select {
            padding: 10px 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background: white;
            cursor: pointer;
            min-width: 200px;
        }

        .compare-btn {
            padding: 10px 20px;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.3s;
        }

        .compare-btn:hover {
            background: #2980b9;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .comparison-header, .comparison-row {
                flex-direction: column;
            }

            .comparison-header-item, .comparison-row-title, .comparison-row-item {
                text-align: left;
                border-right: none;
                border-bottom: 1px solid #eee;
            }

            .product-selection {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Natural Beauty Product Comparison</h1>
        
        <div class="product-selection">
            <select id="product1" class="product-select">
                <option value="">Select Product 1</option>
            </select>
            <select id="product2" class="product-select">
                <option value="">Select Product 2</option>
            </select>
            <button id="compareButton" class="compare-btn">Compare Products</button>
        </div>

        <div id="comparisonResults" class="comparison-container" style="display: none;">
            <!-- Comparison table will be generated here -->
        </div>
    </div>

    <script>
        // Product data
        const products = {
            "bioliv": {
                name: "Bioliv Hair Oils",
                category: "Hair Care",
                benefits: [
                    "Promotes hair growth",
                    "Reduces hair fall",
                    "Nourishes scalp",
                    "Adds shine to hair"
                ],
                ingredients: [
                    "Olive oil",
                    "Almond oil",
                    "Coconut oil",
                    "Rosemary extract"
                ],
                price: "$19.99",
                rating: "4.5/5"
            },
            "bigclean": {
                name: "Bigclean Glass Cleaner",
                category: "Home Care",
                benefits: [
                    "Streak-free cleaning",
                    "Eco-friendly formula",
                    "Removes tough stains",
                    "Safe for all glass surfaces"
                ],
                ingredients: [
                    "Distilled water",
                    "White vinegar",
                    "Citrus extract",
                    "Plant-based surfactants"
                ],
                price: "$12.99",
                rating: "4.2/5"
            },
            "herbaskin": {
                name: "Herbaskin Face Cream",
                category: "Skin Care",
                benefits: [
                    "Hydrates skin",
                    "Reduces wrinkles",
                    "Natural SPF protection",
                    "Suitable for all skin types"
                ],
                ingredients: [
                    "Aloe vera",
                    "Shea butter",
                    "Jojoba oil",
                    "Green tea extract"
                ],
                price: "$24.99",
                rating: "4.7/5"
            }
        };

        // DOM elements
        const product1Select = document.getElementById('product1');
        const product2Select = document.getElementById('product2');
        const compareButton = document.getElementById('compareButton');
        const comparisonResults = document.getElementById('comparisonResults');

        /**
         * Initialize the product dropdowns
         */
        function initializeDropdowns() {
            // Add products to dropdowns
            for (const [id, product] of Object.entries(products)) {
                const option1 = document.createElement('option');
                option1.value = id;
                option1.textContent = product.name;
                product1Select.appendChild(option1);

                const option2 = document.createElement('option');
                option2.value = id;
                option2.textContent = product.name;
                product2Select.appendChild(option2);
            }
        }

        /**
         * Compare two products and display results
         * @param {string} product1Id - ID of first product
         * @param {string} product2Id - ID of second product
         */
        function compareProducts(product1Id, product2Id) {
            if (!product1Id || !product2Id) {
                alert('Please select two products to compare');
                return;
            }

            if (product1Id === product2Id) {
                alert('Please select two different products to compare');
                return;
            }

            const product1 = products[product1Id];
            const product2 = products[product2Id];

            // Clear previous results
            comparisonResults.innerHTML = '';
            comparisonResults.style.display = 'block';

            // Create comparison table
            const table = document.createElement('div');

            // Header row
            const headerRow = document.createElement('div');
            headerRow.className = 'comparison-header';

            const emptyHeader = document.createElement('div');
            emptyHeader.className = 'comparison-header-item';
            emptyHeader.textContent = 'Features';
            headerRow.appendChild(emptyHeader);

            const header1 = document.createElement('div');
            header1.className = 'comparison-header-item';
            header1.textContent = product1.name;
            headerRow.appendChild(header1);

            const header2 = document.createElement('div');
            header2.className = 'comparison-header-item';
            header2.textContent = product2.name;
            headerRow.appendChild(header2);

            table.appendChild(headerRow);

            // Add comparison rows
            addComparisonRow(table, 'Category', product1.category, product2.category);
            addComparisonRow(table, 'Price', product1.price, product2.price);
            addComparisonRow(table, 'Rating', product1.rating, product2.rating);
            
            // Benefits comparison
            addListComparisonRow(table, 'Benefits', product1.benefits, product2.benefits);
            
            // Ingredients comparison
            addListComparisonRow(table, 'Ingredients', product1.ingredients, product2.ingredients);

            comparisonResults.appendChild(table);
        }

        /**
         * Add a simple comparison row to the table
         * @param {HTMLElement} table - Table element
         * @param {string} title - Row title
         * @param {string} value1 - First product value
         * @param {string} value2 - Second product value
         */
        function addComparisonRow(table, title, value
