"""
Generated Code Metadata:
========================
Original URL: https://berachain.stride.co
Prompt: "Design a basic HTML/CSS template for a domain sale landing page, inspired by the layout and content of Stride.co for sale listings."
Generated: DETERMINISTIC_01d162a1946f2379
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Sale Landing Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="hero">
            <h1>Premium Domain for Sale</h1>
            <p>Unlock the full potential of your online presence</p>
            <button>Learn More</button>
        </section>
        <section class="domain-info">
            <h2>Domain Details</h2>
            <ul>
                <li><strong>Domain Name:</strong> example.com</li>
                <li><strong>Price:</strong> $10,000</li>
                <li><strong>Category:</strong> Business</li>
                <li><strong>Age:</strong> 10 years</li>
            </ul>
        </section>
        <section class="features">
            <h2>Why This Domain?</h2>
            <ul>
                <li><i class="checkmark"></i> High-traffic potential</li>
                <li><i class="checkmark"></i> Memorable and brandable</li>
                <li><i class="checkmark"></i> Perfect for business or investment</li>
            </ul>
        </section>
        <section class="testimonials">
            <h2>What Our Clients Say</h2>
            <blockquote>
                <p>We were blown away by the quality of the domain and the professionalism of the seller.</p>
                <cite>John Doe, CEO of Example Inc.</cite>
            </blockquote>
        </section>
        <section class="call-to-action">
            <h2>Ready to Make an Offer?</h2>
            <button>Contact Us</button>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Domain Sale Landing Page</p>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
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
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
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

.domain-info {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

.domain-info ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.domain-info li {
    margin-bottom: 10px;
}

.features {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

.features ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.features li {
    margin-bottom: 10px;
}

.features .checkmark {
    font-size: 18px;
    color: #008000;
    margin-right: 10px;
}

.testimonials {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

.testimonials blockquote {
    border-left: 4px solid #333;
    padding-left: 10px;
}

.testimonials cite {
    font-size: 14px;
    color: #666;
}

.call-to-action {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

.call-to-action button {
    background-color: #555;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

button:hover {
    background-color: #555;
}
```
