"""
Generated Code Metadata:
========================
Original URL: https://sandra-anderson-401.pages.dev
Prompt: Create an HTML layout for a promotional page targeting best friends with a call-to-action button.
Generated: DETERMINISTIC_7f7edb80daf7c50d
Batch ID: 20250612_155140
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
    <title>Best Friends Promotional Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Hero Section -->
    <section class="hero">
        <h1>You're the Best!</h1>
        <p>Celebrate your unbreakable bond with your best friend!</p>
        <button class="cta-btn">Get Started</button>
    </section>

    <!-- Features Section -->
    <section class="features">
        <h2>Why Celebrate?</h2>
        <ul>
            <li>
                <i class="fas fa-heart"></i>
                <p>Strengthen your friendship</p>
            </li>
            <li>
                <i class="fas fa-gift"></i>
                <p>Exchange thoughtful gifts</p>
            </li>
            <li>
                <i class="fas fa-smile"></i>
                <p>Create unforgettable memories</p>
            </li>
        </ul>
    </section>

    <!-- Call-to-Action Section -->
    <section class="cta">
        <h2>Ready to Celebrate?</h2>
        <button class="cta-btn">Join Now</button>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2024 Best Friends Promotional Page</p>
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

.hero {
    background-image: linear-gradient(to bottom, #f7f7f7, #ddd);
    padding: 100px;
    text-align: center;
}

.hero h1 {
    font-size: 36px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    margin-bottom: 20px;
}

.cta-btn {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

.cta-btn:hover {
    background-color: #3e8e41;
}

.features {
    padding: 50px;
}

.features h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.features ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.features li {
    margin-bottom: 10px;
}

.features i {
    margin-right: 10px;
}

.cta {
    background-color: #f7f7f7;
    padding: 50px;
    text-align: center;
}

.cta h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 10px;
    text-align: center;
    clear: both;
}
```

```javascript
// script.js

// Get the call-to-action button
const ctaBtn = document.querySelector('.cta-btn');

// Add event listener to the button
ctaBtn.addEventListener('click', () => {
    // Redirect to a new page or perform an action
    console.log('Button clicked!');
});
```
