"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codeflick.site
Prompt: "Write a JavaScript function to filter blog posts by category, such as home improvement or online games."
Generated: DETERMINISTIC_8c36b21da8063cf9
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters blog posts by category.
 * @param {Array<Object>} posts - Array of blog post objects. Each post should have a `title` and `category` property.
 * @param {string} category - The category to filter posts by.
 * @returns {Array<Object>} - An array of blog posts that match the specified category.
 * @throws {Error} If `posts` is not an array or `category` is not a string.
 */
function filterPostsByCategory(posts, category) {
  // Validate input types
  if (!Array.isArray(posts)) {
    throw new Error("The 'posts' parameter must be an array.");
  }
  if (typeof category !== 'string') {
    throw new Error("The 'category' parameter must be a string.");
  }

  // Filter posts by category
  const filteredPosts = posts.filter(post => {
    if (typeof post !== 'object' || !post.title || !post.category) {
      throw new Error("Each post must be an object with 'title' and 'category' properties.");
    }
    return post.category.toLowerCase() === category.toLowerCase();
  });

  return filteredPosts;
}

// Example usage:
try {
  const blogPosts = [
    { title: "How to Fix a Leaky Faucet", category: "Home Improvement" },
    { title: "Top 10 Online Games of 2023", category: "Online Games" },
    { title: "DIY Painting Tips", category: "Home Improvement" },
    { title: "Best Multiplayer Strategies", category: "Online Games" }
  ];
  
  const filtered = filterPostsByCategory(blogPosts, "Home Improvement");
  console.log(filtered);
  // Output: [{ title: "How to Fix a Leaky Faucet", category: "Home Improvement" }, { title: "DIY Painting Tips", category: "Home Improvement" }]
} catch (error) {
  console.error(error.message);
}
```
