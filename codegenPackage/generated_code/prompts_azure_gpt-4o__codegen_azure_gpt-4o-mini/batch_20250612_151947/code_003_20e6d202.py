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
 * 
 * @param {Array<string>} articles - An array of article titles.
 * @returns {Object} An object containing categorized articles.
 * @throws {TypeError} Throws an error if the input is not an array of strings.
 */
function categorizeArticles(articles) {
    // Validate input
    if (!Array.isArray(articles)) {
        throw new TypeError('Input must be an array of strings.');
    }

    // Initialize categories
    const categories = {
        unstoppable: [],
        youngHeroes: [],
        others: []
    };

    // Define keywords for categorization
    const unstoppableKeywords = ['unstoppable', 'inspiring', 'impactful'];
    const youngHeroesKeywords = ['young', 'youth', 'teen'];

    // Categorize each article based on keywords
    articles.forEach(title => {
        if (typeof title !== 'string') {
            throw new TypeError('Each article title must be a string.');
        }

        const lowerTitle = title.toLowerCase();

        // Check for "Unstoppable!" category
        if (unstoppableKeywords.some(keyword => lowerTitle.includes(keyword))) {
            categories.unstoppable.push(title);
        }
        // Check for "Young Social Impact Heroes" category
        else if (youngHeroesKeywords.some(keyword => lowerTitle.includes(keyword))) {
            categories.youngHeroes.push(title);
        } 
        // If no keywords match, categorize as "others"
        else {
            categories.others.push(title);
        }
    });

    return categories;
}

// Example usage
try {
    const articles = [
        "Unstoppable Change Makers",
        "Young Innovators in Action",
        "The Inspiring Journey of a Social Entrepreneur",
        "Youth Leaders Making a Difference",
        "A Day in the Life of an Impactful Hero"
    ];

    const categorizedArticles = categorizeArticles(articles);
    console.log(categorizedArticles);
} catch (error) {
    console.error('Error categorizing articles:', error.message);
}
```
