"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Write a JavaScript function that retrieves product details from Navkar Furniture's API and displays them on a webpage.
Generated: DETERMINISTIC_2053d673533e341e
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.navkarfurniture.com/products": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.navkarfurniture.com/products`": {
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
 * Function to fetch and display product details from Navkar Furniture's API
 * Assumes the webpage contains a div with the id 'product-container' to display products
 */
async function fetchAndDisplayProductDetails() {
  // URL of Navkar Furniture's API endpoint
  const apiUrl = 'https://api.navkarfurniture.com/products';
  
  try {
    // Fetch product data from the API
    const response = await fetch(apiUrl);

    // Check if the response is okay (status code 200-299)
    if (!response.ok) {
      throw new Error(`Error fetching product details: ${response.status} ${response.statusText}`);
    }

    // Parse the JSON response
    const products = await response.json();

    // Get the container element in the DOM
    const productContainer = document.getElementById('product-container');
    if (!productContainer) {
      throw new Error('Product container element not found in the DOM.');
    }

    // Clear existing content in the container
    productContainer.innerHTML = '';

    // Display each product in the container
    products.forEach(product => {
      // Create a div element for each product
      const productDiv = document.createElement('div');
      productDiv.classList.add('product-item');

      // Populate the product details
      productDiv.innerHTML = `
        <h2>${product.name}</h2>
        <p>Price: $${product.price.toFixed(2)}</p>
        <p>Description: ${product.description}</p>
        <img src="${product.image}" alt="${product.name}" style="max-width: 200px;">
      `;

      // Append the product div to the container
      productContainer.appendChild(productDiv);
    });

  } catch (error) {
    // Handle errors
    console.error('An error occurred:', error);
    alert('Unable to fetch product details. Please try again later.');
  }
}

// Call the function to fetch and display product details
// This can be triggered by a user action or on page load
fetchAndDisplayProductDetails();
```

**Note:** Ensure that:
1. The API URL `https://api.navkarfurniture.com/products` exists and is reachable.
2. The HTML file contains a `<div id="product-container"></div>` where the product details will be displayed.
