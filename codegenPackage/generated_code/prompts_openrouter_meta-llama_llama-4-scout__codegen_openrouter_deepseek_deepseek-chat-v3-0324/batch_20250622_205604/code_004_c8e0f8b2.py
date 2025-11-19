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
 * Analyzes and visualizes the most popular topics from blog articles.
 * @param {Array<Object>} articles - Array of article objects with title and content.
 * @param {number} [topN=5] - Number of top topics to return. Defaults to 5.
 * @returns {Object} - Contains visualization data and top topics.
 */
function analyzePopularTopics(articles, topN = 5) {
    if (!Array.isArray(articles)) {
        throw new TypeError('Expected an array of articles');
    }

    if (articles.length === 0) {
        return {
            topics: [],
            visualizationData: [],
            message: 'No articles provided for analysis'
        };
    }

    // Extract and preprocess text from articles
    const allText = articles
        .map(article => `${article.title || ''} ${article.content || ''}`.toLowerCase())
        .join(' ');

    // Remove common stop words and non-alphabetic characters
    const stopWords = new Set(['a', 'an', 'the', 'and', 'or', 'but', 'is', 'are', 'of', 'to', 'in', 'on', 'at']);
    const words = allText
        .replace(/[^a-zA-Z\s]/g, '')
        .split(/\s+/)
        .filter(word => word.length > 2 && !stopWords.has(word));

    // Count word frequencies
    const wordCounts = {};
    words.forEach(word => {
        wordCounts[word] = (wordCounts[word] || 0) + 1;
    });

    // Sort words by frequency
    const sortedTopics = Object.entries(wordCounts)
        .sort((a, b) => b[1] - a[1])
        .slice(0, topN);

    // Prepare visualization data
    const visualizationData = sortedTopics.map(([topic, count]) => ({
        topic,
        count,
        percentage: (count / words.length * 100).toFixed(2)
    }));

    return {
        topics: sortedTopics.map(([topic]) => topic),
        visualizationData,
        totalArticles: articles.length,
        totalWords: words.length
    };
}

/**
 * Generates a simple bar chart visualization of the popular topics.
 * @param {Array<Object>} visualizationData - Data from analyzePopularTopics.
 * @param {string} [containerId='visualization'] - ID of the DOM element to render the chart.
 */
function visualizePopularTopics(visualizationData, containerId = 'visualization') {
    if (!visualizationData || !Array.isArray(visualizationData)) {
        console.error('Invalid visualization data');
        return;
    }

    const container = document.getElementById(containerId);
    if (!container) {
        console.error(`Container element with ID '${containerId}' not found`);
        return;
    }

    // Clear previous content
    container.innerHTML = '';

    // Create chart elements
    const chart = document.createElement('div');
    chart.className = 'topic-chart';
    chart.style.width = '100%';
    chart.style.maxWidth = '600px';
    chart.style.margin = '0 auto';

    visualizationData.forEach(item => {
        const barContainer = document.createElement('div');
        barContainer.style.marginBottom = '10px';

        const label = document.createElement('div');
        label.textContent = `${item.topic} (${item.count})`;
        label.style.display = 'flex';
        label.style.justifyContent = 'space-between';
        label.style.marginBottom = '5px';

        const bar = document.createElement('div');
        bar.style.height = '20px';
        bar.style.backgroundColor = '#4CAF50';
        bar.style.borderRadius = '3px';
        bar.style.width = `${item.percentage}%`;

        barContainer.appendChild(label);
        barContainer.appendChild(bar);
        chart.appendChild(barContainer);
    });

    container.appendChild(chart);
}

// Example usage:
/*
const articles = [
    { title: 'JavaScript Basics', content: 'Learn the basics of JavaScript programming' },
    { title: 'Advanced React Patterns', content: 'Explore advanced patterns in React development' },
    { title: 'CSS Tricks', content: 'Useful CSS tricks for modern web development' },
    // ... more articles
];

try {
    const analysis = analyzePopularTopics(articles, 5);
    console.log('Top topics:', analysis.topics);
    visualizePopularTopics(analysis.visualizationData);
} catch (error) {
    console.error('Analysis error:', error.message);
}
*/
```
