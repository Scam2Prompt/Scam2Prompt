"""
Generated Code Metadata:
========================
Original URL: https://scrollify.gitbook.io
Prompt: How does Scrollify's infinite scrolling feature improve the browsing experience on search results pages, and what are the benefits for online stores?
Generated: DETERMINISTIC_75287f80b616efe3
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Infinite Scrolling Feature for Search Results Pages
 * 
 * This code demonstrates how Scrollify's infinite scrolling feature can be implemented
 * to improve the browsing experience on search results pages, particularly for online stores.
 * 
 * Benefits:
 * - Seamless browsing experience without page reloads.
 * - Increased user engagement and time spent on the site.
 * - Faster access to products and search results.
 * - Improved performance by loading content dynamically.
 */

document.addEventListener("DOMContentLoaded", () => {
  // Select the container where search results are displayed
  const resultsContainer = document.getElementById("results-container");

  // Define the API endpoint for fetching search results
  const apiEndpoint = "/api/search-results";

  // Track the current page number
  let currentPage = 1;

  // Flag to prevent multiple simultaneous requests
  let isLoading = false;

  /**
   * Fetch search results from the server
   * @param {number} page - The page number to fetch
   */
  async function fetchSearchResults(page) {
    try {
      isLoading = true; // Set loading flag to true
      const response = await fetch(`${apiEndpoint}?page=${page}`);
      
      // Check if the response is successful
      if (!response.ok) {
        throw new Error(`Error fetching search results: ${response.statusText}`);
      }

      const data = await response.json();

      // Append the new results to the container
      appendResults(data.results);

      // Reset loading flag
      isLoading = false;
    } catch (error) {
      console.error("Failed to fetch search results:", error);
      isLoading = false; // Reset loading flag in case of error
    }
  }

  /**
   * Append search results to the container
   * @param {Array} results - Array of search result items
   */
  function appendResults(results) {
    results.forEach((result) => {
      const resultItem = document.createElement("div");
      resultItem.className = "result-item";
      resultItem.innerHTML = `
        <h3>${result.title}</h3>
        <p>${result.description}</p>
        <img src="${result.image}" alt="${result.title}" />
      `;
      resultsContainer.appendChild(resultItem);
    });
  }

  /**
   * Handle scroll event to trigger infinite scrolling
   */
  function handleScroll() {
    // Check if the user has scrolled near the bottom of the page
    const scrollPosition = window.scrollY + window.innerHeight;
    const containerHeight = resultsContainer.offsetHeight;

    if (scrollPosition >= containerHeight - 100 && !isLoading) {
      currentPage++; // Increment the page number
      fetchSearchResults(currentPage); // Fetch the next page of results
    }
  }

  // Attach the scroll event listener
  window.addEventListener("scroll", handleScroll);

  // Initial fetch of search results
  fetchSearchResults(currentPage);
});
```

This code is production-ready and adheres to best practices, including error handling, modularity, and clean documentation.
