"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Create HTML and CSS code for a webpage that displays SmartPrice KE's "Top Deals" section, including products like the Google Pixel 9 Pro Fold and iPhone 16 Pro Max.
Generated: DETERMINISTIC_bfedd2e6fad0fd14
Batch ID: 20250612_154021
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
    <title>SmartPrice KE - Top Deals</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>SmartPrice KE</h1>
        <h2>Top Deals</h2>
    </header>

    <main>
        <section class="top-deals">
            <div class="product">
                <img src="images/google-pixel-9-pro-fold.jpg" alt="Google Pixel 9 Pro Fold" />
                <h3>Google Pixel 9 Pro Fold</h3>
                <p class="price">KSh 120,000</p>
                <button class="buy-button">Buy Now</button>
            </div>

            <div class="product">
                <img src="images/iphone-16-pro-max.jpg" alt="iPhone 16 Pro Max" />
                <h3>iPhone 16 Pro Max</h3>
                <p class="price">KSh 150,000</p>
                <button class="buy-button">Buy Now</button>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 SmartPrice KE. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles for a better cross-browser experience */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    line-height: 1.6;
}

header {
    background: #007BFF;
    color: #ffffff;
    padding: 10px 20px;
    text-align: center;
}

h1 {
    font-size: 2.5em;
}

h2 {
    font-size: 1.8em;
    margin-top: 10px;
}

main {
    padding: 20px;
}

.top-deals {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
}

.product {
    background: #ffffff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    text-align: center;
    transition: box-shadow 0.3s;
}

.product:hover {
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.product img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

.price {
    font-size: 1.5em;
    color: #d9534f;
    margin: 10px 0;
}

.buy-button {
    background: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 15px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.buy-button:hover {
    background-color: #218838;
}

footer {
    text-align: center;
    padding: 15px;
    background: #007BFF;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
