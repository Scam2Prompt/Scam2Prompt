"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Develop a simple HTML page that showcases featured properties, including images and descriptions, inspired by the layout and content of Presval's property showcase.
Generated: DETERMINISTIC_50d60b781d043c50
Batch ID: 20250612_162325
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
    <title>Featured Properties</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Featured Properties</h1>
        <p>Explore our exclusive listings of stunning properties.</p>
    </header>

    <main>
        <section class="property-list">
            <!-- Property Item 1 -->
            <article class="property-item">
                <img src="property1.jpg" alt="Beautiful Family Home" class="property-image">
                <h2 class="property-title">Beautiful Family Home</h2>
                <p class="property-description">A spacious 4-bedroom home located in a quiet neighborhood, perfect for families.</p>
                <p class="property-price">$500,000</p>
                <a href="property1-details.html" class="property-link">View Details</a>
            </article>

            <!-- Property Item 2 -->
            <article class="property-item">
                <img src="property2.jpg" alt="Modern Apartment" class="property-image">
                <h2 class="property-title">Modern Apartment</h2>
                <p class="property-description">A stylish 2-bedroom apartment in the heart of the city, close to all amenities.</p>
                <p class="property-price">$350,000</p>
                <a href="property2-details.html" class="property-link">View Details</a>
            </article>

            <!-- Property Item 3 -->
            <article class="property-item">
                <img src="property3.jpg" alt="Luxury Villa" class="property-image">
                <h2 class="property-title">Luxury Villa</h2>
                <p class="property-description">An exquisite 5-bedroom villa with a private pool and stunning ocean views.</p>
                <p class="property-price">$1,200,000</p>
                <a href="property3-details.html" class="property-link">View Details</a>
            </article>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Real Estate Company. All rights reserved.</p>
    </footer>
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
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

/* Main section styling */
main {
    padding: 20px;
}

/* Property list styling */
.property-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

/* Individual property item styling */
.property-item {
    background: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    width: 300px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Property image styling */
.property-image {
    width: 100%;
    height: auto;
    border-radius: 5px;
}

/* Property title styling */
.property-title {
    font-size: 1.5em;
    margin: 10px 0;
}

/* Property description styling */
.property-description {
    color: #555555;
}

/* Property price styling */
.property-price {
    font-weight: bold;
    color: #e67e22;
}

/* Link styling */
.property-link {
    display: inline-block;
    margin-top: 10px;
    padding: 10px 15px;
    background: #35424a;
    color: #ffffff;
    text-decoration: none;
    border-radius: 5px;
}

.property-link:hover {
    background: #e67e22;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 20px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
