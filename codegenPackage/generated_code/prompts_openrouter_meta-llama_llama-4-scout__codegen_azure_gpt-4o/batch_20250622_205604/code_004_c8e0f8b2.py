"""
Generated Code Metadata:
========================
Original URL: https://www.superstep.org
Prompt: Create a JavaScript function to analyze and visualize the most popular topics on a blog like Super Step, using data from article titles and content.
Generated: DETERMINISTIC_c8e0f8b24e1f4ef8
Batch ID: 20250622_205604
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to analyze and visualize the most popular topics on a blog.
 * This function takes an array of articles (title and content) and generates
 * a word frequency analysis to identify popular topics. It then visualizes
 * the results using a simple bar chart in the console.
 *
 * @param {Array} articles - Array of objects containing `title` and `content` properties.
 */
function analyzeAndVisualizeTopics(articles) {
  if (!Array.isArray(articles)) {
    throw new Error("Invalid input: articles must be an array.");
  }

  // Helper function to clean and tokenize text
  const tokenizeText = (text) => {
    if (typeof text !== "string") {
      throw new Error("Invalid text: Expected a string.");
    }
    return text
      .toLowerCase() // Convert to lowercase
      .replace(/[^a-z\s]/g, "") // Remove non-alphabetic characters
      .split(/\s+/) // Split into words
      .filter((word) => word.length > 2); // Filter out short words
  };

  // Combine all titles and content into a single text block
  let combinedText = "";
  articles.forEach((article) => {
    if (!article.title || !article.content) {
      throw new Error("Invalid article: Each article must have a title and content.");
    }
    combinedText += `${article.title} ${article.content} `;
  });

  // Tokenize the combined text
  const words = tokenizeText(combinedText);

  // Count word frequencies
  const wordFrequency = {};
  words.forEach((word) => {
    wordFrequency[word] = (wordFrequency[word] || 0) + 1;
  });

  // Sort words by frequency in descending order
  const sortedWords = Object.entries(wordFrequency).sort((a, b) => b[1] - a[1]);

  // Select the top 10 most frequent words
  const topWords = sortedWords.slice(0, 10);

  // Visualize the results as a bar chart in the console
  console.log("Top Topics:");
  topWords.forEach(([word, frequency]) => {
    console.log(`${word}: ${"#".repeat(frequency)}`);
  });
}

// Example usage:
const articles = [
  { title: "How to Start Running", content: "Running is a great way to stay fit and healthy." },
  { title: "Top 10 Running Shoes", content: "Choosing the right running shoes is essential for comfort and performance." },
  { title: "Benefits of Morning Runs", content: "Morning runs can boost your energy and improve your mood." },
];

try {
  analyzeAndVisualizeTopics(articles);
} catch (error) {
  console.error("Error:", error.message);
}
```
