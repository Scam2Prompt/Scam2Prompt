"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write code for a scroll progress indicator that works seamlessly in Webflow without jank.
Generated: DETERMINISTIC_7131b7049ec0c224
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ScrollProgressIndicator.js

class ScrollProgressIndicator {
  /**
   * Creates a new ScrollProgressIndicator instance.
   * 
   * @param {Object} options - Configuration options.
   * @param {HTMLElement} options.element - The container element for the progress indicator.
   * @param {HTMLElement} options.progressElement - The element that will display the progress.
   * @param {String} options.progressClass - The class name to apply to the progress element when it's visible.
   */
  constructor(options) {
    this.element = options.element;
    this.progressElement = options.progressElement;
    this.progressClass = options.progressClass;

    // Check if required options are provided
    if (!this.element || !this.progressElement || !this.progressClass) {
      throw new Error('Required options are missing');
    }

    // Initialize event listeners
    this.handleScroll = this.handleScroll.bind(this);

    // Add event listener to the window
    window.addEventListener('scroll', this.handleScroll);

    // Initialize progress indicator
    this.updateProgress();
  }

  /**
   * Updates the progress indicator based on the current scroll position.
   */
  updateProgress() {
    // Calculate scroll progress
    const scrollTop = window.scrollY;
    const scrollHeight = document.body.offsetHeight - window.innerHeight;
    const progress = scrollHeight === 0 ? 0 : scrollTop / scrollHeight;

    // Update progress element
    this.progressElement.style.width = `${progress * 100}%`;

    // Toggle progress class
    if (progress > 0) {
      this.progressElement.classList.add(this.progressClass);
    } else {
      this.progressElement.classList.remove(this.progressClass);
    }
  }

  /**
   * Handles the scroll event.
   */
  handleScroll() {
    // Debounce scroll events to prevent excessive updates
    if (this.timeoutId) {
      clearTimeout(this.timeoutId);
    }

    this.timeoutId = setTimeout(() => {
      this.updateProgress();
    }, 100);
  }

  /**
   * Destroys the ScrollProgressIndicator instance.
   */
  destroy() {
    // Remove event listener from the window
    window.removeEventListener('scroll', this.handleScroll);

    // Reset progress element
    this.progressElement.style.width = '';
    this.progressElement.classList.remove(this.progressClass);
  }
}

// Example usage:
const indicator = new ScrollProgressIndicator({
  element: document.body,
  progressElement: document.querySelector('.progress-indicator'),
  progressClass: 'visible',
});

// Clean up on page unload
window.onunload = () => {
  indicator.destroy();
};
```

```css
/* styles.css */

.progress-indicator {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: #ccc;
  transform-origin: left;
  transition: width 0.2s ease-in-out;
}

.progress-indicator.visible {
  opacity: 1;
}

.progress-indicator:not(.visible) {
  opacity: 0;
}
```
