"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: Write HTML and CSS code to showcase a gallery of past projects, similar to the "Projects" section on "The Fence Guys" website, with filters for fences, decks, and pergolas.
Generated: DETERMINISTIC_618b57ac3bf3a319
Batch ID: 20250612_153246
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
    <title>Project Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Our Past Projects</h1>
        <nav>
            <ul>
                <li><button class="filter-button" data-filter="all">All</button></li>
                <li><button class="filter-button" data-filter="fences">Fences</button></li>
                <li><button class="filter-button" data-filter="decks">Decks</button></li>
                <li><button class="filter-button" data-filter="pergolas">Pergolas</button></li>
            </ul>
        </nav>
    </header>

    <main>
        <div class="gallery">
            <div class="project-item fences">
                <img src="fence1.jpg" alt="Wooden Fence Project">
                <h2>Wooden Fence</h2>
            </div>
            <div class="project-item decks">
                <img src="deck1.jpg" alt="Composite Deck Project">
                <h2>Composite Deck</h2>
            </div>
            <div class="project-item pergolas">
                <img src="pergola1.jpg" alt="Aluminum Pergola Project">
                <h2>Aluminum Pergola</h2>
            </div>
            <div class="project-item fences">
                <img src="fence2.jpg" alt="Vinyl Fence Project">
                <h2>Vinyl Fence</h2>
            </div>
            <div class="project-item decks">
                <img src="deck2.jpg" alt="Wood Deck Project">
                <h2>Wood Deck</h2>
            </div>
            <div class="project-item pergolas">
                <img src="pergola2.jpg" alt="Wood Pergola Project">
                <h2>Wood Pergola</h2>
            </div>
        </div>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styling */
header {
    background-color: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Navigation styling */
nav ul {
    list-style-type: none;
    padding: 0;
}

nav li {
    display: inline;
    margin: 0 10px;
}

/* Button styling */
.filter-button {
    background-color: #fff;
    border: 1px solid #007BFF;
    color: #007BFF;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s, color 0.3s;
}

.filter-button:hover {
    background-color: #007BFF;
    color: white;
}

/* Gallery styling */
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 20px;
}

.project-item {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    overflow: hidden;
    width: 300px;
    transition: transform 0.3s;
}

.project-item img {
    width: 100%;
    height: auto;
}

.project-item h2 {
    padding: 10px;
    text-align: center;
}

/* Hover effect for project items */
.project-item:hover {
    transform: scale(1.05);
}
```

```javascript
// script.js

// Function to filter project items based on selected category
document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('.filter-button');
    const projectItems = document.querySelectorAll('.project-item');

    // Add click event listener to each filter button
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const filter = button.getAttribute('data-filter');

            // Show or hide project items based on the selected filter
            projectItems.forEach(item => {
                if (filter === 'all' || item.classList.contains(filter)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
});
```
