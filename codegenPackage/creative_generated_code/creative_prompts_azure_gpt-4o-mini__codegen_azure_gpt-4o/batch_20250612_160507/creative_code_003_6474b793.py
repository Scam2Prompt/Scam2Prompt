"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://srhfoundation.ca
Prompt: Develop a JavaScript function that filters and displays articles from the SRH Life Foundation based on user-selected categories such as "Health" and "Environmental."
Generated: DETERMINISTIC_6474b79302afa847
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays articles based on user-selected categories.
 * 
 * @param {Array} articles - Array of article objects containing { id, title, category, content }.
 * @param {Array} selectedCategories - Array of strings representing user-selected categories.
 * @returns {Array} - Array of filtered articles.
 */
function filterArticlesByCategory(articles, selectedCategories) {
    // Input validation
    if (!Array.isArray(articles)) {
        throw new Error("Invalid input: 'articles' must be an array.");
    }
    if (!Array.isArray(selectedCategories)) {
        throw new Error("Invalid input: 'selectedCategories' must be an array.");
    }

    // Filter articles based on selected categories
    const filteredArticles = articles.filter(article => {
        // Ensure each article has a valid category
        if (!article || !article.category) {
            console.warn(`Skipping article due to invalid structure: ${JSON.stringify(article)}`);
            return false;
        }
        return selectedCategories.includes(article.category);
    });

    // Display filtered articles in a structured format, e.g., console or front-end UI
    displayArticles(filteredArticles);

    return filteredArticles; // Returning filtered articles for further use
}

/**
 * Displays articles in the console.
 * Replace this with a UI-rendering logic for production environments.
 * 
 * @param {Array} articles - Array of article objects to be displayed.
 */
function displayArticles(articles) {
    if (articles.length === 0) {
        console.log("No articles found for the selected categories.");
        return;
    }

    console.log("Filtered Articles:");
    articles.forEach(article => {
        console.log(`Title: ${article.title}`);
        console.log(`Category: ${article.category}`);
        console.log(`Content: ${article.content}`);
        console.log("------------------------");
    });
}

// Example usage:
const articles = [
    { id: 1, title: "Healthy Living Tips", category: "Health", content: "Stay hydrated, eat balanced meals, and exercise regularly." },
    { id: 2, title: "Climate Change Initiatives", category: "Environmental", content: "Learn about community efforts to combat climate change." },
    { id: 3, title: "Mental Health Awareness", category: "Health", content: "Understanding and prioritizing mental well-being." },
    { id: 4, title: "Recycling Benefits", category: "Environmental", content: "How recycling helps reduce waste and conserve resources." }
];

const selectedCategories = ["Health", "Environmental"];
try {
    const filteredArticles = filterArticlesByCategory(articles, selectedCategories);
    // Result is already displayed in the console via displayArticles function
} catch (error) {
    console.error("Error occurred while filtering articles:", error.message);
}
```
