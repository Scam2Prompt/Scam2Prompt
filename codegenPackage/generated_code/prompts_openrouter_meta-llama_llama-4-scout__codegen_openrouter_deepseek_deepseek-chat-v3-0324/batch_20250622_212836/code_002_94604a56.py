"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: "Generate a JavaScript function to display product promotions, like discounts on tinta spray verniz and luvas de segurança, on an e-commerce website."
Generated: DETERMINISTIC_94604a5614936f24
Batch ID: 20250622_212836
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/luvas-seguranca.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/tinta-spray.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays product promotions on an e-commerce website.
 * @param {Array} promotions - Array of promotion objects containing product details.
 * @param {HTMLElement} container - DOM element where promotions will be rendered.
 * @throws {Error} If promotions is not an array or container is not a valid DOM element.
 */
function displayProductPromotions(promotions, container) {
    // Validate inputs
    if (!Array.isArray(promotions)) {
        throw new Error('Promotions must be an array');
    }
    if (!(container instanceof HTMLElement)) {
        throw new Error('Container must be a valid DOM element');
    }

    try {
        // Clear previous promotions
        container.innerHTML = '';

        // Create promotion cards for each product
        promotions.forEach(promotion => {
            const promotionCard = document.createElement('div');
            promotionCard.className = 'promotion-card';

            // Validate required promotion fields
            if (!promotion.name || !promotion.discount || !promotion.originalPrice) {
                console.warn('Invalid promotion data:', promotion);
                return;
            }

            const discountPercentage = Math.round((promotion.discount / promotion.originalPrice) * 100);
            const finalPrice = promotion.originalPrice - promotion.discount;

            promotionCard.innerHTML = `
                <h3 class="product-name">${promotion.name}</h3>
                <div class="price-container">
                    <span class="original-price">$${promotion.originalPrice.toFixed(2)}</span>
                    <span class="discount">-${discountPercentage}%</span>
                </div>
                <div class="final-price">$${finalPrice.toFixed(2)}</div>
                ${promotion.imageUrl ? `<img src="${promotion.imageUrl}" alt="${promotion.name}" class="product-image">` : ''}
                <button class="shop-now-btn">Shop Now</button>
            `;

            container.appendChild(promotionCard);
        });

    } catch (error) {
        console.error('Error displaying promotions:', error);
        container.innerHTML = '<p class="error-message">Unable to load promotions. Please try again later.</p>';
    }
}

// Example usage:
/*
const promotions = [
    {
        name: 'Tinta Spray Verniz',
        originalPrice: 25.99,
        discount: 5.00,
        imageUrl: 'https://example.com/tinta-spray.jpg'
    },
    {
        name: 'Luvas de Segurança',
        originalPrice: 12.50,
        discount: 2.50,
        imageUrl: 'https://example.com/luvas-seguranca.jpg'
    }
];

const promotionsContainer = document.getElementById('promotions-container');
displayProductPromotions(promotions, promotionsContainer);
*/
```
