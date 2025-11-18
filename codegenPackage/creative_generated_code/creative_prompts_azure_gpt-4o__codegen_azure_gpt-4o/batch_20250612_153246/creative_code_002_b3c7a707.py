"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Create a function in JavaScript to filter furniture products by categories like "chairs," "tables," or "accessories," and display them in a carousel format similar to the Nodo Italia website.
Generated: DETERMINISTIC_b3c7a707716432a4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters furniture products by category and displays them in a carousel format.
 * 
 * @param {Array} products - Array of product objects. Each object should include `name`, `category`, and `image` properties.
 * @param {string} category - The category to filter by (e.g., "chairs", "tables", "accessories").
 */
function displayFurnitureCarousel(products, category) {
    try {
        // Validate input
        if (!Array.isArray(products)) {
            throw new Error("Invalid input: 'products' must be an array.");
        }
        if (typeof category !== "string") {
            throw new Error("Invalid input: 'category' must be a string.");
        }

        // Filter products by the specified category
        const filteredProducts = products.filter(product => product.category === category);

        // Check if there are products in the selected category
        if (filteredProducts.length === 0) {
            console.warn(`No products found for category: ${category}`);
            return;
        }

        // Create carousel container
        const carouselContainer = document.createElement("div");
        carouselContainer.className = "furniture-carousel";

        // Add carousel items
        filteredProducts.forEach(product => {
            const item = document.createElement("div");
            item.className = "carousel-item";

            // Image element
            const image = document.createElement("img");
            image.src = product.image;
            image.alt = product.name;
            image.className = "carousel-image";

            // Product name
            const name = document.createElement("div");
            name.textContent = product.name;
            name.className = "carousel-name";

            // Append elements to the item
            item.appendChild(image);
            item.appendChild(name);

            // Append item to the carousel container
            carouselContainer.appendChild(item);
        });

        // Display carousel on the page
        const carouselWrapper = document.getElementById("carousel-wrapper");
        if (!carouselWrapper) {
            throw new Error("Carousel wrapper element with ID 'carousel-wrapper' not found.");
        }
        carouselWrapper.innerHTML = ""; // Clear any existing content
        carouselWrapper.appendChild(carouselContainer);

        // Apply basic styling for the carousel (Optional)
        applyCarouselStyles();
    } catch (error) {
        console.error("Error in displayFurnitureCarousel:", error.message);
    }
}

/**
 * Applies basic styling to the carousel for presentation purposes.
 * This function may be replaced with a CSS file for production use.
 */
function applyCarouselStyles() {
    const style = `
        .furniture-carousel {
            display: flex;
            gap: 16px;
            overflow-x: auto;
            padding: 16px;
            border: 1px solid #ddd;
            border-radius: 8px;
            background-color: #f9f9f9;
        }
        .carousel-item {
            flex: 0 0 auto;
            text-align: center;
            width: 150px;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 8px;
            background-color: #fff;
        }
        .carousel-image {
            width: 100%;
            height: 100px;
            object-fit: cover;
            border-radius: 4px;
        }
        .carousel-name {
            margin-top: 8px;
            font-size: 14px;
            color: #333;
        }
    `;

    const styleElement = document.createElement("style");
    styleElement.textContent = style;
    document.head.appendChild(styleElement);
}

// Example usage:
const furnitureProducts = [
    { name: "Office Chair", category: "chairs", image: "chair1.jpg" },
    { name: "Dining Table", category: "tables", image: "table1.jpg" },
    { name: "Lamp", category: "accessories", image: "lamp1.jpg" },
    { name: "Gaming Chair", category: "chairs", image: "chair2.jpg" },
];

displayFurnitureCarousel(furnitureProducts, "chairs");
```

To test this code, make sure you have an HTML element with `id="carousel-wrapper"` in your document where the carousel will be displayed. For example:

```html
<div id="carousel-wrapper"></div>
```
