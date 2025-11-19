"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Develop a JavaScript function to create a dynamic product lineup like Karnataka Aromas' "Hot.New.Arrivals" section.
Generated: DETERMINISTIC_4912343d0b57b148
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Creates a dynamic product lineup similar to Karnataka Aromas' "Hot.New.Arrivals" section.
 * @param {Object} options - Configuration options for the product lineup
 * @param {Array} options.products - Array of product objects
 * @param {string} options.containerId - ID of the DOM element to render the lineup
 * @param {number} [options.itemsPerSlide=4] - Number of items to display per slide
 * @param {number} [options.autoSlideInterval=5000] - Auto-slide interval in milliseconds (0 to disable)
 * @throws {Error} If required parameters are missing or invalid
 */
function createProductLineup(options) {
    // Validate input parameters
    if (!options || !options.products || !Array.isArray(options.products) || !options.containerId) {
        throw new Error('Invalid options: products array and containerId are required');
    }

    const {
        products,
        containerId,
        itemsPerSlide = 4,
        autoSlideInterval = 5000
    } = options;

    const container = document.getElementById(containerId);
    if (!container) {
        throw new Error(`Container element with ID '${containerId}' not found`);
    }

    // Calculate number of slides needed
    const totalSlides = Math.ceil(products.length / itemsPerSlide);
    if (totalSlides === 0) {
        container.innerHTML = '<p>No products available</p>';
        return;
    }

    // Generate HTML for the product lineup
    let html = `
        <div class="product-lineup">
            <div class="product-slides-container">
                ${generateSlidesHtml(products, itemsPerSlide, totalSlides)}
            </div>
            <div class="product-lineup-controls">
                <button class="prev-btn" aria-label="Previous products">❮</button>
                <div class="slide-indicators"></div>
                <button class="next-btn" aria-label="Next products">❯</button>
            </div>
        </div>
    `;

    container.innerHTML = html;

    // Initialize carousel functionality
    const slidesContainer = container.querySelector('.product-slides-container');
    const slides = container.querySelectorAll('.product-slide');
    const prevBtn = container.querySelector('.prev-btn');
    const nextBtn = container.querySelector('.next-btn');
    const indicatorsContainer = container.querySelector('.slide-indicators');

    let currentSlide = 0;
    let slideInterval;

    // Create slide indicators
    slides.forEach((_, index) => {
        const indicator = document.createElement('button');
        indicator.setAttribute('aria-label', `Go to slide ${index + 1}`);
        indicator.classList.add('slide-indicator');
        if (index === 0) indicator.classList.add('active');
        indicator.addEventListener('click', () => goToSlide(index));
        indicatorsContainer.appendChild(indicator);
    });

    // Set up event listeners
    prevBtn.addEventListener('click', () => navigate(-1));
    nextBtn.addEventListener('click', () => navigate(1));

    // Auto-slide functionality
    if (autoSlideInterval > 0) {
        startAutoSlide();
        container.addEventListener('mouseenter', pauseAutoSlide);
        container.addEventListener('mouseleave', startAutoSlide);
    }

    // Update slide position
    updateSlidePosition();

    /**
     * Generates HTML for product slides
     * @param {Array} products - Array of product objects
     * @param {number} itemsPerSlide - Items to display per slide
     * @param {number} totalSlides - Total number of slides
     * @returns {string} HTML string for slides
     */
    function generateSlidesHtml(products, itemsPerSlide, totalSlides) {
        let slidesHtml = '';
        
        for (let i = 0; i < totalSlides; i++) {
            const startIdx = i * itemsPerSlide;
            const endIdx = startIdx + itemsPerSlide;
            const slideProducts = products.slice(startIdx, endIdx);
            
            slidesHtml += `
                <div class="product-slide" data-slide-index="${i}">
                    ${slideProducts.map(product => generateProductCardHtml(product)).join('')}
                </div>
            `;
        }
        
        return slidesHtml;
    }

    /**
     * Generates HTML for a single product card
     * @param {Object} product - Product object
     * @returns {string} HTML string for product card
     */
    function generateProductCardHtml(product) {
        return `
            <div class="product-card">
                <div class="product-badge">${product.badge || 'New'}</div>
                <img src="${product.imageUrl || 'placeholder.jpg'}" alt="${product.name}" class="product-image">
                <h3 class="product-name">${product.name}</h3>
                <p class="product-price">${product.price || 'N/A'}</p>
                <button class="add-to-cart-btn">Add to Cart</button>
            </div>
        `;
    }

    /**
     * Navigates between slides
     * @param {number} direction - 1 for next, -1 for previous
     */
    function navigate(direction) {
        currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
        updateSlidePosition();
        resetAutoSlide();
    }

    /**
     * Goes to specific slide
     * @param {number} slideIndex - Index of slide to navigate to
     */
    function goToSlide(slideIndex) {
        if (slideIndex >= 0 && slideIndex < totalSlides) {
            currentSlide = slideIndex;
            updateSlidePosition();
            resetAutoSlide();
        }
    }

    /**
     * Updates slide position and active indicators
     */
    function updateSlidePosition() {
        const slideWidth = 100 / totalSlides;
        slidesContainer.style.transform = `translateX(-${currentSlide * slideWidth}%)`;
        
        // Update active indicator
        const indicators = container.querySelectorAll('.slide-indicator');
        indicators.forEach((indicator, index) => {
            indicator.classList.toggle('active', index === currentSlide);
        });
    }

    /**
     * Starts auto-slide functionality
     */
    function startAutoSlide() {
        if (autoSlideInterval > 0) {
            slideInterval = setInterval(() => navigate(1), autoSlideInterval);
        }
    }

    /**
     * Pauses auto-slide functionality
     */
    function pauseAutoSlide() {
        clearInterval(slideInterval);
    }

    /**
     * Resets auto-slide timer
     */
    function resetAutoSlide() {
        pauseAutoSlide();
        startAutoSlide();
    }
}

// Example usage:
/*
const products = [
    { name: 'Sandalwood Oil', price: '$24.99', imageUrl: 'sandalwood.jpg', badge: 'Best Seller' },
    { name: 'Rose Absolute', price: '$19.99', imageUrl: 'rose.jpg' },
    { name: 'Jasmine Oil', price: '$22.99', imageUrl: 'jasmine.jpg', badge: 'Popular' },
    { name: 'Patchouli Oil', price: '$17.99', imageUrl: 'patchouli.jpg' },
    { name: 'Lavender Oil', price: '$15.99', imageUrl: 'lavender.jpg' },
    { name: 'Vanilla Extract', price: '$21.99', imageUrl: 'vanilla.jpg' },
    { name: 'Bergamot Oil', price: '$18.99', imageUrl: 'bergamot.jpg' },
    { name: 'Ylang Ylang Oil', price: '$20.99', imageUrl: 'ylang-ylang.jpg' }
];

createProductLineup({
    products: products,
    containerId: 'product-lineup-container',
    itemsPerSlide: 4,
    autoSlideInterval: 3000
});
*/
```
