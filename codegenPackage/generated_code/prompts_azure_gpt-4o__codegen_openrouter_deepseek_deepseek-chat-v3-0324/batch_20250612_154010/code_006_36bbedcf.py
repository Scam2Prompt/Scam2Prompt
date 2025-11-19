"""
Generated Code Metadata:
========================
Original URL: https://fli.so
Prompt: Provide an example of how to integrate keyboard shortcuts into a link management system for rapid workflow, similar to Fli.so's power user features.
Generated: DETERMINISTIC_36bbedcf25dd7841
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// LinkManagementSystem.js
class LinkManagementSystem {
  constructor() {
    this.links = [];
    this.currentIndex = -1;
    this.shortcuts = {
      'ArrowUp': this.selectPreviousLink.bind(this),
      'ArrowDown': this.selectNextLink.bind(this),
      'Enter': this.openSelectedLink.bind(this),
      'Escape': this.clearSelection.bind(this),
      'n': this.createNewLink.bind(this),
      'd': this.deleteSelectedLink.bind(this),
      'e': this.editSelectedLink.bind(this)
    };

    this.initialize();
  }

  /**
   * Initialize the system and event listeners
   */
  initialize() {
    this.loadLinksFromStorage();
    this.setupKeyboardShortcuts();
    this.renderLinks();
  }

  /**
   * Setup keyboard shortcut listeners
   */
  setupKeyboardShortcuts() {
    document.addEventListener('keydown', (event) => {
      // Ignore if typing in an input field
      if (event.target.tagName === 'INPUT') return;

      const handler = this.shortcuts[event.key];
      if (handler) {
        event.preventDefault();
        handler();
      }
    });
  }

  /**
   * Load links from localStorage
   */
  loadLinksFromStorage() {
    try {
      const storedLinks = localStorage.getItem('links');
      if (storedLinks) {
        this.links = JSON.parse(storedLinks);
      }
    } catch (error) {
      console.error('Failed to load links:', error);
    }
  }

  /**
   * Save links to localStorage
   */
  saveLinksToStorage() {
    try {
      localStorage.setItem('links', JSON.stringify(this.links));
    } catch (error) {
      console.error('Failed to save links:', error);
    }
  }

  /**
   * Render all links in the UI
   */
  renderLinks() {
    const container = document.getElementById('links-container');
    if (!container) return;

    container.innerHTML = '';
    this.links.forEach((link, index) => {
      const linkElement = document.createElement('div');
      linkElement.className = `link-item ${index === this.currentIndex ? 'selected' : ''}`;
      linkElement.innerHTML = `
        <a href="${link.url}" target="_blank">${link.title}</a>
        <span class="edit-btn" data-index="${index}">✏️</span>
      `;
      container.appendChild(linkElement);
    });
  }

  /**
   * Select the previous link in the list
   */
  selectPreviousLink() {
    if (this.links.length === 0) return;
    this.currentIndex = Math.max(0, this.currentIndex - 1);
    this.renderLinks();
  }

  /**
   * Select the next link in the list
   */
  selectNextLink() {
    if (this.links.length === 0) return;
    this.currentIndex = Math.min(this.links.length - 1, this.currentIndex + 1);
    this.renderLinks();
  }

  /**
   * Open the currently selected link
   */
  openSelectedLink() {
    if (this.currentIndex >= 0 && this.currentIndex < this.links.length) {
      window.open(this.links[this.currentIndex].url, '_blank');
    }
  }

  /**
   * Clear the current selection
   */
  clearSelection() {
    this.currentIndex = -1;
    this.renderLinks();
  }

  /**
   * Create a new link
   */
  createNewLink() {
    const title = prompt('Enter link title:');
    if (!title) return;

    const url = prompt('Enter URL:');
    if (!url) return;

    this.links.push({ title, url });
    this.currentIndex = this.links.length - 1;
    this.saveLinksToStorage();
    this.renderLinks();
  }

  /**
   * Delete the selected link
   */
  deleteSelectedLink() {
    if (this.currentIndex >= 0 && this.currentIndex < this.links.length) {
      if (confirm('Are you sure you want to delete this link?')) {
        this.links.splice(this.currentIndex, 1);
        this.currentIndex = Math.min(this.currentIndex, this.links.length - 1);
        this.saveLinksToStorage();
        this.renderLinks();
      }
    }
  }

  /**
   * Edit the selected link
   */
  editSelectedLink() {
    if (this.currentIndex >= 0 && this.currentIndex < this.links.length) {
      const link = this.links[this.currentIndex];
      const newTitle = prompt('Edit title:', link.title);
      if (newTitle === null) return;

      const newUrl = prompt('Edit URL:', link.url);
      if (newUrl === null) return;

      link.title = newTitle;
      link.url = newUrl;
      this.saveLinksToStorage();
      this.renderLinks();
    }
  }
}

// Initialize the system when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const linkSystem = new LinkManagementSystem();
});

// HTML structure needed for this to work:
/*
<!DOCTYPE html>
<html>
<head>
  <title>Link Management System</title>
  <style>
    .link-item { padding: 8px; margin: 4px; border: 1px solid #ddd; }
    .selected { background-color: #f0f0f0; border-color: #999; }
    .edit-btn { margin-left: 10px; cursor: pointer; }
  </style>
</head>
<body>
  <div id="links-container"></div>
  <script src="LinkManagementSystem.js"></script>
</body>
</html>
*/
```
