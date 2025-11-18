"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thesoftware.online
Prompt: Provide JavaScript code to enhance the search functionality on a WordPress site, enabling real-time post previews as users type, similar to the search feature described in a WooCommerce-based site.
Generated: DETERMINISTIC_7641639f861beb74
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Real-time WordPress search functionality with post previews.
 * This script uses WordPress's REST API to fetch posts dynamically based on user input.
 * Add this code to your WordPress theme or as part of a custom plugin.
 */

// Ensure the DOM is loaded before executing the script
document.addEventListener("DOMContentLoaded", function () {
    // Create a debounce function to limit API calls
    function debounce(func, delay) {
        let timer;
        return function (...args) {
            clearTimeout(timer);
            timer = setTimeout(() => {
                func.apply(this, args);
            }, delay);
        };
    }

    // DOM elements
    const searchInput = document.querySelector("#search-input"); // The search input field (add an ID to your input field)
    const resultsContainer = document.querySelector("#search-results"); // The container where results will be displayed (add an ID to your results container)

    if (!searchInput || !resultsContainer) {
        console.error("Search input or results container not found in DOM.");
        return;
    }

    // Function to fetch and display search results
    async function fetchSearchResults(query) {
        try {
            // Clear previous results
            resultsContainer.innerHTML = "";

            // If the query is empty, don't fetch results
            if (!query.trim()) {
                return;
            }

            // Make a request to the WordPress REST API
            const response = await fetch(`/wp-json/wp/v2/posts?search=${encodeURIComponent(query)}&_embed=true`);

            // Check for HTTP errors
            if (!response.ok) {
                console.error("Failed to fetch search results:", response.statusText);
                resultsContainer.innerHTML = `<p>Error fetching results. Please try again later.</p>`;
                return;
            }

            const posts = await response.json();

            // If no posts match the query, show a "No results" message
            if (posts.length === 0) {
                resultsContainer.innerHTML = `<p>No results found.</p>`;
                return;
            }

            // Display posts in the results container
            const fragment = document.createDocumentFragment();
            posts.forEach((post) => {
                const postElement = document.createElement("div");
                postElement.classList.add("search-result-item");

                // Post title with link
                const postTitle = document.createElement("a");
                postTitle.href = post.link;
                postTitle.textContent = post.title.rendered;
                postTitle.classList.add("search-result-title");

                // Post thumbnail (if available)
                const postThumbnail = document.createElement("img");
                const featuredMedia = post._embedded && post._embedded["wp:featuredmedia"] ? post._embedded["wp:featuredmedia"][0] : null;
                postThumbnail.src = featuredMedia ? featuredMedia.source_url : "";
                postThumbnail.alt = featuredMedia ? featuredMedia.alt_text : "Post thumbnail";
                postThumbnail.classList.add("search-result-thumbnail");

                // Append elements to the container
                if (featuredMedia) {
                    postElement.appendChild(postThumbnail);
                }
                postElement.appendChild(postTitle);

                fragment.appendChild(postElement);
            });

            resultsContainer.appendChild(fragment);
        } catch (error) {
            console.error("Error fetching or processing search results:", error);
            resultsContainer.innerHTML = `<p>Error fetching results. Please try again later.</p>`;
        }
    }

    // Attach the input event to the search field, with debouncing
    searchInput.addEventListener("input", debounce((event) => {
        const query = event.target.value;
        fetchSearchResults(query);
    }, 300)); // 300ms debounce delay
});
```

---

### Notes for Integration:
1. **HTML Structure:** Ensure your WordPress site has the following elements:
   - A search input field with the ID `search-input` (e.g., `<input type="text" id="search-input" />`).
   - A container for displaying results with the ID `search-results` (e.g., `<div id="search-results"></div>`).

2. **Styling:** Add CSS to style the results (`search-result-item`, `search-result-title`, and `search-result-thumbnail`) for a better user experience.

3. **REST API:** Verify that the WordPress REST API is enabled on the site. If disabled, enable it by default or use a plugin like "REST API Authentication."

4. **Browser Compatibility:** Test the code on multiple browsers to ensure proper functionality.
