"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenceguys4u.com
Prompt: Write HTML and CSS code to showcase a gallery of past projects, similar to the "Projects" section on "The Fence Guys" website, with filters for fences, decks, and pergolas.
Generated: DETERMINISTIC_618b57ac3bf3a319
Batch ID: 20250612_153246
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
    <title>Project Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Our Past Projects</h1>
        <nav>
            <ul>
                <li><button class="filter-btn" data-filter="all">All</button></li>
                <li><button class="filter-btn" data-filter="fences">Fences</button></li>
                <li><button class="filter-btn" data-filter="decks">Decks</button></li>
                <li><button class="filter-btn" data-filter="pergolas">Pergolas</button></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="gallery">
            <div class="project fences">
                <img src="fence1.jpg" alt="Wooden Fence Project">
                <h2>Wooden Fence</h2>
                <p>A beautiful wooden fence project completed in 2022.</p>
            </div>
            <div class="project decks">
                <img src="deck1.jpg" alt="Composite Deck Project">
                <h2>Composite Deck</h2>
                <p>A modern composite deck crafted for outdoor relaxation.</p>
            </div>
            <div class="project pergolas">
                <img src="pergola1.jpg" alt="Pergola Project">
                <h2>Garden Pergola</h2>
                <p>A charming pergola that enhances garden aesthetics.</p>
            </div>
            <div class="project fences">
                <img src="fence2.jpg" alt="Vinyl Fence Project">
                <h2>Vinyl Fence</h2>
                <p>A low-maintenance vinyl fence installed in 2021.</p>
            </div>
            <div class="project decks">
                <img src="deck2.jpg" alt="Wood Deck Project">
                <h2>Wood Deck</h2>
                <p>A classic wood deck perfect for family gatherings.</p>
            </div>
            <div class="project pergolas">
                <img src="pergola2.jpg" alt="Attached Pergola Project">
                <h2>Attached Pergola</h2>
                <p>An attached pergola providing shade and elegance.</p>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 The Fence Guys. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic resets */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav li {
    display: inline;
    margin: 0 10px;
}

/* Button styles */
.filter-btn {
    background: #e8491d;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
}

.filter-btn:hover {
    background: #c6391a;
}

/* Gallery styles */
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 20px;
}

.project {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 15px;
    max-width: 300px;
    overflow: hidden;
    transition: transform 0.2s;
}

.project img {
    width: 100%;
    height: auto;
}

.project h2 {
    padding: 10px;
    font-size: 1.5em;
}

.project p {
    padding: 0 10px 10px;
}

/* Hover effect on project */
.project:hover {
    transform: scale(1.05);
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px 0;
    background: #35424a;
    color: #ffffff;
}
```

```javascript
// script.js

// Functionality for filtering projects
document.addEventListener("DOMContentLoaded", () => {
    const filterButtons = document.querySelectorAll(".filter-btn");
    const projects = document.querySelectorAll(".project");

    filterButtons.forEach(button => {
        button.addEventListener("click", () => {
            const filter = button.dataset.filter;
            projects.forEach(project => {
                // Show all projects or filter by category
                if (filter === "all" || project.classList.contains(filter)) {
                    project.style.display = "block";
                } else {
                    project.style.display = "none";
                }
            });
        });
    });
});
```
