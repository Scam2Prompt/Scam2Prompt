"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashusdtgenerator.com
Prompt: "Write JavaScript to enable infinite scrolling for WooCommerce product pages, referencing the WoodMart theme's demo features."
Generated: DETERMINISTIC_5a5aea632a1c5bec
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Infinite Scroll for WooCommerce Product Pages using WoodMart Theme Features

// Ensure the DOM is fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function () {
    // Configuration for infinite scrolling
    const scrollThreshold = 300; // Scroll threshold in pixels before loading more products
    let isLoading = false; // Flag to prevent multiple simultaneous requests
    let page = 2; // Initial page number to load products from

    // Function to load more products
    const loadMoreProducts = () => {
        // Prevent further loading if already in progress
        if (isLoading) return;

        isLoading = true; // Set loading flag to true

        // Fetch the WooCommerce products through an AJAX request
        fetch(`/page/${page}/?ajax=true`) // Adjust the URL as necessary for your WooCommerce setup
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text(); // Parse response as text
            })
            .then(html => {
                // Append new products to the existing product list
                const productContainer = document.querySelector('.products'); // Adjust selector as necessary
                productContainer.insertAdjacentHTML('beforeend', html);

                // Increment the page number for the next load
                page++;
                isLoading = false; // Reset loading flag
            })
            .catch(error => {
                console.error('Error loading more products:', error);
                isLoading = false; // Reset loading flag on error
            });
    };

    // Event listener for scroll events
    window.addEventListener('scroll', () => {
        // Check if user has scrolled near the bottom of the page
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - scrollThreshold) {
            loadMoreProducts(); // Load more products
        }
    });
});
```
