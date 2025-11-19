"""
Generated Code Metadata:
========================
Original URL: https://aibanshee.com
Prompt: Generate a code snippet to create a responsive portfolio layout using CSS Grid, inspired by the portfolio types mentioned on the IMST Telehealth website.
Generated: DETERMINISTIC_240cae9e5f5b94ab
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
    <title>Responsive Portfolio Layout</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="portfolio-container">
        <div class="portfolio-item">
            <img src="image1.jpg" alt="Project 1 Image">
            <h2>Project 1 Title</h2>
            <p>Project 1 Description</p>
        </div>
        <div class="portfolio-item">
            <img src="image2.jpg" alt="Project 2 Image">
            <h2>Project 2 Title</h2>
            <p>Project 2 Description</p>
        </div>
        <div class="portfolio-item">
            <img src="image3.jpg" alt="Project 3 Image">
            <h2>Project 3 Title</h2>
            <p>Project 3 Description</p>
        </div>
        <!-- Add more portfolio items here -->
    </div>
</body>
</html>
```

```css
/* styles.css */

:root {
    --grid-columns: 3;
    --grid-gap: 20px;
    --item-width: 300px;
}

.portfolio-container {
    display: grid;
    grid-template-columns: repeat(var(--grid-columns), 1fr);
    grid-gap: var(--grid-gap);
    max-width: 1200px;
    margin: 40px auto;
}

.portfolio-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.portfolio-item img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.portfolio-item h2 {
    font-size: 24px;
    margin-top: 10px;
}

.portfolio-item p {
    font-size: 16px;
    color: #666;
}

/* Responsive layout adjustments */
@media (max-width: 768px) {
    :root {
        --grid-columns: 2;
    }
}

@media (max-width: 480px) {
    :root {
        --grid-columns: 1;
    }
    .portfolio-item {
        padding: 10px;
    }
    .portfolio-item img {
        height: 150px;
    }
}
```

```javascript
// script.js (optional, for dynamic portfolio item creation)

// Get the portfolio container element
const portfolioContainer = document.querySelector('.portfolio-container');

// Sample portfolio item data
const portfolioItems = [
    { image: 'image1.jpg', title: 'Project 1 Title', description: 'Project 1 Description' },
    { image: 'image2.jpg', title: 'Project 2 Title', description: 'Project 2 Description' },
    { image: 'image3.jpg', title: 'Project 3 Title', description: 'Project 3 Description' },
    // Add more portfolio items here
];

// Function to create a portfolio item element
function createPortfolioItem(item) {
    const itemElement = document.createElement('div');
    itemElement.classList.add('portfolio-item');

    const imageElement = document.createElement('img');
    imageElement.src = item.image;
    imageElement.alt = item.title;

    const titleElement = document.createElement('h2');
    titleElement.textContent = item.title;

    const descriptionElement = document.createElement('p');
    descriptionElement.textContent = item.description;

    itemElement.appendChild(imageElement);
    itemElement.appendChild(titleElement);
    itemElement.appendChild(descriptionElement);

    return itemElement;
}

// Create and append portfolio items dynamically
portfolioItems.forEach((item) => {
    const portfolioItemElement = createPortfolioItem(item);
    portfolioContainer.appendChild(portfolioItemElement);
});
```
