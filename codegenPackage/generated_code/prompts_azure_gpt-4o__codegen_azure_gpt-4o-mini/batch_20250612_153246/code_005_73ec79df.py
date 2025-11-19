"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: Generate HTML and CSS code for a pricing table that includes packages like "Minim," "Mediu," and "Maxim," with features such as SEO, maintenance, and visual identity elements, as detailed on Henfruit's website.
Generated: DETERMINISTIC_73ec79df5eb334bf
Batch ID: 20250612_153246
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
    <title>Pricing Table</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="pricing-table">
        <div class="pricing-package">
            <h2>Minim</h2>
            <p class="price">$99/month</p>
            <ul class="features">
                <li>SEO Optimization</li>
                <li>Basic Maintenance</li>
                <li>Visual Identity Elements</li>
            </ul>
            <button class="btn">Choose Minim</button>
        </div>
        <div class="pricing-package">
            <h2>Mediu</h2>
            <p class="price">$199/month</p>
            <ul class="features">
                <li>SEO Optimization</li>
                <li>Standard Maintenance</li>
                <li>Visual Identity Elements</li>
                <li>Social Media Integration</li>
            </ul>
            <button class="btn">Choose Mediu</button>
        </div>
        <div class="pricing-package">
            <h2>Maxim</h2>
            <p class="price">$299/month</p>
            <ul class="features">
                <li>SEO Optimization</li>
                <li>Premium Maintenance</li>
                <li>Visual Identity Elements</li>
                <li>Social Media Integration</li>
                <li>Analytics & Reporting</li>
            </ul>
            <button class="btn">Choose Maxim</button>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Pricing table container */
.pricing-table {
    display: flex;
    justify-content: space-around;
    width: 80%;
}

/* Individual pricing package styling */
.pricing-package {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    width: 30%;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s;
}

/* Hover effect for pricing packages */
.pricing-package:hover {
    transform: scale(1.05);
}

/* Price styling */
.price {
    font-size: 24px;
    font-weight: bold;
    margin: 15px 0;
}

/* Features list styling */
.features {
    list-style-type: none;
    margin: 20px 0;
}

/* Button styling */
.btn {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
    transition: background-color 0.3s;
}

/* Button hover effect */
.btn:hover {
    background-color: #0056b3;
}
```
