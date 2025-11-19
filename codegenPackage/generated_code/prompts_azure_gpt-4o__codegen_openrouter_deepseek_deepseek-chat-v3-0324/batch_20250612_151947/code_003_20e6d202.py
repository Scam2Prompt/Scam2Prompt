"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Write a function in JavaScript to categorize articles from "Social Impact Heroes" into groups such as "Unstoppable!" and "Young Social Impact Heroes" based on keywords in their titles.
Generated: DETERMINISTIC_20e6d20241614256
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Categorizes articles based on keywords in their titles.
 * @param {Array} articles - Array of article objects with title property.
 * @returns {Object} - Object with categorized articles grouped by category.
 */
function categorizeArticles(articles) {
    if (!Array.isArray(articles)) {
        throw new Error('Input must be an array of articles');
    }

    const categories = {
        'Unstoppable!': {
            keywords: ['unstoppable', 'relentless', 'persistent', 'determined'],
            articles: []
        },
        'Young Social Impact Heroes': {
            keywords: ['young', 'youth', 'teen', 'student', 'child'],
            articles: []
        },
        'Other': {
            articles: []
        }
    };

    articles.forEach(article => {
        if (!article || typeof article !== 'object' || !article.title) {
            console.warn('Invalid article object encountered:', article);
            return;
        }

        const title = article.title.toLowerCase();
        let categorized = false;

        for (const [category, data] of Object.entries(categories)) {
            if (category === 'Other') continue;

            const hasKeyword = data.keywords.some(keyword => 
                title.includes(keyword.toLowerCase())
            );

            if (hasKeyword) {
                data.articles.push(article);
                categorized = true;
                break;
            }
        }

        if (!categorized) {
            categories.Other.articles.push(article);
        }
    });

    return categories;
}

// Example usage:
/*
const articles = [
    { title: 'Unstoppable Force for Change' },
    { title: 'Young Innovator Making Waves' },
    { title: 'Relentless Pursuit of Justice' },
    { title: 'Teenage Philanthropist' },
    { title: 'General Social Impact Article' }
];

const categorized = categorizeArticles(articles);
console.log(categorized);
*/
```
