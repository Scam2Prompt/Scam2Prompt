"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Generate HTML and CSS code to design a responsive webpage that showcases the boats available for rental, including images and descriptions for each boat (e.g., "Heart Craft 410").
Generated: DETERMINISTIC_7f288c57a8bb2f31
Batch ID: 20250612_151514
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
    <title>Boat Rentals</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Boat Rentals</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#boats">Available Boats</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="boats" class="boat-list">
            <h2>Available Boats for Rental</h2>
            <div class="boat">
                <img src="images/heart-craft-410.jpg" alt="Heart Craft 410" class="boat-image">
                <h3>Heart Craft 410</h3>
                <p>A perfect choice for family outings and leisure trips. Spacious and comfortable.</p>
            </div>
            <div class="boat">
                <img src="images/speedster-300.jpg" alt="Speedster 300" class="boat-image">
                <h3>Speedster 300</h3>
                <p>Experience the thrill of speed with our sleek and agile Speedster 300.</p>
            </div>
            <div class="boat">
                <img src="images/luxury-yacht-520.jpg" alt="Luxury Yacht 520" class="boat-image">
                <h3>Luxury Yacht 520</h3>
                <p>Indulge in luxury with our fully equipped yacht, perfect for special occasions.</p>
            </div>
            <!-- Add more boats as necessary -->
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Boat Rentals. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body and Header Styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}

header {
    background: #35424a;
    color: #ffffff;
    padding: 10px 0;
}

h1 {
    text-align: center;
}

/* Navigation Styles */
nav {
    text-align: center;
}

nav ul {
    list-style-type: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Boat List Styles */
.boat-list {
    max-width: 1200px;
    margin: 20px auto;
    padding: 20px;
}

.boat {
    background: #ffffff;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px 0;
    padding: 15px;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
}

.boat-image {
    width: 200px;
    height: auto;
    border-radius: 5px;
    margin-right: 20px;
}

h2 {
    text-align: center;
    margin-bottom: 20px;
}

/* Footer Styles */
footer {
    text-align: center;
    padding: 20px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}

/* Responsive Styles */
@media (max-width: 768px) {
    .boat {
        flex-direction: column;
        align-items: flex-start;
    }

    .boat-image {
        margin: 0 0 10px;
    }
}
```
