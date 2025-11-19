"""
Generated Code Metadata:
========================
Original URL: https://tiburonfishingreels.com
Prompt: Develop a user interface design for a fishing reel product page that highlights the unique features of Tiburon's automatic-shifting reels.
Generated: DETERMINISTIC_05c03a77f7182b2f
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tiburon Automatic-Shifting Reels</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#features">Features</a></li>
                <li><a href="#specs">Specs</a></li>
                <li><a href="#reviews">Reviews</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Tiburon Automatic-Shifting Reels</h1>
        <p>Experience the future of fishing with Tiburon's revolutionary automatic-shifting reels.</p>
        <button>Learn More</button>
        <img src="tiburon-reel.jpg" alt="Tiburon Reel">
    </section>

    <!-- Features Section -->
    <section id="features">
        <h2>Unique Features</h2>
        <div class="feature-cards">
            <div class="feature-card">
                <h3>Automatic-Shifting Technology</h3>
                <p>Our reels automatically adjust gear ratios for optimal performance.</p>
            </div>
            <div class="feature-card">
                <h3>Smart Sensor</h3>
                <p>Our advanced sensor technology detects changes in fishing conditions and adjusts the reel accordingly.</p>
            </div>
            <div class="feature-card">
                <h3>Durable Design</h3>
                <p>Our reels are built with high-quality materials to withstand the rigors of frequent use.</p>
            </div>
        </div>
    </section>

    <!-- Specs Section -->
    <section id="specs">
        <h2>Specifications</h2>
        <table>
            <thead>
                <tr>
                    <th>Model</th>
                    <th>Gear Ratio</th>
                    <th>Line Capacity</th>
                    <th>Weight</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Tiburon TR-100</td>
                    <td>4.5:1</td>
                    <td>150 yards / 15 lb</td>
                    <td>12 oz</td>
                </tr>
                <tr>
                    <td>Tiburon TR-200</td>
                    <td>5.2:1</td>
                    <td>200 yards / 20 lb</td>
                    <td>15 oz</td>
                </tr>
            </tbody>
        </table>
    </section>

    <!-- Reviews Section -->
    <section id="reviews">
        <h2>What Our Customers Say</h2>
        <div class="review-cards">
            <div class="review-card">
                <p>"The Tiburon reel has taken my fishing game to the next level. The automatic-shifting technology is a game-changer!"</p>
                <p>— John D.</p>
            </div>
            <div class="review-card">
                <p>"I've never had a reel that's so easy to use. The smart sensor is incredibly accurate."</p>
                <p>— Sarah K.</p>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Tiburon Reels. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

.hero p {
    font-size: 18px;
}

.feature-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.feature-card {
    background-color: #f7f7f7;
    padding: 20px;
    margin: 20px;
    width: 200px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.feature-card h3 {
    margin-top: 0;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

th {
    background-color: #f0f0f0;
}

.review-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.review-card {
    background-color: #f7f7f7;
    padding: 20px;
    margin: 20px;
    width: 200px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

```javascript
// script.js

// Add event listener to learn more button
document.querySelector('.hero button').addEventListener('click', () => {
    // Scroll to features section
    document.querySelector('#features').scrollIntoView({ behavior: 'smooth' });
});

// Add event listener to nav links
document.querySelectorAll('header nav a').forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        // Scroll to corresponding section
        document.querySelector(link.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
    });
});
```
