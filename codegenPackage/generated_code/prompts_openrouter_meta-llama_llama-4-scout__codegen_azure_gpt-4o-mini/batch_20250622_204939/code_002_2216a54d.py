"""
Generated Code Metadata:
========================
Original URL: https://dhcpbrazz.blogspot.com
Prompt: Generate a JavaScript code to display the product information of HD 3.5'' 4TB Seagate IronWolf ST4000VN008, including its price and discount percentage, on a web page.
Generated: DETERMINISTIC_2216a54dee171ed6
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Information</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            max-width: 400px;
        }
        .product-title {
            font-size: 24px;
            font-weight: bold;
        }
        .product-price {
            font-size: 20px;
            color: green;
        }
        .product-discount {
            font-size: 16px;
            color: red;
        }
    </style>
</head>
<body>

    <div id="product-info">
        <!-- Product information will be displayed here -->
    </div>

    <script>
        // Product data
        const product = {
            name: "HD 3.5'' 4TB Seagate IronWolf ST4000VN008",
            price: 129.99, // Original price in USD
            discountPercentage: 15 // Discount percentage
        };

        /**
         * Function to calculate the discounted price
         * @param {number} price - The original price of the product
         * @param {number} discount - The discount percentage
         * @returns {number} - The discounted price
         */
        function calculateDiscountedPrice(price, discount) {
            if (typeof price !== 'number' || typeof discount !== 'number') {
                throw new Error("Price and discount must be numbers");
            }
            return price - (price * (discount / 100));
        }

        /**
         * Function to display product information on the web page
         * @param {Object} product - The product object containing name, price, and discount
         */
        function displayProductInfo(product) {
            try {
                const discountedPrice = calculateDiscountedPrice(product.price, product.discountPercentage);
                
                // Create HTML content
                const productHTML = `
                    <div class="product-title">${product.name}</div>
                    <div class="product-price">Price: $${product.price.toFixed(2)}</div>
                    <div class="product-discount">Discount: ${product.discountPercentage}%</div>
                    <div class="product-price">Discounted Price: $${discountedPrice.toFixed(2)}</div>
                `;

                // Insert HTML into the product-info div
                document.getElementById('product-info').innerHTML = productHTML;
            } catch (error) {
                console.error("Error displaying product information:", error);
                document.getElementById('product-info').innerHTML = "<p>Error displaying product information. Please try again later.</p>";
            }
        }

        // Call the function to display product information
        displayProductInfo(product);
    </script>

</body>
</html>
```
