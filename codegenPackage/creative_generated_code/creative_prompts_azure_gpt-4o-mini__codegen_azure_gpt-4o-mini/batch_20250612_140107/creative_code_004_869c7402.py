"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interline-asia.com
Prompt: Develop a JavaScript function to display recent posts dynamically on a philosophy blog powered by WordPress.
Generated: DETERMINISTIC_869c74020eb13f10
Batch ID: 20250612_140107
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://yourphilosophyblog.com": {
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
 * Fetches recent posts from a WordPress site and displays them dynamically.
 * @param {string} apiUrl - The URL of the WordPress REST API endpoint for posts.
 * @param {HTMLElement} container - The DOM element where posts will be rendered.
 * @param {number} postCount - The number of recent posts to fetch.
 */
async function displayRecentPosts(apiUrl, container, postCount = 5) {
    try {
        // Construct the API endpoint URL with the specified post count
        const url = `${apiUrl}/wp-json/wp/v2/posts?per_page=${postCount}`;
        
        // Fetch recent posts from the WordPress REST API
        const response = await fetch(url);

        // Check if the response is ok (status code in the range 200-299)
        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.statusText}`);
        }

        // Parse the JSON response
        const posts = await response.json();

        // Clear the container before rendering new posts
        container.innerHTML = '';

        // Loop through the posts and render them
        posts.forEach(post => {
            // Create a new article element for each post
            const article = document.createElement('article');
            article.classList.add('post');

            // Create and append the post title
            const title = document.createElement('h2');
            title.innerHTML = `<a href="${post.link}" target="_blank">${post.title.rendered}</a>`;
            article.appendChild(title);

            // Create and append the post excerpt
            const excerpt = document.createElement('div');
            excerpt.innerHTML = post.excerpt.rendered;
            article.appendChild(excerpt);

            // Append the article to the container
            container.appendChild(article);
        });

    } catch (error) {
        // Log any errors to the console
        console.error('Error fetching recent posts:', error);
        // Optionally, display an error message to the user
        container.innerHTML = '<p>Failed to load recent posts. Please try again later.</p>';
    }
}

// Example usage:
// Assuming you have a <div id="recent-posts"></div> in your HTML
const container = document.getElementById('recent-posts');
const apiUrl = 'https://yourphilosophyblog.com'; // Replace with your WordPress site URL
displayRecentPosts(apiUrl, container);
```
