"""
Generated Code Metadata:
========================
Original URL: https://olaf-schirm.de
Prompt: Design a simple web application that showcases Olaf Schirm's physical and digital artworks, including interactive elements for the "Wunderkammer" section.
Generated: DETERMINISTIC_3fc769607491e4a8
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Olaf Schirm Art Gallery Web Application**
=============================================

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Olaf Schirm Art Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#physical-artworks">Physical Artworks</a></li>
                <li><a href="#digital-artworks">Digital Artworks</a></li>
                <li><a href="#wunderkammer">Wunderkammer</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="physical-artworks">
            <h1>Physical Artworks</h1>
            <div class="artwork-grid">
                <!-- artwork images will be generated dynamically -->
            </div>
        </section>
        <section id="digital-artworks">
            <h1>Digital Artworks</h1>
            <div class="artwork-grid">
                <!-- artwork images will be generated dynamically -->
            </div>
        </section>
        <section id="wunderkammer">
            <h1>Wunderkammer</h1>
            <div class="wunderkammer-container">
                <canvas id="wunderkammer-canvas" width="800" height="600"></canvas>
                <script src="wunderkammer.js"></script>
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

### styles.css
```css
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

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

nav li {
    margin-right: 20px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.artwork-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 10px;
}

.wunderkammer-container {
    position: relative;
}

#wunderkammer-canvas {
    border: 1px solid #000;
}
```

### script.js
```javascript
// Get artwork data from API or database
fetch('/api/artworks')
    .then(response => response.json())
    .then(artworks => {
        const physicalArtworksSection = document.querySelector('#physical-artworks .artwork-grid');
        const digitalArtworksSection = document.querySelector('#digital-artworks .artwork-grid');

        artworks.forEach(artwork => {
            const artworkHTML = `
                <img src="${artwork.image}" alt="${artwork.title}">
                <p>${artwork.title}</p>
            `;

            if (artwork.type === 'physical') {
                physicalArtworksSection.insertAdjacentHTML('beforeend', artworkHTML);
            } else if (artwork.type === 'digital') {
                digitalArtworksSection.insertAdjacentHTML('beforeend', artworkHTML);
            }
        });
    })
    .catch(error => console.error('Error fetching artworks:', error));
```

### wunderkammer.js
```javascript
// Get canvas element
const canvas = document.getElementById('wunderkammer-canvas');
const ctx = canvas.getContext('2d');

// Set up interactive elements
let isDragging = false;
let offset = [0, 0];

canvas.addEventListener('mousedown', (event) => {
    isDragging = true;
    offset = [canvas.offsetLeft - event.clientX, canvas.offsetTop - event.clientY];
});

document.addEventListener('mouseup', () => {
    isDragging = false;
});

document.addEventListener('mousemove', (event) => {
    if (isDragging) {
        canvas.style.top = `${event.clientY + offset[1]}px`;
        canvas.style.left = `${event.clientX + offset[0]}px`;
    }
});

// Draw Wunderkammer artwork
ctx.fillStyle = '#fff';
ctx.fillRect(0, 0, canvas.width, canvas.height);

ctx.font = '24px Arial';
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';
ctx.fillStyle = '#000';
ctx.fillText('Wunderkammer', canvas.width / 2, canvas.height / 2);
```

### server.js (using Node.js and Express)
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Artwork data (replace with database or API call)
const artworks = [
    { id: 1, title: 'Artwork 1', image: 'artwork1.jpg', type: 'physical' },
    { id: 2, title: 'Artwork 2', image: 'artwork2.jpg', type: 'digital' },
    // ...
];

app.use(express.static('public'));

app.get('/api/artworks', (req, res) => {
    res.json(artworks);
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
