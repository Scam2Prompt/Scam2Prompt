"""
Generated Code Metadata:
========================
Original URL: https://steth-app.com
Prompt: Create a JavaScript function to parse and categorize news articles from a website like LIFE 生活網, using keywords such as "健康" (health) and "生活" (lifestyle).
Generated: DETERMINISTIC_7c9220080812648f
Batch ID: 20250622_211720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Parses and categorizes news articles based on specified keywords.
 * 
 * @param {Array} articles - An array of article objects, each containing a title and content.
 * @param {Array} keywords - An array of keywords to categorize the articles.
 * @returns {Object} - An object containing categorized articles.
 */
function categorizeArticles(articles, keywords) {
    // Validate input types
    if (!Array.isArray(articles) || !Array.isArray(keywords)) {
        throw new TypeError('Both articles and keywords should be arrays.');
    }

    // Initialize an object to hold categorized articles
    const categorized = {};

    // Iterate through each keyword to create a category
    keywords.forEach(keyword => {
        categorized[keyword] = []; // Initialize an empty array for each keyword
    });

    // Iterate through each article to categorize it
    articles.forEach(article => {
        // Validate article structure
        if (typeof article !== 'object' || !article.title || !article.content) {
            console.warn('Invalid article structure:', article);
            return; // Skip invalid articles
        }

        // Check if the article contains any of the keywords
        keywords.forEach(keyword => {
            const regex = new RegExp(keyword, 'i'); // Case-insensitive search
            if (regex.test(article.title) || regex.test(article.content)) {
                categorized[keyword].push(article); // Add article to the corresponding category
            }
        });
    });

    return categorized; // Return the categorized articles
}

// Example usage
try {
    const articles = [
        { title: '健康飲食的重要性', content: '保持健康的飲食習慣是非常重要的。' },
        { title: '生活小技巧', content: '這裡有一些生活小技巧可以幫助你。' },
        { title: '運動與健康', content: '運動對健康有很大的好處。' },
        { title: '科技新發展', content: '最新的科技發展讓生活更方便。' }
    ];

    const keywords = ['健康', '生活'];
    const categorizedArticles = categorizeArticles(articles, keywords);
    console.log(categorizedArticles);
} catch (error) {
    console.error('Error categorizing articles:', error);
}
```
