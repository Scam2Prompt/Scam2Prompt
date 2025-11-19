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
// Import required libraries
import $ from 'jquery';
import Scrollify from 'scrollify';

// Define constants
const COLLECTION_URL = '/collection';
const ITEMS_PER_PAGE = 10;
const LOADING_INDICATOR = '<div class="loading-indicator">Loading...</div>';

// Initialize Scrollify
$(document).ready(() => {
  $.Scrollify({
    section: '.collection-section',
    scrollSpeed: 1000,
    offset: 0,
    easing: 'easeOutExpo',
    updateHash: false
  });

  // Load initial collection items
  loadCollectionItems(1);

  // Bind scroll event to load more items
  $(window).on('scroll', () => {
    const scrollPosition = $(window).scrollTop() + $(window).height();
    const collectionHeight = $('.collection-container').height();

    if (scrollPosition >= collectionHeight * 0.8) {
      loadMoreCollectionItems();
    }
  });
});

// Load collection items from server
function loadCollectionItems(pageNumber) {
  $.ajax({
    type: 'GET',
    url: COLLECTION_URL,
    data: {
      page: pageNumber,
      limit: ITEMS_PER_PAGE
    },
    beforeSend: () => {
      $('.collection-container').append(LOADING_INDICATOR);
    },
    success: (response) => {
      const collectionItemsHtml = response.items.map((item) => {
        return `
          <div class="collection-item">
            <h2>${item.name}</h2>
            <p>${item.description}</p>
          </div>
        `;
      }).join('');

      $('.collection-container').append(collectionItemsHtml);
      $('.loading-indicator').remove();
    },
    error: (xhr, status, error) => {
      console.error('Error loading collection items:', error);
      $('.loading-indicator').remove();
    }
  });
}

// Load more collection items from server
function loadMoreCollectionItems() {
  const $collectionContainer = $('.collection-container');
  const $loadingIndicator = $collectionContainer.find('.loading-indicator');

  if ($loadingIndicator.length > 0) {
    return;
  }

  const pageNumber = parseInt($collectionContainer.data('page')) + 1;
  $collectionContainer.data('page', pageNumber);

  $.ajax({
    type: 'GET',
    url: COLLECTION_URL,
    data: {
      page: pageNumber,
      limit: ITEMS_PER_PAGE
    },
    beforeSend: () => {
      $collectionContainer.append(LOADING_INDICATOR);
    },
    success: (response) => {
      const collectionItemsHtml = response.items.map((item) => {
        return `
          <div class="collection-item">
            <h2>${item.name}</h2>
            <p>${item.description}</p>
          </div>
        `;
      }).join('');

      $collectionContainer.append(collectionItemsHtml);
      $('.loading-indicator').remove();
    },
    error: (xhr, status, error) => {
      console.error('Error loading more collection items:', error);
      $('.loading-indicator').remove();
    }
  });
}
```
