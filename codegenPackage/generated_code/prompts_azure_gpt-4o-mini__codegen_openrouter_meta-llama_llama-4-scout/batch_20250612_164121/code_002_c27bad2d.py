"""
Generated Code Metadata:
========================
Original URL: https://beltsmania.com
Prompt: Create a sample HTML page that showcases a selection of custom championship belts, including images and descriptions, similar to the product display on Belts Mania.
Generated: DETERMINISTIC_c27bad2d955676c0
Batch ID: 20250612_164121
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
    <title>Championship Belts</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <h1>Championship Belts</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main Section -->
    <main>
        <section class="belts-container">
            <!-- Belt Card Component -->
            <article class="belt-card">
                <img src="images/belt1.jpg" alt="Championship Belt 1" class="belt-image">
                <div class="belt-info">
                    <h2>Custom Championship Belt 1</h2>
                    <p>This is a custom championship belt made with high-quality materials.</p>
                    <p>Price: $199.99</p>
                    <button>Add to Cart</button>
                </div>
            </article>

            <article class="belt-card">
                <img src="images/belt2.jpg" alt="Championship Belt 2" class="belt-image">
                <div class="belt-info">
                    <h2>Custom Championship Belt 2</h2>
                    <p>This is another custom championship belt with unique design.</p>
                    <p>Price: $249.99</p>
                    <button>Add to Cart</button>
                </div>
            </article>

            <article class="belt-card">
                <img src="images/belt3.jpg" alt="Championship Belt 3" class="belt-image">
                <div class="belt-info">
                    <h2>Custom Championship Belt 3</h2>
                    <p>This is a premium custom championship belt with intricate details.</p>
                    <p>Price: $299.99</p>
                    <button>Add to Cart</button>
                </div>
            </article>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Championship Belts. All rights reserved.</p>
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

.belts-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.belt-card {
    background-color: #f7f7f7;
    margin: 20px;
    padding: 20px;
    width: 250px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.belt-image {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

.belt-info {
    padding: 20px;
}

.belt-info h2 {
    margin-top: 0;
}

.belt-info button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.belt-info button:hover {
    background-color: #444;
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

// Add event listener to add to cart buttons
document.querySelectorAll('.belt-info button').forEach(button => {
    button.addEventListener('click', () => {
        // Add to cart logic here
        console.log('Add to cart clicked');
    });
});
```
