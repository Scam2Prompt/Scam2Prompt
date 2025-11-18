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
 * Generates optimized SEO meta-tags for a business website.
 * 
 * @param {string} title - The title of the webpage (max 60 characters).
 * @param {string} description - A brief description of the webpage (max 160 characters).
 * @param {string[]} keywords - An array of keywords related to the webpage.
 * @param {string} author - The author of the content.
 * @throws {Error} If any input exceeds the specified character limits.
 * @returns {string} The generated meta tags as a string.
 */
function generateSEOMetaTags(title, description, keywords, author) {
    // Validate input length
    if (title.length > 60) {
        throw new Error('Title exceeds the maximum length of 60 characters.');
    }
    if (description.length > 160) {
        throw new Error('Description exceeds the maximum length of 160 characters.');
    }
    if (!Array.isArray(keywords) || keywords.some(keyword => keyword.length === 0)) {
        throw new Error('Keywords must be a non-empty array of strings.');
    }
    if (author.length === 0) {
        throw new Error('Author must be a non-empty string.');
    }

    // Prepare meta tags
    const metaTags = `
        <title>${escapeHtml(title)}</title>
        <meta name="description" content="${escapeHtml(description)}">
        <meta name="keywords" content="${escapeHtml(keywords.join(', '))}">
        <meta name="author" content="${escapeHtml(author)}">
    `;

    return metaTags.trim();
}

/**
 * Escapes HTML special characters in a string to prevent XSS.
 * 
 * @param {string} str - The string to escape.
 * @returns {string} The escaped string.
 */
function escapeHtml(str) {
    const escapeChars = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
    };
    return str.replace(/[&<>"']/g, char => escapeChars[char] || char);
}

// Example usage with error handling
try {
    const metaTags = generateSEOMetaTags(
        'Our Amazing Business',
        'We provide exceptional services to our clients.',
        ['business', 'services', 'clients', 'quality'],
        'MDA Tech Sys'
    );
    console.log(metaTags);
} catch (error) {
    console.error('Error generating meta tags:', error.message);
}
```
