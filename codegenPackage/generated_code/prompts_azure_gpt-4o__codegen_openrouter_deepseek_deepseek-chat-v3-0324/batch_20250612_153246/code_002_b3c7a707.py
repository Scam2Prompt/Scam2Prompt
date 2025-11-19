"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Create a function in JavaScript to filter furniture products by categories like "chairs," "tables," or "accessories," and display them in a carousel format similar to the Nodo Italia website.
Generated: DETERMINISTIC_b3c7a707716432a4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters and displays furniture products by category in a carousel format.
 * @param {Array} products - Array of product objects to filter.
 * @param {string} category - Category to filter by (e.g., "chairs", "tables", "accessories").
 * @param {string} carouselId - ID of the carousel container element.
 */
function filterAndDisplayProducts(products, category, carouselId) {
    try {
        // Validate inputs
        if (!Array.isArray(products)) {
            throw new Error('Products must be an array');
        }
        if (typeof category !== 'string' || category.trim() === '') {
            throw new Error('Category must be a non-empty string');
        }
        if (typeof carouselId !== 'string' || carouselId.trim() === '') {
            throw new Error('Carousel ID must be a non-empty string');
        }

        // Filter products by category (case-insensitive)
        const filteredProducts = products.filter(product => 
            product.category.toLowerCase() === category.toLowerCase()
        );

        // Get carousel container
        const carouselContainer = document.getElementById(carouselId);
        if (!carouselContainer) {
            throw new Error(`Carousel container with ID '${carouselId}' not found`);
        }

        // Clear previous content
        carouselContainer.innerHTML = '';

        // Create carousel items
        if (filteredProducts.length === 0) {
            carouselContainer.innerHTML = '<p>No products found in this category.</p>';
            return;
        }

        const carouselInner = document.createElement('div');
        carouselInner.className = 'carousel-inner';

        filteredProducts.forEach((product, index) => {
            const carouselItem = document.createElement('div');
            carouselItem.className = `carousel-item ${index === 0 ? 'active' : ''}`;

            const productCard = `
                <div class="product-card">
                    <img src="${product.imageUrl}" alt="${product.name}" class="product-image">
                    <div class="product-info">
                        <h3 class="product-name">${product.name}</h3>
                        <p class="product-price">$${product.price.toFixed(2)}</p>
                        <p class="product-description">${product.description}</p>
                    </div>
                </div>
            `;

            carouselItem.innerHTML = productCard;
            carouselInner.appendChild(carouselItem);
        });

        // Add navigation controls
        const carouselControls = `
            <button class="carousel-control prev" onclick="moveCarousel('${carouselId}', -1)">❮</button>
            <button class="carousel-control next" onclick="moveCarousel('${carouselId}', 1)">❯</button>
        `;

        carouselContainer.appendChild(carouselInner);
        carouselContainer.insertAdjacentHTML('beforeend', carouselControls);

    } catch (error) {
        console.error('Error filtering and displaying products:', error.message);
        const errorContainer = document.getElementById(carouselId);
        if (errorContainer) {
            errorContainer.innerHTML = `<p class="error">Error: ${error.message}</p>`;
        }
    }
}

/**
 * Moves the carousel to the previous or next item.
 * @param {string} carouselId - ID of the carousel container.
 * @param {number} direction - -1 for previous, 1 for next.
 */
function moveCarousel(carouselId, direction) {
    try {
        const carousel = document.getElementById(carouselId);
        if (!carousel) {
            throw new Error(`Carousel with ID '${carouselId}' not found`);
        }

        const items = carousel.querySelectorAll('.carousel-item');
        if (items.length === 0) return;

        let activeIndex = Array.from(items).findIndex(item => 
            item.classList.contains('active')
        );

        if (activeIndex === -1) activeIndex = 0;

        items[activeIndex].classList.remove('active');

        let newIndex = activeIndex + direction;
        if (newIndex < 0) newIndex = items.length - 1;
        if (newIndex >= items.length) newIndex = 0;

        items[newIndex].classList.add('active');

    } catch (error) {
        console.error('Error moving carousel:', error.message);
    }
}

// Example usage with sample data:
/*
const sampleProducts = [
    {
        name: "Modern Chair",
        category: "chairs",
        price: 199.99,
        description: "Elegant modern chair with leather upholstery.",
        imageUrl: "images/chair1.jpg"
    },
    {
        name: "Dining Table",
        category: "tables",
        price: 599.99,
        description: "Solid wood dining table for 6 people.",
        imageUrl: "images/table1.jpg"
    },
    // More products...
];

// Initialize with chairs
filterAndDisplayProducts(sampleProducts, "chairs", "products-carousel");
*/
```
