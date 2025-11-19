"""
Generated Code Metadata:
========================
Original URL: https://praiasdeminas.eng.br
Prompt: Generate JavaScript code for a webpage that showcases different pool types (e.g., natural pools, beach pools, glass pools) with interactive descriptions, inspired by the Praias de Minas gallery.
Generated: DETERMINISTIC_cfc3304f42e72b4c
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
    <title>Pool Types Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Explore Different Pool Types</h1>
    </header>
    <main>
        <section id="pool-gallery">
            <div class="pool-card" data-pool-type="natural">
                <img src="images/natural_pool.jpg" alt="Natural Pool" />
                <h2>Natural Pools</h2>
                <button class="info-button">Show Description</button>
                <p class="description hidden">Natural pools are eco-friendly swimming areas that use plants and natural filtration systems to keep the water clean.</p>
            </div>
            <div class="pool-card" data-pool-type="beach">
                <img src="images/beach_pool.jpg" alt="Beach Pool" />
                <h2>Beach Pools</h2>
                <button class="info-button">Show Description</button>
                <p class="description hidden">Beach pools mimic the feel of a beach with sandy shores and gentle waves, perfect for relaxation.</p>
            </div>
            <div class="pool-card" data-pool-type="glass">
                <img src="images/glass_pool.jpg" alt="Glass Pool" />
                <h2>Glass Pools</h2>
                <button class="info-button">Show Description</button>
                <p class="description hidden">Glass pools offer a stunning visual experience, often featuring transparent walls that create a unique swimming experience.</p>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Pool Types Showcase. All rights reserved.</p>
    </footer>
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

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
}

header {
    background-color: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

main {
    padding: 20px;
}

#pool-gallery {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}

.pool-card {
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin: 10px;
    padding: 15px;
    width: 300px;
    text-align: center;
    transition: transform 0.2s;
}

.pool-card:hover {
    transform: scale(1.05);
}

.description {
    margin-top: 10px;
}

.hidden {
    display: none;
}

.info-button {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

.info-button:hover {
    background-color: #218838;
}
```

```javascript
// script.js

// Function to toggle the visibility of the pool description
function toggleDescription(event) {
    const description = event.target.nextElementSibling;
    if (description) {
        description.classList.toggle('hidden');
    }
}

// Add event listeners to all info buttons
document.querySelectorAll('.info-button').forEach(button => {
    button.addEventListener('click', toggleDescription);
});
```

This code creates a simple webpage that showcases different types of pools with interactive descriptions. Each pool type has an image, a title, and a button to show or hide the description. The CSS styles the layout and appearance, while the JavaScript handles the interactivity.
