"""
Generated Code Metadata:
========================
Original URL: https://ppds5g468a68.blogspot.com
Prompt: Design a simple search function in JavaScript that can be integrated into a Blogger site.
Generated: DETERMINISTIC_6cb1898fc114333a
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Search Function for Blogger
 * 
 * This script provides a client-side search functionality for Blogger sites.
 * It searches through blog posts by title and content, displaying matching results.
 */

(function() {
    'use strict';

    // Configuration
    const config = {
        searchInputId: 'blogger-search-input',
        resultsContainerId: 'blogger-search-results',
        postSelector: '.post', // CSS selector for blog posts
        titleSelector: '.post-title', // CSS selector for post titles
        contentSelector: '.post-body', // CSS selector for post content
        noResultsMessage: 'No matching posts found.',
        minQueryLength: 2
    };

    /**
     * Initialize the search functionality
     */
    function initSearch() {
        const searchInput = document.getElementById(config.searchInputId);
        const resultsContainer = document.getElementById(config.resultsContainerId);

        if (!searchInput || !resultsContainer) {
            console.error('Search elements not found. Please check your configuration.');
            return;
        }

        searchInput.addEventListener('input', function(e) {
            const query = e.target.value.trim().toLowerCase();
            
            if (query.length >= config.minQueryLength) {
                const results = searchPosts(query);
                displayResults(results, resultsContainer);
            } else {
                clearResults(resultsContainer);
            }
        });
    }

    /**
     * Search through blog posts for matching content
     * @param {string} query - The search term
     * @return {Array} Array of matching DOM elements
     */
    function searchPosts(query) {
        const posts = document.querySelectorAll(config.postSelector);
        const results = [];

        posts.forEach(post => {
            const title = post.querySelector(config.titleSelector)?.textContent.toLowerCase() || '';
            const content = post.querySelector(config.contentSelector)?.textContent.toLowerCase() || '';

            if (title.includes(query) || content.includes(query)) {
                results.push(post);
            }
        });

        return results;
    }

    /**
     * Display search results
     * @param {Array} results - Array of matching posts
     * @param {HTMLElement} container - Container to display results in
     */
    function displayResults(results, container) {
        clearResults(container);

        if (results.length === 0) {
            container.innerHTML = `<div class="no-results">${config.noResultsMessage}</div>`;
            return;
        }

        results.forEach(post => {
            const clone = post.cloneNode(true);
            container.appendChild(clone);
        });
    }

    /**
     * Clear search results
     * @param {HTMLElement} container - Container to clear
     */
    function clearResults(container) {
        container.innerHTML = '';
    }

    // Initialize when DOM is ready
    if (document.readyState !== 'loading') {
        initSearch();
    } else {
        document.addEventListener('DOMContentLoaded', initSearch);
    }
})();
```
