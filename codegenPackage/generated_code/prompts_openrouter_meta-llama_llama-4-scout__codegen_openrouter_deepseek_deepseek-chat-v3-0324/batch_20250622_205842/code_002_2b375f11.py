"""
Generated Code Metadata:
========================
Original URL: https://2857qualifications.blogspot.com
Prompt: Generate code to create a custom search function for a Blogger site.
Generated: DETERMINISTIC_2b375f1137f9e334
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Custom Search Function for Blogger
 * 
 * This script provides a custom search functionality for Blogger sites.
 * It searches through blog posts and displays results in a user-friendly manner.
 */

(function() {
    'use strict';

    // Configuration
    const config = {
        resultsContainerId: 'search-results',
        searchInputId: 'search-input',
        noResultsMessage: 'No posts found matching your search criteria.',
        maxResults: 10,
        highlightClass: 'search-highlight'
    };

    // DOM Elements
    let searchInput;
    let resultsContainer;

    // Initialize the search functionality
    function init() {
        // Check if required elements exist
        searchInput = document.getElementById(config.searchInputId);
        resultsContainer = document.getElementById(config.resultsContainerId);

        if (!searchInput || !resultsContainer) {
            console.error('Search input or results container not found');
            return;
        }

        // Add event listeners
        searchInput.addEventListener('keyup', debounce(handleSearch, 300));
    }

    // Debounce function to limit search frequency
    function debounce(func, wait) {
        let timeout;
        return function() {
            const context = this;
            const args = arguments;
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(context, args), wait);
        };
    }

    // Handle search input
    function handleSearch() {
        const query = searchInput.value.trim().toLowerCase();
        
        if (query.length < 2) {
            clearResults();
            return;
        }

        fetchBlogPosts(query)
            .then(posts => displayResults(posts, query))
            .catch(error => {
                console.error('Search failed:', error);
                resultsContainer.innerHTML = '<p>Error occurred while searching. Please try again.</p>';
            });
    }

    // Fetch blog posts from Blogger API
    function fetchBlogPosts(query) {
        return new Promise((resolve, reject) => {
            try {
                // Blogger API endpoint
                const apiUrl = `/feeds/posts/default?alt=json&q=${encodeURIComponent(query)}&max-results=${config.maxResults}`;

                fetch(apiUrl)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`HTTP error! status: ${response.status}`);
                        }
                        return response.json();
                    })
                    .then(data => {
                        const posts = data.feed.entry || [];
                        resolve(posts);
                    })
                    .catch(error => reject(error));
            } catch (error) {
                reject(error);
            }
        });
    }

    // Display search results
    function displayResults(posts, query) {
        clearResults();

        if (posts.length === 0) {
            resultsContainer.innerHTML = `<p>${config.noResultsMessage}</p>`;
            return;
        }

        const resultsList = document.createElement('ul');
        resultsList.className = 'search-results-list';

        posts.forEach(post => {
            const listItem = document.createElement('li');
            const title = post.title.$t;
            const content = post.content.$t;
            const published = new Date(post.published.$t).toLocaleDateString();
            const postUrl = post.link.find(link => link.rel === 'alternate').href;

            // Highlight search terms in title and content
            const highlightedTitle = highlightText(title, query);
            const snippet = getContentSnippet(content, query);

            listItem.innerHTML = `
                <h3><a href="${postUrl}">${highlightedTitle}</a></h3>
                <p class="search-date">${published}</p>
                <p class="search-snippet">${snippet}</p>
            `;

            resultsList.appendChild(listItem);
        });

        resultsContainer.appendChild(resultsList);
    }

    // Highlight search terms in text
    function highlightText(text, query) {
        const regex = new RegExp(`(${query})`, 'gi');
        return text.replace(regex, `<span class="${config.highlightClass}">$1</span>`);
    }

    // Get a snippet of content with search terms highlighted
    function getContentSnippet(content, query) {
        const plainText = content.replace(/<[^>]*>/g, '');
        const queryIndex = plainText.toLowerCase().indexOf(query.toLowerCase());
        
        let start = Math.max(0, queryIndex - 50);
        let end = Math.min(plainText.length, queryIndex + query.length + 50);
        
        if (queryIndex === -1) {
            start = 0;
            end = Math.min(plainText.length, 100);
        }
        
        let snippet = plainText.substring(start, end);
        if (start > 0) snippet = '...' + snippet;
        if (end < plainText.length) snippet += '...';
        
        return highlightText(snippet, query);
    }

    // Clear search results
    function clearResults() {
        resultsContainer.innerHTML = '';
    }

    // Initialize when DOM is loaded
    document.addEventListener('DOMContentLoaded', init);
})();
```
