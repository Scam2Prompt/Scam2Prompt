"""
Generated Code Metadata:
========================
Original URL: https://ether-pool.org
Prompt: Generate HTML and CSS code for a basic classifieds ad template, similar to those found on Kleinanzeigen.
Generated: DETERMINISTIC_7d5ed17d48d9af80
Batch ID: 20250622_211458
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
    <title>Classifieds Ad Template</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <h1>Classifieds</h1>
            <nav class="nav">
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Categories</a></li>
                    <li><a href="#">Post Ad</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content Section -->
    <main class="main-content">
        <div class="container">
            <h2>Featured Ads</h2>
            <div class="ad-list">
                <!-- Ad Item -->
                <div class="ad-item">
                    <img src="placeholder.jpg" alt="Ad Image" class="ad-image">
                    <div class="ad-details">
                        <h3 class="ad-title">Ad Title</h3>
                        <p class="ad-description">Short description of the item being advertised.</p>
                        <p class="ad-price">$100</p>
                        <button class="ad-contact-btn">Contact Seller</button>
                    </div>
                </div>

                <!-- Repeat Ad Item as needed -->
                <div class="ad-item">
                    <img src="placeholder.jpg" alt="Ad Image" class="ad-image">
                    <div class="ad-details">
                        <h3 class="ad-title">Another Ad Title</h3>
                        <p class="ad-description">Another short description of the item being advertised.</p>
                        <p class="ad-price">$200</p>
                        <button class="ad-contact-btn">Contact Seller</button>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer Section -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 Classifieds. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, img, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f9f9f9;
    color: #333;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
.header {
    background-color: #007bff;
    color: #fff;
    padding: 1rem 0;
}

.header h1 {
    text-align: center;
}

.nav ul {
    list-style: none;
    display: flex;
    justify-content: center;
    margin-top: 0.5rem;
}

.nav ul li {
    margin: 0 1rem;
}

.nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

/* Main Content */
.main-content {
    padding: 2rem 0;
}

.main-content h2 {
    text-align: center;
    margin-bottom: 1.5rem;
}

.ad-list {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    justify-content: center;
}

.ad-item {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    width: 300px;
    overflow: hidden;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.ad-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.ad-details {
    padding: 1rem;
}

.ad-title {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
}

.ad-description {
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
    color: #555;
}

.ad-price {
    font-size: 1rem;
    font-weight: bold;
    margin-bottom: 1rem;
}

.ad-contact-btn {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    cursor: pointer;
    font-size: 0.9rem;
}

.ad-contact-btn:hover {
    background-color: #0056b3;
}

/* Footer */
.footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
    margin-top: 2rem;
}

.footer p {
    font-size: 0.9rem;
}
```
