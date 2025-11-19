"""
Generated Code Metadata:
========================
Original URL: https://apysolutions.com
Prompt: "Write a code snippet in JavaScript to implement a simple SEO optimization technique, such as meta tag generation, for a website."
Generated: DETERMINISTIC_4689922ced5fd536
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Generates and inserts SEO meta tags into the document head.
 * @param {Object} metaTags - An object containing key-value pairs for meta tags.
 * @param {string} metaTags.title - The title of the webpage.
 * @param {string} metaTags.description - A brief description of the webpage.
 * @param {string} metaTags.keywords - A comma-separated list of keywords for SEO.
 * @param {string} metaTags.author - The author of the webpage.
 */
function generateMetaTags(metaTags) {
    // Validate input
    if (typeof metaTags !== 'object' || metaTags === null) {
        console.error('Invalid input: metaTags must be a non-null object.');
        return;
    }

    // Create and append title tag
    if (metaTags.title) {
        const titleTag = document.createElement('title');
        titleTag.textContent = metaTags.title;
        document.head.appendChild(titleTag);
    }

    // Create and append description meta tag
    if (metaTags.description) {
        const descriptionTag = document.createElement('meta');
        descriptionTag.name = 'description';
        descriptionTag.content = metaTags.description;
        document.head.appendChild(descriptionTag);
    }

    // Create and append keywords meta tag
    if (metaTags.keywords) {
        const keywordsTag = document.createElement('meta');
        keywordsTag.name = 'keywords';
        keywordsTag.content = metaTags.keywords;
        document.head.appendChild(keywordsTag);
    }

    // Create and append author meta tag
    if (metaTags.author) {
        const authorTag = document.createElement('meta');
        authorTag.name = 'author';
        authorTag.content = metaTags.author;
        document.head.appendChild(authorTag);
    }
}

// Example usage
const seoMetaTags = {
    title: 'My Awesome Website',
    description: 'This is a brief description of my awesome website.',
    keywords: 'awesome, website, SEO, example',
    author: 'John Doe'
};

// Call the function to generate and insert meta tags
generateMetaTags(seoMetaTags);
```
