"""
Generated Code Metadata:
========================
Original URL: https://ppds5g468a68.blogspot.com
Prompt: Design a simple search function in JavaScript that can be integrated into a Blogger site.
Generated: DETERMINISTIC_6cb1898fc114333a
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple search function for a Blogger site.
 * This function searches for posts based on a query string and displays matching results.
 * 
 * Assumptions:
 * - Posts are stored in an array of objects, each containing `title` and `content` properties.
 * - The function is designed to be integrated into a Blogger site with minimal setup.
 */

// Sample data: Replace this with actual data from your Blogger site
const posts = [
  { title: "How to Learn JavaScript", content: "JavaScript is a versatile programming language..." },
  { title: "10 Tips for Blogging", content: "Blogging is a great way to share your thoughts..." },
  { title: "Understanding CSS", content: "CSS is used to style web pages..." },
  { title: "JavaScript Array Methods", content: "Arrays in JavaScript come with many useful methods..." },
];

/**
 * Search function to find posts matching the query.
 * @param {string} query - The search term entered by the user.
 * @returns {Array} - An array of matching posts.
 */
function searchPosts(query) {
  try {
    // Validate input
    if (typeof query !== "string" || query.trim() === "") {
      throw new Error("Invalid search query. Please enter a valid string.");
    }

    // Normalize query for case-insensitive search
    const normalizedQuery = query.toLowerCase();

    // Filter posts based on the query
    const results = posts.filter(post => 
      post.title.toLowerCase().includes(normalizedQuery) || 
      post.content.toLowerCase().includes(normalizedQuery)
    );

    return results;
  } catch (error) {
    console.error("Error during search:", error.message);
    return [];
  }
}

/**
 * Function to display search results on the Blogger site.
 * @param {Array} results - Array of matching posts.
 */
function displayResults(results) {
  // Get the results container element (replace with actual Blogger element ID or class)
  const resultsContainer = document.getElementById("search-results");

  // Clear previous results
  resultsContainer.innerHTML = "";

  if (results.length === 0) {
    resultsContainer.innerHTML = "<p>No results found.</p>";
    return;
  }

  // Generate HTML for each result
  results.forEach(post => {
    const postElement = document.createElement("div");
    postElement.className = "search-result";
    postElement.innerHTML = `
      <h3>${post.title}</h3>
      <p>${post.content.substring(0, 100)}...</p>
    `;
    resultsContainer.appendChild(postElement);
  });
}

/**
 * Event listener for the search form submission.
 * This function integrates the search functionality with the Blogger site.
 */
document.getElementById("search-form").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form from submitting normally

  // Get the search query from the input field
  const query = document.getElementById("search-input").value;

  // Perform the search
  const results = searchPosts(query);

  // Display the results
  displayResults(results);
});
```

### HTML Example for Integration:
```html
<!-- Search Form -->
<form id="search-form">
  <input type="text" id="search-input" placeholder="Search posts..." />
  <button type="submit">Search</button>
</form>

<!-- Search Results Container -->
<div id="search-results"></div>
```

### Notes:
- Replace `posts` with actual data from your Blogger site (e.g., fetched via an API).
- Ensure the `search-form` and `search-results` IDs match the elements in your Blogger site's HTML.
