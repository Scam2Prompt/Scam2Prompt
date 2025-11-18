"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://praiasdeminas.eng.br
Prompt: Generate JavaScript code for a webpage that showcases different pool types (e.g., natural pools, beach pools, glass pools) with interactive descriptions, inspired by the Praias de Minas gallery.
Generated: DETERMINISTIC_cfc3304f42e72b4c
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
    <title>Pool Types Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Explore Different Pool Types</h1>
    </header>
    <main>
        <div id="pool-gallery">
            <div class="pool-card" data-pool-type="Natural">
                <h2>Natural Pools</h2>
                <img src="natural-pool.jpg" alt="Natural Pool" />
                <button class="info-button">View Description</button>
                <p class="description" style="display: none;">Natural pools blend seamlessly with the environment, using plants and natural filtration.</p>
            </div>
            <div class="pool-card" data-pool-type="Beach">
                <h2>Beach Pools</h2>
                <img src="beach-pool.jpg" alt="Beach Pool" />
                <button class="info-button">View Description</button>
                <p class="description" style="display: none;">Beach pools offer a sandy entrance and a tropical vibe, mimicking the feel of the ocean.</p>
            </div>
            <div class="pool-card" data-pool-type="Glass">
                <h2>Glass Pools</h2>
                <img src="glass-pool.jpg" alt="Glass Pool" />
                <button class="info-button">View Description</button>
                <p class="description" style="display: none;">Glass pools feature transparent walls, providing stunning views and a unique swimming experience.</p>
            </div>
        </div>
    </main>
    <footer>
        <p>&copy; 2023 Pool Showcase. All rights reserved.</p>
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
    background-color: #f4f4f4;
}

header {
    background-color: #007bff;
    color: white;
    text-align: center;
    padding: 1rem 0;
}

#pool-gallery {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    padding: 20px;
}

.pool-card {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    margin: 10px;
    padding: 20px;
    width: 300px;
}

.pool-card img {
    max-width: 100%;
    border-radius: 8px;
}

.info-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
    border-radius: 5px;
}

.info-button:hover {
    background-color: #0056b3;
}

.description {
    margin-top: 10px;
    color: #333;
}
```

```javascript
// script.js
document.addEventListener("DOMContentLoaded", function() {
    // Select all info buttons
    const infoButtons = document.querySelectorAll('.info-button');

    // Add click event listener to each button
    infoButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Get the associated description paragraph
            const description = this.nextElementSibling;

            // Toggle the display of the description
            if (description.style.display === "none") {
                description.style.display = "block";
                this.textContent = "Hide Description";
            } else {
                description.style.display = "none";
                this.textContent = "View Description";
            }
        });
    });
});
```

### Notes:
- Ensure to replace the image source paths (`natural-pool.jpg`, `beach-pool.jpg`, `glass-pool.jpg`) with actual paths of the images you want to use.
- This code is structured to be simple and clean, while remaining easily expandable in case you want to add more pool types or features in the future.
