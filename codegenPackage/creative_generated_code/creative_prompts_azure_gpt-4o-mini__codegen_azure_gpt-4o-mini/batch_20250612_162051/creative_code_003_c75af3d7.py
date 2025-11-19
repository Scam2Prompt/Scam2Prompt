"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birafurniture.com
Prompt: Develop a simple HTML/CSS template for a furniture shop homepage that includes sections for exploring different furniture categories, similar to Bira Furniture's design.
Generated: DETERMINISTIC_c75af3d7fd0d9c54
Batch ID: 20250612_162051
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
    <title>Furniture Shop</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Our Furniture Shop</h1>
        <nav>
            <ul>
                <li><a href="#living-room">Living Room</a></li>
                <li><a href="#bedroom">Bedroom</a></li>
                <li><a href="#office">Office</a></li>
                <li><a href="#outdoor">Outdoor</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="living-room" class="category">
            <h2>Living Room Furniture</h2>
            <p>Explore our collection of sofas, coffee tables, and more.</p>
            <div class="item-grid">
                <div class="item">
                    <img src="sofa.jpg" alt="Comfortable Sofa">
                    <h3>Comfortable Sofa</h3>
                    <p>$499</p>
                </div>
                <div class="item">
                    <img src="coffee-table.jpg" alt="Stylish Coffee Table">
                    <h3>Stylish Coffee Table</h3>
                    <p>$199</p>
                </div>
                <!-- Add more living room items here -->
            </div>
        </section>

        <section id="bedroom" class="category">
            <h2>Bedroom Furniture</h2>
            <p>Find the perfect bed, dresser, and nightstand.</p>
            <div class="item-grid">
                <div class="item">
                    <img src="bed.jpg" alt="Cozy Bed">
                    <h3>Cozy Bed</h3>
                    <p>$699</p>
                </div>
                <div class="item">
                    <img src="dresser.jpg" alt="Elegant Dresser">
                    <h3>Elegant Dresser</h3>
                    <p>$299</p>
                </div>
                <!-- Add more bedroom items here -->
            </div>
        </section>

        <section id="office" class="category">
            <h2>Office Furniture</h2>
            <p>Upgrade your workspace with our desks and chairs.</p>
            <div class="item-grid">
                <div class="item">
                    <img src="desk.jpg" alt="Ergonomic Desk">
                    <h3>Ergonomic Desk</h3>
                    <p>$399</p>
                </div>
                <div class="item">
                    <img src="office-chair.jpg" alt="Comfortable Office Chair">
                    <h3>Comfortable Office Chair</h3>
                    <p>$149</p>
                </div>
                <!-- Add more office items here -->
            </div>
        </section>

        <section id="outdoor" class="category">
            <h2>Outdoor Furniture</h2>
            <p>Enjoy your garden with our outdoor sofas and chairs.</p>
            <div class="item-grid">
                <div class="item">
                    <img src="outdoor-sofa.jpg" alt="Outdoor Sofa">
                    <h3>Outdoor Sofa</h3>
                    <p>$799</p>
                </div>
                <div class="item">
                    <img src="patio-chair.jpg" alt="Patio Chair">
                    <h3>Patio Chair</h3>
                    <p>$199</p>
                </div>
                <!-- Add more outdoor items here -->
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Furniture Shop. All Rights Reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #333;
    color: #fff;
    padding: 15px 0;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

.category {
    background: #fff;
    margin: 20px;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.item-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.item {
    flex: 1 1 calc(30% - 20px);
    margin: 10px;
    background: #f9f9f9;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
}

.item img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

footer {
    text-align: center;
    margin: 20px 0;
    padding: 10px 0;
    background: #333;
    color: #fff;
}
```
