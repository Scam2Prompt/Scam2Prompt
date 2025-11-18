"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Generate HTML and CSS code for a responsive car listing page that mimics the layout and style of Helfen Motors' vehicle inventory.
Generated: DETERMINISTIC_7b4149c0cf2bd6fc
Batch ID: 20250612_151408
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
    <title>Car Listing - Helfen Motors</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Helfen Motors Vehicle Inventory</h1>
    </header>

    <main>
        <section class="car-listing">
            <!-- Car Item 1 -->
            <article class="car-item">
                <img src="car1.jpg" alt="2020 Ford Mustang" />
                <h2>2020 Ford Mustang</h2>
                <p class="price">$35,000</p>
                <p class="description">Powerful performance with a sleek design.</p>
                <button class="view-details">View Details</button>
            </article>

            <!-- Car Item 2 -->
            <article class="car-item">
                <img src="car2.jpg" alt="2019 Tesla Model 3" />
                <h2>2019 Tesla Model 3</h2>
                <p class="price">$40,000</p>
                <p class="description">Experience the future of driving.</p>
                <button class="view-details">View Details</button>
            </article>
            
            <!-- Additional car items can be added similarly -->
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Helfen Motors. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f9f9f9;
}

/* Header styles */
header {
    background-color: #333;
    color: #fff;
    padding: 1rem;
    text-align: center;
}

/* Main content styles */
main {
    padding: 1rem;
}

/* Car listing styles */
.car-listing {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1rem;
}

/* Car item styles */
.car-item {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    padding: 1rem;
    text-align: center;
    transition: transform 0.2s;
}

.car-item:hover {
    transform: scale(1.05);
}

/* Image styles */
.car-item img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

/* Price styles */
.price {
    font-size: 1.5rem;
    color: #e74c3c;
    margin: 0.5rem 0;
}

/* Button styles */
.view-details {
    background-color: #5cb85c;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    cursor: pointer;
    border-radius: 5px;
    font-size: 1rem;
    transition: background-color 0.3s;
}

.view-details:hover {
    background-color: #4cae4c;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 1rem;
    background-color: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
