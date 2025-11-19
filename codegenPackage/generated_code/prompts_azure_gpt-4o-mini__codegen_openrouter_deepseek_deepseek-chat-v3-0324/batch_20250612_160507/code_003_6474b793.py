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
 * Filters and displays articles from the SRH Life Foundation based on selected categories.
 * @param {Array} articles - Array of article objects to filter.
 * @param {Array} selectedCategories - Array of category strings to filter by.
 * @returns {Array} Filtered array of articles matching the selected categories.
 * @throws {Error} If articles is not an array or selectedCategories is not an array.
 */
function filterArticlesByCategory(articles, selectedCategories) {
    // Validate input parameters
    if (!Array.isArray(articles)) {
        throw new Error('Articles must be an array');
    }
    if (!Array.isArray(selectedCategories)) {
        throw new Error('Selected categories must be an array');
    }

    // If no categories are selected, return all articles
    if (selectedCategories.length === 0) {
        return articles;
    }

    // Filter articles that match any of the selected categories
    return articles.filter(article => {
        // Ensure article has categories and it's an array
        if (!article.categories || !Array.isArray(article.categories)) {
            return false;
        }

        // Check if article has at least one matching category
        return article.categories.some(category => 
            selectedCategories.includes(category)
        );
    });
}

/**
 * Displays filtered articles in the DOM.
 * @param {Array} filteredArticles - Array of filtered article objects to display.
 * @param {string} containerId - ID of the DOM element to render articles in.
 * @throws {Error} If containerId is not found or filteredArticles is not an array.
 */
function displayFilteredArticles(filteredArticles, containerId) {
    // Validate input parameters
    if (!Array.isArray(filteredArticles)) {
        throw new Error('Filtered articles must be an array');
    }

    const container = document.getElementById(containerId);
    if (!container) {
        throw new Error(`Container with ID ${containerId} not found`);
    }

    // Clear previous content
    container.innerHTML = '';

    // Display message if no articles found
    if (filteredArticles.length === 0) {
        container.innerHTML = '<p>No articles found matching the selected categories.</p>';
        return;
    }

    // Create and append article elements
    filteredArticles.forEach(article => {
        const articleElement = document.createElement('div');
        articleElement.className = 'article';
        
        const titleElement = document.createElement('h2');
        titleElement.textContent = article.title || 'Untitled Article';
        
        const contentElement = document.createElement('p');
        contentElement.textContent = article.content || 'No content available';
        
        const categoriesElement = document.createElement('div');
        categoriesElement.className = 'categories';
        categoriesElement.textContent = `Categories: ${(article.categories || []).join(', ')}`;
        
        articleElement.appendChild(titleElement);
        articleElement.appendChild(contentElement);
        articleElement.appendChild(categoriesElement);
        
        container.appendChild(articleElement);
    });
}

/**
 * Example usage with event listeners for category selection
 */
document.addEventListener('DOMContentLoaded', () => {
    // Example articles data
    const articles = [
        {
            title: 'Healthy Living Tips',
            content: 'Learn how to maintain a healthy lifestyle...',
            categories: ['Health']
        },
        {
            title: 'Environmental Conservation',
            content: 'Ways to protect our environment...',
            categories: ['Environmental']
        },
        {
            title: 'Holistic Wellness',
            content: 'Combining physical and mental health approaches...',
            categories: ['Health', 'Wellness']
        }
    ];

    // Get category checkboxes
    const healthCheckbox = document.getElementById('health-category');
    const environmentalCheckbox = document.getElementById('environmental-category');
    const filterButton = document.getElementById('filter-button');

    if (filterButton) {
        filterButton.addEventListener('click', () => {
            try {
                // Get selected categories
                const selectedCategories = [];
                if (healthCheckbox && healthCheckbox.checked) {
                    selectedCategories.push('Health');
                }
                if (environmentalCheckbox && environmentalCheckbox.checked) {
                    selectedCategories.push('Environmental');
                }

                // Filter and display articles
                const filteredArticles = filterArticlesByCategory(articles, selectedCategories);
                displayFilteredArticles(filteredArticles, 'articles-container');
            } catch (error) {
                console.error('Error filtering articles:', error.message);
                alert('An error occurred while filtering articles. Please try again.');
            }
        });
    }
});
```
