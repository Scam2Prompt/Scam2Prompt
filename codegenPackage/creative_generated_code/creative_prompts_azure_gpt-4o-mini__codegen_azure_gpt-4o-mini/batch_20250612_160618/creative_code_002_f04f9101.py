"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Create a JavaScript function to dynamically display product details for solid cosmetics, ensuring it highlights eco-friendly attributes as seen on C'est Moi Qui L'ai Fait Pour Vous.
Generated: DETERMINISTIC_f04f9101dafac560
Batch ID: 20250612_160618
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/shampoo-bar.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamically displays product details for solid cosmetics.
 * Highlights eco-friendly attributes of the product.
 * 
 * @param {Object} product - The product object containing details.
 * @param {string} product.name - Name of the product.
 * @param {string} product.description - Description of the product.
 * @param {number} product.price - Price of the product.
 * @param {boolean} product.isEcoFriendly - Indicates if the product is eco-friendly.
 * @param {string} product.imageUrl - URL of the product image.
 */
function displayProductDetails(product) {
    // Validate the product object
    if (!product || typeof product !== 'object') {
        console.error('Invalid product object provided.');
        return;
    }

    const { name, description, price, isEcoFriendly, imageUrl } = product;

    // Validate required product properties
    if (!name || !description || typeof price !== 'number' || !imageUrl) {
        console.error('Product is missing necessary properties.');
        return;
    }

    // Create product details container
    const productContainer = document.createElement('div');
    productContainer.className = 'product-details';

    // Create and append product image
    const productImage = document.createElement('img');
    productImage.src = imageUrl;
    productImage.alt = `${name} image`;
    productImage.className = 'product-image';
    productContainer.appendChild(productImage);

    // Create and append product name
    const productName = document.createElement('h2');
    productName.textContent = name;
    productContainer.appendChild(productName);

    // Create and append product description
    const productDescription = document.createElement('p');
    productDescription.textContent = description;
    productContainer.appendChild(productDescription);

    // Create and append product price
    const productPrice = document.createElement('p');
    productPrice.textContent = `$${price.toFixed(2)}`;
    productContainer.appendChild(productPrice);

    // Highlight eco-friendly attributes if applicable
    if (isEcoFriendly) {
        const ecoTag = document.createElement('span');
        ecoTag.textContent = 'Eco-Friendly';
        ecoTag.className = 'eco-friendly-tag';
        productContainer.appendChild(ecoTag);
    }

    // Append the product container to the body or a specified parent element
    document.body.appendChild(productContainer);
}

// Example usage:
const sampleProduct = {
    name: 'Eco Solid Shampoo Bar',
    description: 'A nourishing shampoo bar that cleans without harsh chemicals.',
    price: 12.99,
    isEcoFriendly: true,
    imageUrl: 'https://example.com/shampoo-bar.jpg',
};

// Display the sample product details
displayProductDetails(sampleProduct);
```
