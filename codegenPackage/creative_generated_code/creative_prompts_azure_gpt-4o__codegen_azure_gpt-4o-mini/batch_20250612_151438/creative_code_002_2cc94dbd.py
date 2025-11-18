"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Generate code to create an e-commerce product listing page for lighting products, including fields for product name, price, discount percentage, installment options, and free shipping eligibility, as seen in the "Plafon Chess 4xe27 Biv Newline 171bt" example.
Generated: DETERMINISTIC_2cc94dbd9f5d8760
Batch ID: 20250612_151438
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
    <title>Lighting Products - E-commerce Listing</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Lighting Products</h1>
    </header>
    <main>
        <section id="product-list">
            <!-- Product Item -->
            <article class="product-item">
                <h2 class="product-name">Plafon Chess 4xe27 Biv Newline 171bt</h2>
                <p class="product-price">Price: <span class="price">€120.00</span></p>
                <p class="product-discount">Discount: <span class="discount">15%</span></p>
                <p class="product-installment">Installments: <span class="installment-options">€10.00/month for 12 months</span></p>
                <p class="product-free-shipping">Free Shipping: <span class="free-shipping">Yes</span></p>
                <button class="add-to-cart">Add to Cart</button>
            </article>
            <!-- Additional product items can be added here -->
        </section>
    </main>
    <footer>
        <p>&copy; 2023 E-commerce Lighting Store</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for body margins and padding */
body {
    margin: 0;
    font-family: Arial, sans-serif;
}

/* Header styles */
header {
    background-color: #f8f8f8;
    padding: 20px;
    text-align: center;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Product item styles */
.product-item {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 15px;
}

.product-name {
    font-size: 1.5em;
    margin: 0;
}

.product-price,
.product-discount,
.product-installment,
.product-free-shipping {
    margin: 5px 0;
}

/* Button styles */
.add-to-cart {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
}

.add-to-cart:hover {
    background-color: #218838; /* Darker green on hover */
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px;
    background-color: #f1f1f1;
}
```

```javascript
// script.js

// Function to handle the add to cart action
function addToCart(product) {
    try {
        // Example of product object structure
        const cartItem = {
            name: product.name,
            price: product.price,
            discount: product.discount,
            installment: product.installment,
            freeShipping: product.freeShipping,
        };

        // Here we would normally add the item to a shopping cart
        console.log("Product added to cart:", cartItem);
        alert(`${product.name} has been added to your cart.`);
    } catch (error) {
        console.error("Error adding product to cart:", error);
        alert("Failed to add product to cart. Please try again.");
    }
}

// Attach event listeners to add to cart buttons after DOM content is loaded
document.addEventListener('DOMContentLoaded', () => {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', () => {
            const productItem = button.closest('.product-item');
            const productName = productItem.querySelector('.product-name').innerText;
            const productPrice = productItem.querySelector('.price').innerText;
            const productDiscount = productItem.querySelector('.discount').innerText;
            const productInstallment = productItem.querySelector('.installment-options').innerText;
            const productFreeShipping = productItem.querySelector('.free-shipping').innerText === 'Yes';

            addToCart({
                name: productName,
                price: productPrice,
                discount: productDiscount,
                installment: productInstallment,
                freeShipping: productFreeShipping
            });
        });
    });
});
```
