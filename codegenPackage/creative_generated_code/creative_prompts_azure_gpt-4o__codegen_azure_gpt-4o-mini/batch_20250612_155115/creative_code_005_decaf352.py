"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ocuvana.com
Prompt: Generate HTML and CSS code for a product page showcasing magnetic eyelashes with features like "patented polymer composite" and "multi-pole magnetization," as described on Ocuvana's website.
Generated: DETERMINISTIC_decaf3525d4dd400
Batch ID: 20250612_155115
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
    <title>Magnetic Eyelashes - Ocuvana</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Ocuvana Magnetic Eyelashes</h1>
    </header>
    
    <main>
        <section class="product-overview">
            <img src="magnetic-eyelashes.jpg" alt="Magnetic Eyelashes" class="product-image">
            <h2>Experience the Future of Eyelash Technology</h2>
            <p>Our magnetic eyelashes are designed with cutting-edge features to give you the best look with ease.</p>
        </section>

        <section class="features">
            <h3>Features</h3>
            <ul>
                <li><strong>Patented Polymer Composite:</strong> Lightweight and durable material for a natural look.</li>
                <li><strong>Multi-Pole Magnetization:</strong> Ensures a secure and comfortable fit for all-day wear.</li>
                <li><strong>Easy Application:</strong> Quick to apply and remove without the need for glue.</li>
            </ul>
        </section>

        <section class="purchase">
            <h3>Order Now</h3>
            <p>Price: <strong>$29.99</strong></p>
            <button id="buy-now">Buy Now</button>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Ocuvana. All rights reserved.</p>
    </footer>

    <script>
        document.getElementById('buy-now').addEventListener('click', function() {
            try {
                // Simulating a purchase request
                alert("Thank you for your purchase!");
            } catch (error) {
                console.error("Purchase failed:", error);
                alert("There was an error processing your purchase. Please try again.");
            }
        });
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

header {
    background: #35424a;
    color: #ffffff;
    padding: 10px 0;
    text-align: center;
}

.product-overview {
    padding: 20px;
    text-align: center;
}

.product-image {
    max-width: 100%;
    height: auto;
}

.features {
    background: #ffffff;
    padding: 20px;
    margin: 20px 0;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.features h3 {
    margin-bottom: 15px;
}

.purchase {
    text-align: center;
    margin: 20px 0;
}

.purchase button {
    background: #35424a;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 5px;
}

.purchase button:hover {
    background: #2c3e50;
}

footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
