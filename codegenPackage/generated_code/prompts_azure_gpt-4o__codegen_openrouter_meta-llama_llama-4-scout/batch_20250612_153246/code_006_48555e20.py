"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: Write code to design a responsive website layout that highlights artistic categories such as sculptures, paintings, and flyers, as seen on "The Perfect Studio."
Generated: DETERMINISTIC_48555e2002c39d15
Batch ID: 20250612_153246
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
    <title>The Perfect Studio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#sculptures">Sculptures</a></li>
                <li><a href="#paintings">Paintings</a></li>
                <li><a href="#flyers">Flyers</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to The Perfect Studio</h1>
        <p>Explore our artistic categories</p>
    </section>

    <!-- Art Categories Section -->
    <section class="art-categories">
        <div class="category" id="sculptures">
            <h2>Sculptures</h2>
            <div class="art-grid">
                <div class="art-item">
                    <img src="sculpture1.jpg" alt="Sculpture 1">
                    <p>Sculpture 1 Description</p>
                </div>
                <div class="art-item">
                    <img src="sculpture2.jpg" alt="Sculpture 2">
                    <p>Sculpture 2 Description</p>
                </div>
            </div>
        </div>

        <div class="category" id="paintings">
            <h2>Paintings</h2>
            <div class="art-grid">
                <div class="art-item">
                    <img src="painting1.jpg" alt="Painting 1">
                    <p>Painting 1 Description</p>
                </div>
                <div class="art-item">
                    <img src="painting2.jpg" alt="Painting 2">
                    <p>Painting 2 Description</p>
                </div>
            </div>
        </div>

        <div class="category" id="flyers">
            <h2>Flyers</h2>
            <div class="art-grid">
                <div class="art-item">
                    <img src="flyer1.jpg" alt="Flyer 1">
                    <p>Flyer 1 Description</p>
                </div>
                <div class="art-item">
                    <img src="flyer2.jpg" alt="Flyer 2">
                    <p>Flyer 2 Description</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 The Perfect Studio</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

:root {
    --primary-color: #333;
    --secondary-color: #666;
    --background-color: #f9f9f9;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: var(--primary-color);
    background-color: var(--background-color);
}

header {
    background-color: var(--primary-color);
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

.hero {
    background-image: linear-gradient(to bottom, #f7f7f7, #ddd);
    padding: 5em;
    text-align: center;
}

.art-categories {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.category {
    margin: 20px;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.category h2 {
    margin-top: 0;
}

.art-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.art-item {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.art-item img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.art-item p {
    padding: 10px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 0 0 10px 10px;
}

footer {
    background-color: var(--primary-color);
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

/* Responsive Design */

@media only screen and (max-width: 768px) {
    .art-grid {
        grid-template-columns: repeat(1, 1fr);
    }
}

@media only screen and (max-width: 480px) {
    .hero {
        padding: 3em;
    }
    .category {
        margin: 10px;
        padding: 10px;
    }
}
```

```javascript
// script.js

// Add event listener to nav links
document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll("header nav a");

    navLinks.forEach((link) => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const targetId = link.getAttribute("href");
            const targetElement = document.querySelector(targetId);
            targetElement.scrollIntoView({ behavior: "smooth" });
        });
    });
});
```
