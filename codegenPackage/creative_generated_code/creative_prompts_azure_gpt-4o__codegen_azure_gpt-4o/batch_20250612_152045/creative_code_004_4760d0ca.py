"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Write a JavaScript function to optimize SEO meta-tags for a business website, using the SEO strategies outlined by MDA Tech Sys.
Generated: DETERMINISTIC_4760d0ca5aa60795
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to optimize SEO meta-tags for a business website.
 * Utilizes common SEO strategies such as keyword insertion, character limits,
 * and dynamic content generation.
 *
 * @param {Object} options - Configuration options for meta-tag optimization.
 * @param {string} options.title - The title of the webpage.
 * @param {string} options.description - A brief description of the webpage.
 * @param {Array<string>} options.keywords - Keywords relevant to the webpage.
 * @param {string} options.businessName - Name of the business.
 * @returns {Object} Meta-tags optimized for SEO.
 */
function optimizeMetaTags({ title, description, keywords, businessName }) {
  // Validate input parameters
  if (!title || typeof title !== 'string') {
    throw new Error("Title is required and must be a string.");
  }
  if (!description || typeof description !== 'string') {
    throw new Error("Description is required and must be a string.");
  }
  if (!Array.isArray(keywords) || keywords.length === 0) {
    throw new Error("Keywords must be a non-empty array of strings.");
  }
  if (!businessName || typeof businessName !== 'string') {
    throw new Error("Business name is required and must be a string.");
  }

  // Helper function to truncate text to a specific length
  const truncateText = (text, maxLength) => {
    return text.length > maxLength ? text.slice(0, maxLength - 3) + "..." : text;
  };

  // Generate optimized title (with character limit and keywords)
  const optimizedTitle = truncateText(
    `${title} | ${businessName} | ${keywords.slice(0, 2).join(", ")}`,
    60 // Recommended title character length for SEO
  );

  // Generate optimized description (with character limit and keywords)
  const optimizedDescription = truncateText(
    `${description} | ${businessName}. Keywords: ${keywords.join(", ")}`,
    160 // Recommended meta description character length for SEO
  );

  // Generate a comma-separated list of keywords
  const optimizedKeywords = keywords.join(", ");

  // Return the optimized meta-tags
  return {
    title: optimizedTitle,
    description: optimizedDescription,
    keywords: optimizedKeywords
  };
}

// Example usage:
try {
  const metaTags = optimizeMetaTags({
    title: "Best Coffee Shop in Town",
    description: "Enjoy the finest coffee brewed fresh every day.",
    keywords: ["coffee", "shop", "local business", "best coffee", "organic coffee"],
    businessName: "Barista Bliss"
  });

  console.log("Optimized Meta-Tags:", metaTags);
} catch (error) {
  console.error("Error optimizing meta-tags:", error.message);
}
```
