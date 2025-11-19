"""
Generated Code Metadata:
========================
Original URL: https://uiriocabrabrazzz.blogspot.com
Prompt: Create a simple HTML/CSS template for a retailer's website that incorporates dynamic window display showcases, reflecting the importance of visual appeal in vitrinismo and visual merchandising.
Generated: DETERMINISTIC_71c86f9a88f8ed9c
Batch ID: 20250622_212605
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
    <title>Retailer Website</title>
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
        <section class="showcase">
            <div class="showcase-container">
                <div class="showcase-item active">
                    <img src="image1.jpg" alt="Product 1">
                    <div class="showcase-overlay">
                        <h2>Product 1</h2>
                        <p>$19.99</p>
                    </div>
                </div>
                <div class="showcase-item">
                    <img src="image2.jpg" alt="Product 2">
                    <div class="showcase-overlay">
                        <h2>Product 2</h2>
                        <p>$29.99</p>
                    </div>
                </div>
                <div class="showcase-item">
                    <img src="image3.jpg" alt="Product 3">
                    <div class="showcase-overlay">
                        <h2>Product 3</h2>
                        <p>$39.99</p>
                    </div>
                </div>
            </div>
            <div class="showcase-controls">
                <button class="prev-btn">&#10094;</button>
                <button class="next-btn">&#10095;</button>
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
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

.showcase {
    position: relative;
    width: 80%;
    margin: 40px auto;
}

.showcase-container {
    position: relative;
    width: 100%;
    height: 500px;
}

.showcase-item {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: none;
}

.showcase-item.active {
    display: block;
}

.showcase-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.showcase-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
    padding: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.showcase-overlay h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.showcase-controls {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
}

.prev-btn, .next-btn {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

.prev-btn:hover, .next-btn:hover {
    background-color: #555;
}
```

**script.js**
```javascript
// Get the showcase items and controls
const showcaseItems = document.querySelectorAll('.showcase-item');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

// Set the active showcase item
let activeIndex = 0;
showcaseItems[activeIndex].classList.add('active');

// Add event listeners to the controls
prevBtn.addEventListener('click', () => {
    showcaseItems[activeIndex].classList.remove('active');
    activeIndex = (activeIndex - 1 + showcaseItems.length) % showcaseItems.length;
    showcaseItems[activeIndex].classList.add('active');
});

nextBtn.addEventListener('click', () => {
    showcaseItems[activeIndex].classList.remove('active');
    activeIndex = (activeIndex + 1) % showcaseItems.length;
    showcaseItems[activeIndex].classList.add('active');
});

// Auto-rotate the showcase items
setInterval(() => {
    nextBtn.click();
}, 5000);
```
