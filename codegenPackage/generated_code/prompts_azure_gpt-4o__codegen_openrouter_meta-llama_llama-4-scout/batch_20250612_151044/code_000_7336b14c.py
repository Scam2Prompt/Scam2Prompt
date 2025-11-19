"""
Generated Code Metadata:
========================
Original URL: https://boredturtleyc.netlify.app
Prompt: Write JavaScript code to display a custom loading message when a web application requires JavaScript to run, similar to the behavior described on the "Bored Turtle Yacht Club" webpage.
Generated: DETERMINISTIC_7336b14c02d4d34a
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// loading-overlay.js

class LoadingOverlay {
  /**
   * Creates a new LoadingOverlay instance.
   * @param {string} message - The loading message to display.
   * @param {string} containerSelector - The CSS selector of the container element.
   */
  constructor(message, containerSelector = 'body') {
    this.message = message;
    this.containerSelector = containerSelector;
    this.overlayElement = null;
  }

  /**
   * Displays the loading overlay.
   */
  show() {
    if (!this.overlayElement) {
      this.createOverlayElement();
    }
    this.overlayElement.classList.add('visible');
  }

  /**
   * Hides the loading overlay.
   */
  hide() {
    if (this.overlayElement) {
      this.overlayElement.classList.remove('visible');
    }
  }

  /**
   * Creates the loading overlay element.
   */
  createOverlayElement() {
    const container = document.querySelector(this.containerSelector);
    if (!container) {
      throw new Error(`Container element not found: ${this.containerSelector}`);
    }

    const overlayHtml = `
      <div class="loading-overlay">
        <div class="loading-message">${this.message}</div>
      </div>
    `;

    const overlayElement = document.createElement('div');
    overlayElement.innerHTML = overlayHtml;
    container.appendChild(overlayElement);

    this.overlayElement = overlayElement.querySelector('.loading-overlay');

    // Add CSS styles for the loading overlay
    const style = document.createElement('style');
    style.textContent = `
      .loading-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 255, 255, 0.8);
        display: flex;
        justify-content: center;
        align-items: center;
        opacity: 0;
        transition: opacity 0.3s ease-in-out;
        pointer-events: none;
      }

      .loading-overlay.visible {
        opacity: 1;
        pointer-events: all;
      }

      .loading-message {
        font-size: 18px;
        font-weight: bold;
        color: #333;
      }
    `;
    document.head.appendChild(style);
  }
}

// Example usage:
document.addEventListener('DOMContentLoaded', () => {
  const loadingOverlay = new LoadingOverlay('JavaScript is required to run this application.');
  loadingOverlay.show();

  // Simulate some work...
  setTimeout(() => {
    loadingOverlay.hide();
  }, 2000);
});
```
