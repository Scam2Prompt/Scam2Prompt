"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marchigue.cl
Prompt: Recommend an API or library to implement accessibility features like color inversion, screen reader support, and font scaling, as described on the Turismo Marchigüe website.
Generated: DETERMINISTIC_f76b39583a53c407
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a code implementation in JavaScript using the popular `axe-core` library for accessibility testing and enhancements. However, note that a complete implementation of the requested features requires integration with UI elements and additional libraries. The provided code demonstrates accessibility features like screen reader support, font scaling, and color inversion.

```javascript
// Import necessary libraries
// Ensure you install axe-core: `npm install axe-core`
import axe from 'axe-core';

// Accessibility Manager Class
class AccessibilityManager {
  constructor() {
    this.defaultFontSize = 16; // Default font size in pixels
    this.initAccessibilityFeatures();
  }

  // Initialize accessibility features
  initAccessibilityFeatures() {
    // Ensure axe-core is initialized
    axe.run((err, results) => {
      if (err) {
        console.error('Error initializing accessibility audit:', err);
      } else {
        console.log('Accessibility audit results:', results);
      }
    });

    // Add event listeners for accessibility controls
    this.setupControls();
  }

  // Toggle color inversion
  toggleColorInversion() {
    const body = document.body;
    const isInverted = body.classList.contains('color-inverted');

    if (isInverted) {
      body.classList.remove('color-inverted');
    } else {
      body.classList.add('color-inverted');
    }
  }

  // Increase font size
  increaseFontSize() {
    this.defaultFontSize += 2;
    document.documentElement.style.fontSize = `${this.defaultFontSize}px`;
  }

  // Decrease font size
  decreaseFontSize() {
    if (this.defaultFontSize > 10) {
      this.defaultFontSize -= 2;
      document.documentElement.style.fontSize = `${this.defaultFontSize}px`;
    }
  }

  // Reset font size
  resetFontSize() {
    this.defaultFontSize = 16;
    document.documentElement.style.fontSize = `${this.defaultFontSize}px`;
  }

  // Set up UI controls for accessibility
  setupControls() {
    // Create buttons for accessibility features
    const container = document.createElement('div');
    container.id = 'accessibility-controls';
    container.style.position = 'fixed';
    container.style.bottom = '10px';
    container.style.right = '10px';

    const invertColorsBtn = this.createButton('Invert Colors', () =>
      this.toggleColorInversion()
    );
    const increaseFontBtn = this.createButton('Increase Font Size', () =>
      this.increaseFontSize()
    );
    const decreaseFontBtn = this.createButton('Decrease Font Size', () =>
      this.decreaseFontSize()
    );
    const resetFontBtn = this.createButton('Reset Font Size', () =>
      this.resetFontSize()
    );

    container.appendChild(invertColorsBtn);
    container.appendChild(increaseFontBtn);
    container.appendChild(decreaseFontBtn);
    container.appendChild(resetFontBtn);

    document.body.appendChild(container);
  }

  // Helper method to create buttons
  createButton(label, onClick) {
    const button = document.createElement('button');
    button.textContent = label;
    button.style.margin = '5px';
    button.style.padding = '10px';
    button.style.fontSize = '14px';
    button.style.cursor = 'pointer';
    button.setAttribute('aria-label', label); // Screen reader friendly
    button.addEventListener('click', onClick);
    return button;
  }
}

// Apply a CSS class for color inversion
const style = document.createElement('style');
style.textContent = `
  .color-inverted {
    filter: invert(100%);
  }
`;
document.head.appendChild(style);

// Initialize accessibility features
window.addEventListener('DOMContentLoaded', () => {
  new AccessibilityManager();
});
```

### Installation Instructions:
1. Add the `axe-core` library via `npm install axe-core`.
2. Include the script in your project as shown above.
3. Add the stylesheet for inverted colors to ensure proper rendering.

This code adheres to best practices, includes error handling, and is ready for integration into your site.
