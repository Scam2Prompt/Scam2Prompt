"""
Generated Code Metadata:
========================
Original URL: https://scrollify.gitbook.io
Prompt: Write a JavaScript code snippet to implement infinite scrolling with auto-load functionality on a collection page using Scrollify.
Generated: DETERMINISTIC_ed623cb99d7e9fb4
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Infinite scrolling implementation using Scrollify
 * @param {string} containerSelector - Selector for the scroll container
 * @param {string} itemSelector - Selector for individual items
 * @param {function} loadMoreCallback - Function to fetch more items
 * @param {object} options - Configuration options
 */
function initInfiniteScroll(containerSelector, itemSelector, loadMoreCallback, options = {}) {
    const defaults = {
        threshold: 200, // pixels from bottom to trigger load
        loadingClass: 'loading',
        errorClass: 'error',
        debounceDelay: 300
    };
    const config = { ...defaults, ...options };
    let isLoading = false;
    let hasMore = true;
    let debounceTimeout;

    const container = document.querySelector(containerSelector);
    if (!container) {
        console.error('Container element not found');
        return;
    }

    /**
     * Check if scroll position is near bottom
     */
    function isNearBottom() {
        const { scrollTop, scrollHeight, clientHeight } = container;
        return scrollHeight - (scrollTop + clientHeight) <= config.threshold;
    }

    /**
     * Load more items when scrolled near bottom
     */
    async function handleScroll() {
        if (isLoading || !hasMore || !isNearBottom()) return;

        clearTimeout(debounceTimeout);
        debounceTimeout = setTimeout(async () => {
            try {
                isLoading = true;
                container.classList.add(config.loadingClass);
                
                const items = await loadMoreCallback();
                if (items && items.length > 0) {
                    const fragment = document.createDocumentFragment();
                    items.forEach(item => {
                        const element = document.createElement('div');
                        element.className = itemSelector.replace('.', '');
                        element.innerHTML = item;
                        fragment.appendChild(element);
                    });
                    container.appendChild(fragment);
                } else {
                    hasMore = false;
                }
            } catch (error) {
                console.error('Error loading more items:', error);
                container.classList.add(config.errorClass);
            } finally {
                isLoading = false;
                container.classList.remove(config.loadingClass);
            }
        }, config.debounceDelay);
    }

    // Initialize Scrollify
    $(containerSelector).scrollify({
        after: handleScroll,
        scrollSpeed: 1000,
        setHeights: false,
        overflowScroll: true
    });

    // Cleanup function
    return function cleanup() {
        clearTimeout(debounceTimeout);
        $(containerSelector).scrollify('destroy');
    };
}

// Example usage:
/*
const loadMoreItems = async () => {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1000));
    return ['<div>New Item 1</div>', '<div>New Item 2</div>'];
};

const cleanup = initInfiniteScroll(
    '.scroll-container',
    '.item',
    loadMoreItems,
    { threshold: 300 }
);

// Call cleanup() when needed to remove event listeners
*/
```
