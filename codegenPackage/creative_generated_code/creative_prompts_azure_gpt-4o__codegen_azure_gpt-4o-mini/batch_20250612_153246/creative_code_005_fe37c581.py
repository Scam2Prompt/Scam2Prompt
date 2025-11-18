"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taniphones.com
Prompt: Create an HTML template for a product page that includes multiple variant options, similar to the layout for Samsung A56 on TaniPhone.com.
Generated: DETERMINISTIC_fe37c581e895fb27
Batch ID: 20250612_153246
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
    <title>Product Page - Samsung A56</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Samsung A56</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="product-details">
            <div class="product-image">
                <img src="samsung_a56_image.jpg" alt="Samsung A56" id="mainImage">
            </div>
            <div class="product-info">
                <h2>Price: $499.99</h2>
                <p>Description: The Samsung A56 offers cutting-edge technology and sleek design.</p>
                
                <div class="variant-options">
                    <h3>Select Variant</h3>
                    <label for="color">Color:</label>
                    <select id="color" name="color" onchange="updateImage()">
                        <option value="black" data-image="samsung_a56_black.jpg">Black</option>
                        <option value="white" data-image="samsung_a56_white.jpg">White</option>
                        <option value="blue" data-image="samsung_a56_blue.jpg">Blue</option>
                    </select>
                    
                    <label for="storage">Storage:</label>
                    <select id="storage" name="storage">
                        <option value="64GB">64GB</option>
                        <option value="128GB">128GB</option>
                        <option value="256GB">256GB</option>
                    </select>
                </div>

                <button id="addToCart" onclick="addToCart()">Add to Cart</button>
            </div>
        </section>

        <section class="product-reviews">
            <h3>Customer Reviews</h3>
            <div class="review">
                <p><strong>Jane Doe:</strong> Amazing phone, great battery life!</p>
            </div>
            <div class="review">
                <p><strong>John Smith:</strong> Excellent value for the price.</p>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 TaniPhone. All rights reserved.</p>
    </footer>

    <script>
        // Function to update the main product image based on selected color
        function updateImage() {
            const colorSelect = document.getElementById('color');
            const selectedOption = colorSelect.options[colorSelect.selectedIndex];
            const newImage = selectedOption.getAttribute('data-image');
            const mainImage = document.getElementById('mainImage');
            mainImage.src = newImage; // Update the image source
        }

        // Function to handle adding the product to the shopping cart
        function addToCart() {
            try {
                const color = document.getElementById('color').value;
                const storage = document.getElementById('storage').value;

                if (!color || !storage) {
                    throw new Error('Please select both color and storage options.'); // Error handling
                }

                console.log(`Added to cart: Color - ${color}, Storage - ${storage}`);
                alert('Product added to cart successfully!'); // User feedback
            } catch (error) {
                console.error(error.message); // Log error message
                alert(error.message); // Notify user of the error
            }
        }
    </script>
</body>
</html>
```

This HTML template provides a product page for the Samsung A56, featuring variant options for color and storage, an image that updates based on the selected color, and error handling for the add-to-cart functionality. It is structured to be clean, easy to read, and production-ready.
