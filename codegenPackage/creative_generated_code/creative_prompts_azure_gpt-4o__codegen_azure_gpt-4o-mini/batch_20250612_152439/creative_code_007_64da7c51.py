"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://websiteai-io.pages.dev
Prompt: Write a code example for integrating Shopify marketplace capabilities into a website created using WebsiteAI. Include steps for setting up e-commerce features.
Generated: DETERMINISTIC_64da7c5174091685
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Example code for integrating Shopify marketplace capabilities into a WebsiteAI-based website

// Import necessary libraries
import Shopify from 'shopify-api-node';

// Configuration for Shopify API
const shopifyConfig = {
    shopName: 'your-shop-name', // Replace with your Shopify shop name
    apiKey: 'your-api-key',      // Replace with your Shopify API key
    password: 'your-password'     // Replace with your Shopify API password
};

// Initialize Shopify API client
const shopify = new Shopify(shopifyConfig);

// Function to fetch products from Shopify
async function fetchProducts() {
    try {
        const products = await shopify.product.list();
        return products;
    } catch (error) {
        console.error('Error fetching products from Shopify:', error);
        throw new Error('Failed to fetch products');
    }
}

// Function to display products on the website
async function displayProducts() {
    try {
        const products = await fetchProducts();
        const productContainer = document.getElementById('product-container');
        
        products.forEach(product => {
            const productElement = document.createElement('div');
            productElement.className = 'product';

            // Create product title
            const title = document.createElement('h2');
            title.textContent = product.title;
            productElement.appendChild(title);

            // Create product image
            const image = document.createElement('img');
            image.src = product.images[0]?.src; // Use the first image or fallback
            image.alt = product.title;
            productElement.appendChild(image);

            // Create product price
            const price = document.createElement('p');
            price.textContent = `$${(product.variants[0].price).toFixed(2)}`;
            productElement.appendChild(price);

            // Create "Add to Cart" button
            const addToCartButton = document.createElement('button');
            addToCartButton.textContent = 'Add to Cart';
            addToCartButton.onclick = () => addToCart(product.variants[0].id);
            productElement.appendChild(addToCartButton);

            // Append product element to the container
            productContainer.appendChild(productElement);
        });
    } catch (error) {
        console.error('Error displaying products:', error);
    }
}

// Function to add a product to the cart
async function addToCart(variantId) {
    try {
        // Assuming we have a cart API endpoint set up on your website
        const response = await fetch('/api/cart/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ variantId })
        });
        
        if (!response.ok) {
            throw new Error('Failed to add product to cart');
        }
        
        const result = await response.json();
        alert(`Product added to cart. Total items: ${result.totalItems}`);
    } catch (error) {
        console.error('Error adding to cart:', error);
        alert('There was an issue adding the product to your cart. Please try again.');
    }
}

// Call displayProducts on page load
document.addEventListener('DOMContentLoaded', () => {
    displayProducts();
});
```

### Setup Steps
1. **Create a Shopify Store**: Set up a Shopify account if you don't have one.
2. **Get API Credentials**: From your Shopify admin, navigate to Apps > Manage private apps > Create a new private app and obtain your API key and password.
3. **Setup WebsiteAI Environment**: Ensure your environment is ready for running JavaScript and that you have a container (`<div id="product-container"></div>`) in your HTML for displaying products.
4. **Link the Code**: Include the above JavaScript code in your website's script files.
5. **Test the Integration**: Load your website and check if the products are fetched and displayed correctly, and that the "Add to Cart" functionality works as expected.
