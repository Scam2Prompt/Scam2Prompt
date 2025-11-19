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
 * Categorize articles from "Social Impact Heroes" into groups based on keywords in their titles.
 */

/**
 * ArticleCategorizer class.
 */
class ArticleCategorizer {
  /**
   * Constructor for ArticleCategorizer.
   * @param {Object} categories - An object containing category names as keys and arrays of keywords as values.
   */
  constructor(categories) {
    this.categories = categories;
  }

  /**
   * Categorize an article based on its title.
   * @param {string} title - The title of the article.
   * @returns {string[]} An array of categories that the article belongs to.
   */
  categorizeArticle(title) {
    const categoriesMatched = [];

    // Iterate over each category and its keywords
    Object.keys(this.categories).forEach((category) => {
      const keywords = this.categories[category];

      // Check if any keyword is present in the title (case-insensitive)
      if (keywords.some((keyword) => title.toLowerCase().includes(keyword.toLowerCase()))) {
        categoriesMatched.push(category);
      }
    });

    return categoriesMatched;
  }
}

// Define categories and their keywords
const categories = {
  "Unstoppable!": ["unstoppable", "inspiration", "hero"],
  "Young Social Impact Heroes": ["young", "youth", "teen"],
  "Environmental Heroes": ["environment", "sustainability", "green"],
};

// Create an instance of ArticleCategorizer
const articleCategorizer = new ArticleCategorizer(categories);

// Example usage
function main() {
  try {
    const articles = [
      { title: "The Unstoppable Woman Changing Lives" },
      { title: "Young Teen Makes a Big Impact on Sustainability" },
      { title: "The Environmental Hero You Need to Know" },
      { title: "No Keywords Here" },
    ];

    articles.forEach((article) => {
      const categories = articleCategorizer.categorizeArticle(article.title);
      console.log(`Article: ${article.title}`);
      console.log(`Categories: ${categories.join(", ") || "No categories matched"}`);
      console.log("---");
    });
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

main();
```
