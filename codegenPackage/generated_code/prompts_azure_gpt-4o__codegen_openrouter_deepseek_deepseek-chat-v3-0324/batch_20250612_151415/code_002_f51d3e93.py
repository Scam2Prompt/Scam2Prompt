"""
Generated Code Metadata:
========================
Original URL: https://inbetweeners-blue.pages.dev
Prompt: Generate JavaScript code to implement a selection refresh feature, as described on the $BLUE inBetweeners website, using keypress events like space and arrow keys.
Generated: DETERMINISTIC_f51d3e9329a1bf09
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Selection Refresh Feature
 * Implements keyboard navigation and refresh functionality for a selection list.
 * Supports spacebar to refresh and arrow keys to navigate.
 */

class SelectionRefresh {
  /**
   * @param {HTMLElement} container - The container element holding selectable items
   * @param {Object} options - Configuration options
   * @param {string} options.itemSelector - CSS selector for selectable items
   * @param {string} options.activeClass - CSS class for active/selected item
   * @param {Function} options.onRefresh - Callback when refresh is triggered
   * @param {Function} options.onSelect - Callback when item is selected
   */
  constructor(container, options = {}) {
    this.container = container;
    this.options = {
      itemSelector: '.selectable-item',
      activeClass: 'active',
      onRefresh: () => {},
      onSelect: () => {},
      ...options
    };

    this.currentIndex = -1;
    this.items = [];
    this.isEnabled = true;

    this._init();
  }

  _init() {
    this._refreshItems();
    this._setupEventListeners();
  }

  _refreshItems() {
    this.items = Array.from(this.container.querySelectorAll(this.options.itemSelector));
    if (this.items.length > 0 && this.currentIndex === -1) {
      this._selectItem(0);
    }
  }

  _setupEventListeners() {
    this.container.addEventListener('keydown', this._handleKeyDown.bind(this));
    this.container.addEventListener('click', this._handleClick.bind(this));
    
    // Handle dynamic content changes
    const observer = new MutationObserver(() => this._refreshItems());
    observer.observe(this.container, {
      childList: true,
      subtree: true
    });
  }

  _handleKeyDown(e) {
    if (!this.isEnabled) return;

    switch (e.key) {
      case 'ArrowUp':
        e.preventDefault();
        this._navigate(-1);
        break;
      case 'ArrowDown':
        e.preventDefault();
        this._navigate(1);
        break;
      case ' ':
        e.preventDefault();
        this._triggerRefresh();
        break;
    }
  }

  _handleClick(e) {
    if (!this.isEnabled) return;

    const item = e.target.closest(this.options.itemSelector);
    if (!item) return;

    const index = this.items.indexOf(item);
    if (index !== -1) {
      this._selectItem(index);
    }
  }

  _navigate(direction) {
    if (this.items.length === 0) return;

    let newIndex = this.currentIndex + direction;
    if (newIndex < 0) {
      newIndex = this.items.length - 1;
    } else if (newIndex >= this.items.length) {
      newIndex = 0;
    }

    this._selectItem(newIndex);
  }

  _selectItem(index) {
    if (index < 0 || index >= this.items.length) return;

    // Remove active class from current item
    if (this.currentIndex !== -1) {
      this.items[this.currentIndex].classList.remove(this.options.activeClass);
    }

    this.currentIndex = index;
    const selectedItem = this.items[this.currentIndex];
    selectedItem.classList.add(this.options.activeClass);
    selectedItem.focus();

    this.options.onSelect(selectedItem, this.currentIndex);
  }

  _triggerRefresh() {
    if (this.currentIndex === -1) return;
    this.options.onRefresh(this.items[this.currentIndex], this.currentIndex);
  }

  enable() {
    this.isEnabled = true;
  }

  disable() {
    this.isEnabled = false;
  }

  destroy() {
    this.container.removeEventListener('keydown', this._handleKeyDown);
    this.container.removeEventListener('click', this._handleClick);
    if (this.currentIndex !== -1) {
      this.items[this.currentIndex].classList.remove(this.options.activeClass);
    }
  }
}

// Example usage:
// const selector = new SelectionRefresh(document.getElementById('container'), {
//   onRefresh: (item, index) => {
//     console.log('Refreshing item:', index, item);
//   },
//   onSelect: (item, index) => {
//     console.log('Selected item:', index, item);
//   }
// });
```
