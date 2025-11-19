"""
Generated Code Metadata:
========================
Original URL: https://mainnet-nobody.pages.dev
Prompt: Recommend a suitable JavaScript library for creating a full-page scrolling website, considering the example of the Nobody NFT project webpage.
Generated: DETERMINISTIC_6e10a7e064bfe492
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import fullpage from 'fullpage.js';

// Define a class for the full-page scrolling website
class FullPageScrollingWebsite {
  /**
   * Initialize the full-page scrolling website
   * @param {object} options - Configuration options for fullpage.js
   */
  constructor(options) {
    // Merge default options with user-provided options
    this.options = {
      scrollingSpeed: 600,
      navigation: true,
      navigationPosition: 'right',
      navigationTooltips: [],
      ...options,
    };

    // Initialize fullpage.js
    this.fullpage = new fullpage('#fullpage', this.options);
  }

  /**
   * Add a new section to the full-page scrolling website
   * @param {string} html - HTML content for the section
   */
  addSection(html) {
    // Create a new section element
    const section = document.createElement('div');
    section.classList.add('section');
    section.innerHTML = html;

    // Add the section to the full-page scrolling website
    document.querySelector('#fullpage').appendChild(section);
  }

  /**
   * Add a new slide to the current section
   * @param {string} html - HTML content for the slide
   */
  addSlide(html) {
    // Get the current section
    const section = document.querySelector('.active');

    // Create a new slide element
    const slide = document.createElement('div');
    slide.classList.add('slide');
    slide.innerHTML = html;

    // Add the slide to the current section
    section.appendChild(slide);
  }
}

// Example usage
try {
  // Create a new full-page scrolling website
  const website = new FullPageScrollingWebsite({
    navigationTooltips: ['Section 1', 'Section 2', 'Section 3'],
  });

  // Add sections and slides
  website.addSection('<h1>Section 1</h1>');
  website.addSection('<h1>Section 2</h1>');
  website.addSlide('<h2>Slide 1</h2>');
  website.addSlide('<h2>Slide 2</h2>');
} catch (error) {
  console.error('Error:', error);
}

// Run the script when the document is ready
document.addEventListener('DOMContentLoaded', () => {
  // Code here
});
```
