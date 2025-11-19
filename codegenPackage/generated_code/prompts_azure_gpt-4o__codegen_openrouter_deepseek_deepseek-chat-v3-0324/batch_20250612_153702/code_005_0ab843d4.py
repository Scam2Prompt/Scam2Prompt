"""
Generated Code Metadata:
========================
Original URL: https://dustbox.netlify.app
Prompt: Suggest methods to customize the table of contents functionality from Dustbox.netlify.app for a documentation website.
Generated: DETERMINISTIC_0ab843d4b7f26444
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Customizable Table of Contents (TOC) functionality for documentation websites.
 * 
 * Features:
 * - Auto-generates TOC from headings
 * - Smooth scrolling to sections
 * - Highlight active section while scrolling
 * - Customizable styling and behavior
 */

class CustomTOC {
  /**
   * Initialize the TOC
   * @param {Object} options - Configuration options
   * @param {string} options.containerSelector - Selector for TOC container
   * @param {string} options.contentSelector - Selector for content area
   * @param {number} options.headingLevel - Max heading level to include (1-6)
   * @param {string} options.activeClass - Class for active TOC item
   * @param {number} options.scrollOffset - Scroll offset for section positioning
   * @param {boolean} options.collapsible - Whether TOC items are collapsible
   */
  constructor(options = {}) {
    this.config = {
      containerSelector: '#toc',
      contentSelector: '#content',
      headingLevel: 3,
      activeClass: 'active',
      scrollOffset: 20,
      collapsible: true,
      ...options
    };

    this.tocContainer = document.querySelector(this.config.containerSelector);
    this.contentArea = document.querySelector(this.config.contentSelector);
    this.headings = [];
    this.tocItems = [];
    this.currentActive = null;

    if (!this.tocContainer || !this.contentArea) {
      console.error('TOC container or content area not found');
      return;
    }

    this.init();
  }

  /**
   * Initialize TOC functionality
   */
  init() {
    this.extractHeadings();
    this.generateTOC();
    this.setupEventListeners();
    this.setupIntersectionObserver();
  }

  /**
   * Extract headings from content area
   */
  extractHeadings() {
    const headingSelectors = [];
    for (let i = 1; i <= this.config.headingLevel; i++) {
      headingSelectors.push(`h${i}`);
    }

    const selector = headingSelectors.join(', ');
    this.headings = Array.from(this.contentArea.querySelectorAll(selector))
      .filter(heading => heading.id)
      .sort((a, b) => {
        return a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1;
      });
  }

  /**
   * Generate TOC HTML structure
   */
  generateTOC() {
    if (this.headings.length === 0) {
      this.tocContainer.innerHTML = '<p>No headings found</p>';
      return;
    }

    const fragment = document.createDocumentFragment();
    const ul = document.createElement('ul');
    ul.className = 'toc-list';

    this.headings.forEach((heading, index) => {
      const li = document.createElement('li');
      li.className = `toc-item toc-level-${heading.tagName.toLowerCase()}`;

      const a = document.createElement('a');
      a.href = `#${heading.id}`;
      a.textContent = heading.textContent;
      a.dataset.index = index;
      a.className = 'toc-link';

      if (this.config.collapsible && heading.tagName !== 'H1') {
        const toggle = document.createElement('span');
        toggle.className = 'toc-toggle';
        toggle.innerHTML = '&#9660;';
        li.prepend(toggle);
      }

      li.appendChild(a);
      ul.appendChild(li);
      this.tocItems.push(li);
    });

    fragment.appendChild(ul);
    this.tocContainer.innerHTML = '';
    this.tocContainer.appendChild(fragment);
  }

  /**
   * Setup event listeners for TOC interactions
   */
  setupEventListeners() {
    // Smooth scroll on TOC item click
    this.tocContainer.addEventListener('click', (e) => {
      const link = e.target.closest('a');
      if (!link) return;

      e.preventDefault();
      const targetId = link.getAttribute('href');
      const targetElement = document.querySelector(targetId);
      
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - this.config.scrollOffset,
          behavior: 'smooth'
        });
      }
    });

    // Collapsible functionality
    if (this.config.collapsible) {
      this.tocContainer.addEventListener('click', (e) => {
        const toggle = e.target.closest('.toc-toggle');
        if (!toggle) return;

        const listItem = toggle.parentElement;
        listItem.classList.toggle('collapsed');
      });
    }
  }

  /**
   * Setup IntersectionObserver to highlight active TOC item
   */
  setupIntersectionObserver() {
    const options = {
      rootMargin: '0px 0px -50% 0px',
      threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        const id = entry.target.getAttribute('id');
        const tocLink = this.tocContainer.querySelector(`a[href="#${id}"]`);
        
        if (entry.isIntersecting) {
          if (this.currentActive) {
            this.currentActive.classList.remove(this.config.activeClass);
          }
          tocLink.parentElement.classList.add(this.config.activeClass);
          this.currentActive = tocLink.parentElement;
        }
      });
    }, options);

    this.headings.forEach(heading => {
      observer.observe(heading);
    });
  }

  /**
   * Update TOC dynamically when content changes
   */
  update() {
    this.headings = [];
    this.tocItems = [];
    this.currentActive = null;
    this.init();
  }
}

// Example usage:
// const toc = new CustomTOC({
//   containerSelector: '#custom-toc',
//   contentSelector: '#main-content',
//   headingLevel: 4,
//   activeClass: 'current-section',
//   scrollOffset: 30,
//   collapsible: true
// });

// To update TOC if content changes dynamically:
// toc.update();
```
