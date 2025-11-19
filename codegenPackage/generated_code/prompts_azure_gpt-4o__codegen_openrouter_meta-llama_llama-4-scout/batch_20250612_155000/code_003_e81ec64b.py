"""
Generated Code Metadata:
========================
Original URL: https://la-guarida.com.ar
Prompt: Create a responsive web design template for showcasing a portfolio of work, inspired by La Guarida's "Our Work" section.
Generated: DETERMINISTIC_e81ec64bc9c5033a
Batch ID: 20250612_155000
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
    <title>Portfolio Template</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#all">All</a></li>
                <li><a href="#web-development">Web Development</a></li>
                <li><a href="#graphic-design">Graphic Design</a></li>
                <li><a href="#photography">Photography</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="portfolio">
            <div class="filter-buttons">
                <button class="active" data-filter="all">All</button>
                <button data-filter="web-development">Web Development</button>
                <button data-filter="graphic-design">Graphic Design</button>
                <button data-filter="photography">Photography</button>
            </div>
            <div class="portfolio-grid">
                <div class="portfolio-item" data-category="web-development">
                    <img src="img/project1.jpg" alt="Project 1">
                    <h3>Project 1</h3>
                    <p>Web development project</p>
                </div>
                <div class="portfolio-item" data-category="graphic-design">
                    <img src="img/project2.jpg" alt="Project 2">
                    <h3>Project 2</h3>
                    <p>Graphic design project</p>
                </div>
                <div class="portfolio-item" data-category="photography">
                    <img src="img/project3.jpg" alt="Project 3">
                    <h3>Project 3</h3>
                    <p>Photography project</p>
                </div>
                <div class="portfolio-item" data-category="web-development">
                    <img src="img/project4.jpg" alt="Project 4">
                    <h3>Project 4</h3>
                    <p>Web development project</p>
                </div>
                <div class="portfolio-item" data-category="graphic-design">
                    <img src="img/project5.jpg" alt="Project 5">
                    <h3>Project 5</h3>
                    <p>Graphic design project</p>
                </div>
                <div class="portfolio-item" data-category="photography">
                    <img src="img/project6.jpg" alt="Project 6">
                    <h3>Project 6</h3>
                    <p>Photography project</p>
                </div>
            </div>
        </section>
    </main>
    <script src="script.js"></script>
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

header nav a:hover {
    color: #ccc;
}

/* Portfolio Styles */
.portfolio {
    max-width: 1200px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.filter-buttons {
    margin-bottom: 20px;
}

.filter-buttons button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.filter-buttons button.active {
    background-color: #555;
}

.filter-buttons button:hover {
    background-color: #444;
}

.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.portfolio-item {
    background-color: #fff;
    border: 1px solid #ddd;
    padding: 20px;
}

.portfolio-item img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.portfolio-item h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

.portfolio-item p {
    font-size: 16px;
    color: #666;
}

/* Responsive Styles */
@media (max-width: 768px) {
    .portfolio-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 480px) {
    .portfolio-grid {
        grid-template-columns: 1fr;
    }
}
```

**script.js**
```javascript
// Get filter buttons and portfolio items
const filterButtons = document.querySelectorAll('.filter-buttons button');
const portfolioItems = document.querySelectorAll('.portfolio-item');

// Add event listeners to filter buttons
filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Get filter category
        const filterCategory = button.getAttribute('data-filter');

        // Filter portfolio items
        portfolioItems.forEach(item => {
            const itemCategory = item.getAttribute('data-category');
            if (filterCategory === 'all' || itemCategory === filterCategory) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });

        // Update active button
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
    });
});
```
