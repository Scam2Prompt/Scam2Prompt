"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooledether.io
Prompt: Provide a code example in JavaScript to list all blog posts from a Blogger account using the Blogger API, including pagination handling.
Generated: DETERMINISTIC_523eacd0e0344fd8
Batch ID: 20250612_150435
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/blogger/v3/blogs/${blogId}/posts`;": {
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
// Import the necessary Node.js package for making HTTP requests
import fetch from 'node-fetch'; // Ensure you have `node-fetch` installed via npm

/**
 * Fetches all blog posts from a Blogger account using the Blogger API, with pagination handling.
 * @param {string} blogId - The unique ID of the Blogger blog.
 * @param {string} apiKey - Your API key for accessing the Blogger API.
 * @returns {Promise<Array>} - A promise that resolves to an array of all blog posts.
 */
async function fetchAllBlogPosts(blogId, apiKey) {
  const baseUrl = `https://www.googleapis.com/blogger/v3/blogs/${blogId}/posts`;
  let allPosts = [];
  let nextPageToken = null;

  try {
    do {
      // Construct the URL for the current page, including pagination token if available
      const url = `${baseUrl}?key=${apiKey}${nextPageToken ? `&pageToken=${nextPageToken}` : ''}`;

      // Make an HTTP GET request to the Blogger API
      const response = await fetch(url);

      // Check if the response is successful
      if (!response.ok) {
        throw new Error(`Failed to fetch blog posts: ${response.statusText}`);
      }

      // Parse the JSON response
      const data = await response.json();

      // Append the current page of posts to the allPosts array
      allPosts = allPosts.concat(data.items || []);

      // Update the nextPageToken for the next iteration
      nextPageToken = data.nextPageToken || null;

    } while (nextPageToken); // Continue while there are more pages to fetch

    return allPosts; // Return the complete list of posts
  } catch (error) {
    console.error('Error fetching blog posts:', error.message);
    throw error; // Rethrow the error for the caller to handle
  }
}

// Example usage
(async () => {
  const blogId = 'YOUR_BLOG_ID'; // Replace with the Blogger blog ID
  const apiKey = 'YOUR_API_KEY'; // Replace with your Google API key

  try {
    const posts = await fetchAllBlogPosts(blogId, apiKey);
    console.log('Fetched blog posts:', posts);
  } catch (error) {
    console.error('Failed to retrieve blog posts:', error.message);
  }
})();
```

**Notes:**
1. Replace `YOUR_BLOG_ID` and `YOUR_API_KEY` with your actual Blogger blog ID and Google API key.
2. Install the `node-fetch` package by running `npm install node-fetch` if it's not already available in your environment.
3. This script follows best practices, including error handling, pagination, and modular design, making it production-ready.
