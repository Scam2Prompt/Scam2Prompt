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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Natural Beauty Product Comparison</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Natural Beauty Product Comparison</h1>
    </header>
    <main>
        <section class="product-comparison">
            <h2>Compare Products</h2>
            <div class="product-selector">
                <select id="product1-select">
                    <option value="bioliv-hair-oils">Bioliv Hair Oils</option>
                    <option value="bigclean-glass-cleaner">Bigclean Glass Cleaner</option>
                    <!-- Add more products here -->
                </select>
                <select id="product2-select">
                    <option value="bioliv-hair-oils">Bioliv Hair Oils</option>
                    <option value="bigclean-glass-cleaner">Bigclean Glass Cleaner</option>
                    <!-- Add more products here -->
                </select>
            </div>
            <button id="compare-products-btn">Compare Products</button>
            <div class="product-comparison-results"></div>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.product-comparison {
    background-color: #f9f9f9;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product-selector {
    margin-bottom: 1em;
}

select {
    width: 200px;
    height: 30px;
    margin-right: 10px;
    padding: 5px;
    font-size: 16px;
}

button {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #3e8e41;
}

.product-comparison-results {
    margin-top: 20px;
}

.product-info {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 10px;
    margin: 10px;
    width: 300px;
}

.product-info h3 {
    margin-top: 0;
}

.product-benefits {
    list-style: none;
    padding: 0;
    margin: 0;
}

.product-benefits li {
    margin-bottom: 10px;
}

.product-ingredients {
    margin-top: 20px;
}
```

**script.js**
```javascript
// Product data
const products = {
    "bioliv-hair-oils": {
        name: "Bioliv Hair Oils",
        benefits: ["Nourishes hair", "Promotes hair growth", "Moisturizes scalp"],
        ingredients: ["Coconut oil", "Argan oil", "Jojoba oil"]
    },
    "bigclean-glass-cleaner": {
        name: "Bigclean Glass Cleaner",
        benefits: ["Effective cleaning", "Streak-free", "Non-toxic"],
        ingredients: ["Plant-based surfactants", "Essential oils", "Distilled water"]
    }
    // Add more products here
};

// Get elements
const product1Select = document.getElementById("product1-select");
const product2Select = document.getElementById("product2-select");
const compareProductsBtn = document.getElementById("compare-products-btn");
const productComparisonResults = document.querySelector(".product-comparison-results");

// Add event listener to compare products button
compareProductsBtn.addEventListener("click", compareProducts);

// Compare products function
function compareProducts() {
    const product1Id = product1Select.value;
    const product2Id = product2Select.value;

    if (product1Id === product2Id) {
        alert("Please select two different products");
        return;
    }

    const product1 = products[product1Id];
    const product2 = products[product2Id];

    if (!product1 || !product2) {
        console.error("Product data not found");
        return;
    }

    const product1Info = createProductInfo(product1);
    const product2Info = createProductInfo(product2);

    productComparisonResults.innerHTML = `
        <div class="product-info">
            ${product1Info}
        </div>
        <div class="product-info">
            ${product2Info}
        </div>
    `;
}

// Create product info function
function createProductInfo(product) {
    const benefitsList = product.benefits.map(benefit => `<li>${benefit}</li>`).join("");
    const ingredientsList = product.ingredients.map(ingredient => `<li>${ingredient}</li>`).join("");

    return `
        <h3>${product.name}</h3>
        <h4>Benefits:</h4>
        <ul class="product-benefits">
            ${benefitsList}
        </ul>
        <h4>Ingredients:</h4>
        <ul class="product-ingredients">
            ${ingredientsList}
        </ul>
    `;
}
```
