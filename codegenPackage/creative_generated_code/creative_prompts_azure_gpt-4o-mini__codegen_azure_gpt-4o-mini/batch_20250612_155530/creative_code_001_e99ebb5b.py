"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thelittlelineco.com
Prompt: Write a function in JavaScript that retrieves product details from a Shopify store's catalog, specifically for items priced at $19.99.
Generated: DETERMINISTIC_e99ebb5bf7533843
Batch ID: 20250612_155530
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-store.myshopify.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://": {
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
 * Fetches product details from a Shopify store's catalog for items priced at $19.99.
 * 
 * @param {string} shopUrl - The base URL of the Shopify store (e.g., 'https://your-store.myshopify.com').
 * @returns {Promise<Array>} - A promise that resolves to an array of product details.
 * @throws {Error} - Throws an error if the request fails or if invalid parameters are provided.
 */
async function fetchProductsAtPrice(shopUrl) {
    // Validate the input URL
    if (typeof shopUrl !== 'string' || !shopUrl.startsWith('https://')) {
        throw new Error('Invalid Shopify store URL provided.');
    }

    const endpoint = `${shopUrl}/admin/api/2023-10/products.json`; // Shopify API endpoint
    const priceToFind = 19.99; // Price to filter products

    try {
        // Fetch products from the Shopify store
        const response = await fetch(endpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-Shopify-Access-Token': 'your-access-token' // Replace with your actual access token
            }
        });

        // Check for successful response
        if (!response.ok) {
            throw new Error(`Error fetching products: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        
        // Filter products priced at $19.99 and return relevant details
        const filteredProducts = data.products.filter(product => {
            return product.variants.some(variant => variant.price === priceToFind.toString());
        }).map(product => ({
            id: product.id,
            title: product.title,
            price: priceToFind,
            image: product.images[0] ? product.images[0].src : null,
            url: `${shopUrl}/products/${product.handle}`
        }));

        return filteredProducts;

    } catch (error) {
        // Handle any errors that occur during the fetch or processing
        console.error('Error fetching products:', error);
        throw new Error('Failed to retrieve product details from Shopify store.');
    }
}

// Example usage (uncomment to use):
// fetchProductsAtPrice('https://your-store.myshopify.com')
//     .then(products => console.log(products))
//     .catch(error => console.error(error));
```
