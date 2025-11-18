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
// Infinite scrolling implementation for WooCommerce product pages in the WoodMart theme

document.addEventListener("DOMContentLoaded", () => {
  // Selector for the product grid container
  const productGrid = document.querySelector(".products-grid");
  if (!productGrid) {
    console.error("Product grid not found. Ensure the selector matches your theme structure.");
    return;
  }

  // Selector for the pagination links container
  const paginationContainer = document.querySelector(".woocommerce-pagination");
  if (!paginationContainer) {
    console.error("Pagination container not found. Ensure the selector matches your theme structure.");
    return;
  }

  // Observe scroll events
  window.addEventListener("scroll", handleInfiniteScroll);

  let isLoading = false; // Prevent multiple simultaneous loading calls

  /**
   * Handle infinite scrolling logic
   */
  function handleInfiniteScroll() {
    const pagination = paginationContainer.querySelector("a.next"); // Find the "next page" link
    if (!pagination) {
      // No more pages to load
      window.removeEventListener("scroll", handleInfiniteScroll);
      console.log("No more pages to load.");
      return;
    }

    // Check if the user has scrolled near the bottom of the page
    const { scrollTop, clientHeight, scrollHeight } = document.documentElement;
    const threshold = 200; // Load content if user is within 200px of the bottom
    if (scrollHeight - scrollTop - clientHeight <= threshold && !isLoading) {
      loadNextPage(pagination.href);
    }
  }

  /**
   * Load the next page's products and append them to the grid
   * @param {string} url - The URL of the next page
   */
  async function loadNextPage(url) {
    try {
      isLoading = true;
      paginationContainer.style.display = "none"; // Hide the pagination during loading

      console.log(`Loading products from: ${url}`);
      const response = await fetch(url);

      if (!response.ok) {
        throw new Error(`Failed to fetch products from ${url}. Status: ${response.status}`);
      }

      const text = await response.text();
      const parser = new DOMParser();
      const doc = parser.parseFromString(text, "text/html");
      const newProducts = doc.querySelector(".products-grid").children; // Select new products
      const nextPagination = doc.querySelector(".woocommerce-pagination a.next"); // Find next pagination link

      // Append new products to the existing product grid
      Array.from(newProducts).forEach((product) => productGrid.appendChild(product));

      // Update pagination link if available
      if (nextPagination) {
        paginationContainer.querySelector("a.next").href = nextPagination.href;
      } else {
        paginationContainer.style.display = "none"; // Hide pagination permanently if no more pages
      }

      console.log("Products loaded successfully.");
    } catch (error) {
      console.error("Error loading products:", error);
    } finally {
      isLoading = false;
    }
  }
});
```
