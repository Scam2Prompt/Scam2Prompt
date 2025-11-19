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
 * Simple Search Function for Blogger Site
 * This function allows users to search for blog posts by title or content.
 * It filters the posts based on the search query and displays the results.
 */

// Sample blog posts data (this would typically come from your Blogger API)
const blogPosts = [
    { title: "JavaScript Basics", content: "Learn the fundamentals of JavaScript." },
    { title: "Advanced JavaScript", content: "Deep dive into JavaScript concepts." },
    { title: "CSS for Beginners", content: "Introduction to CSS styling." },
    { title: "HTML Overview", content: "Understanding the structure of web pages." },
];

/**
 * Searches blog posts based on the provided query.
 * @param {string} query - The search term entered by the user.
 * @returns {Array} - An array of matching blog posts.
 */
function searchPosts(query) {
    // Validate the input
    if (typeof query !== 'string') {
        console.error("Invalid input: query must be a string.");
        return [];
    }

    // Normalize the query to lowercase for case-insensitive search
    const normalizedQuery = query.toLowerCase();

    // Filter posts that include the query in the title or content
    const results = blogPosts.filter(post => 
        post.title.toLowerCase().includes(normalizedQuery) || 
        post.content.toLowerCase().includes(normalizedQuery)
    );

    return results;
}

/**
 * Displays the search results on the page.
 * @param {Array} results - The array of matching blog posts.
 */
function displayResults(results) {
    const resultsContainer = document.getElementById('search-results');
    resultsContainer.innerHTML = ''; // Clear previous results

    if (results.length === 0) {
        resultsContainer.innerHTML = '<p>No results found.</p>';
        return;
    }

    // Create and append result elements
    results.forEach(post => {
        const postElement = document.createElement('div');
        postElement.className = 'post';
        postElement.innerHTML = `<h3>${post.title}</h3><p>${post.content}</p>`;
        resultsContainer.appendChild(postElement);
    });
}

/**
 * Handles the search action when the user submits the search form.
 * @param {Event} event - The event triggered by the form submission.
 */
function handleSearch(event) {
    event.preventDefault(); // Prevent the default form submission

    const queryInput = document.getElementById('search-query');
    const query = queryInput.value.trim(); // Get and trim the input value

    // Perform the search and display results
    const results = searchPosts(query);
    displayResults(results);
}

// Event listener for the search form submission
document.getElementById('search-form').addEventListener('submit', handleSearch);
```

```html
<!-- HTML Structure for Search Functionality -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blogger Search</title>
    <style>
        /* Basic styles for search results */
        #search-results {
            margin-top: 20px;
        }
        .post {
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>Search Blog Posts</h1>
    <form id="search-form">
        <input type="text" id="search-query" placeholder="Enter search term" required>
        <button type="submit">Search</button>
    </form>
    <div id="search-results"></div>

    <script src="path/to/your/search-function.js"></script>
</body>
</html>
```
