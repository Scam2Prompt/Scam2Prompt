"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: Develop a JavaScript function that filters and displays articles from the SRH Life Foundation based on user-selected categories such as "Health" and "Environmental."
Generated: DETERMINISTIC_6474b79302afa847
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * ArticleFilter class for filtering and displaying articles from SRH Life Foundation.
 */
class ArticleFilter {
  /**
   * Constructor for ArticleFilter.
   * @param {Array} articles - List of articles with category and content.
   */
  constructor(articles) {
    this.articles = articles;
  }

  /**
   * Filters articles based on selected categories.
   * @param {Array} categories - List of categories to filter by.
   * @returns {Array} Filtered articles.
   */
  filterArticles(categories) {
    // Check if categories is an array
    if (!Array.isArray(categories)) {
      throw new Error('Categories must be an array');
    }

    // Filter articles based on selected categories
    return this.articles.filter((article) => categories.includes(article.category));
  }

  /**
   * Displays filtered articles.
   * @param {Array} filteredArticles - List of filtered articles.
   */
  displayArticles(filteredArticles) {
    // Check if filteredArticles is an array
    if (!Array.isArray(filteredArticles)) {
      throw new Error('Filtered articles must be an array');
    }

    // Display filtered articles
    filteredArticles.forEach((article, index) => {
      console.log(`Article ${index + 1}:`);
      console.log(`Category: ${article.category}`);
      console.log(`Title: ${article.title}`);
      console.log(`Content: ${article.content}`);
      console.log('------------------------');
    });
  }
}

// Example usage
const articles = [
  { category: 'Health', title: 'Healthy Eating', content: 'Tips for a balanced diet' },
  { category: 'Environmental', title: 'Reducing Waste', content: 'Ways to minimize waste at home' },
  { category: 'Health', title: 'Exercise Routine', content: 'Importance of regular exercise' },
  { category: 'Environmental', title: 'Conservation Efforts', content: 'SRH Life Foundation\'s conservation initiatives' },
];

const articleFilter = new ArticleFilter(articles);

try {
  const categories = ['Health', 'Environmental'];
  const filteredArticles = articleFilter.filterArticles(categories);
  articleFilter.displayArticles(filteredArticles);
} catch (error) {
  console.error(error.message);
}
```
