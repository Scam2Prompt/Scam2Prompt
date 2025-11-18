"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socialimpactheroes.com
Prompt: Write a function in JavaScript to categorize articles from "Social Impact Heroes" into groups such as "Unstoppable!" and "Young Social Impact Heroes" based on keywords in their titles.
Generated: DETERMINISTIC_20e6d20241614256
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Categorizes articles into predefined groups based on keywords in their titles.
 *
 * @param {Array<Object>} articles - An array of article objects, each containing a title.
 * @returns {Object} An object with categorized articles.
 * @throws {TypeError} Throws an error if the input is not an array or if articles do not have titles.
 */
function categorizeArticles(articles) {
    // Validate input
    if (!Array.isArray(articles)) {
        throw new TypeError('Expected an array of articles.');
    }

    // Initialize result object
    const categorized = {
        unstoppable: [],
        youngHeroes: [],
        others: []
    };

    // Define keyword groups
    const unstoppableKeywords = ['unstoppable', 'heroic', 'brave'];
    const youngHeroesKeywords = ['young', 'youth', 'teen', 'kid'];

    // Categorize each article
    articles.forEach(article => {
        // Validate article structure
        if (typeof article !== 'object' || !article.title) {
            throw new TypeError('Each article must be an object with a title property.');
        }

        const titleLower = article.title.toLowerCase();
        let categorizedFlag = false;

        // Check for "Unstoppable!" keywords
        for (const keyword of unstoppableKeywords) {
            if (titleLower.includes(keyword)) {
                categorized.unstoppable.push(article);
                categorizedFlag = true;
                break;
            }
        }

        // Check for "Young Social Impact Heroes" keywords if not categorized yet
        if (!categorizedFlag) {
            for (const keyword of youngHeroesKeywords) {
                if (titleLower.includes(keyword)) {
                    categorized.youngHeroes.push(article);
                    categorizedFlag = true;
                    break;
                }
            }
        }

        // If not categorized, push to "others"
        if (!categorizedFlag) {
            categorized.others.push(article);
        }
    });

    return categorized;
}

// Example usage
try {
    const articles = [
        { title: 'The Unstoppable Journey of a Young Hero' },
        { title: 'How Teens are Changing the World' },
        { title: 'Brave Stories of Community Impact' },
        { title: 'Old Stories Not Related' }
    ];

    const result = categorizeArticles(articles);
    console.log(result);
} catch (error) {
    console.error('Error categorizing articles:', error.message);
}
```
