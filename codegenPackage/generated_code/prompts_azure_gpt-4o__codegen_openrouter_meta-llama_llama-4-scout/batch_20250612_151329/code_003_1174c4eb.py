"""
Generated Code Metadata:
========================
Original URL: https://sdddd.pages.dev
Prompt: Write JavaScript code to implement a gift-opening animation for a web-based event, inspired by the "Day 5 Gifts" feature described on the chimpers-dojo website.
Generated: DETERMINISTIC_1174c4eba4dbf929
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// GiftOpeningAnimation.js

/**
 * GiftOpeningAnimation class.
 * 
 * This class implements a gift-opening animation inspired by the "Day5 Gifts" feature.
 * 
 * @class GiftOpeningAnimation
 */
class GiftOpeningAnimation {
  /**
   * Creates an instance of GiftOpeningAnimation.
   * 
   * @param {HTMLElement} giftElement - The gift element to animate.
   * @param {object} options - Animation options.
   * @param {string} options.openClass - Class to add when the gift is open.
   * @param {string} options.closeClass - Class to add when the gift is closed.
   * @param {number} options.animationDuration - Animation duration in milliseconds.
   * @memberof GiftOpeningAnimation
   */
  constructor(giftElement, options) {
    this.giftElement = giftElement;
    this.options = Object.assign({
      openClass: 'gift-open',
      closeClass: 'gift-close',
      animationDuration: 1000,
    }, options);

    // Check if giftElement is valid
    if (!(giftElement instanceof HTMLElement)) {
      throw new Error('Invalid gift element');
    }

    // Check if options are valid
    if (typeof this.options.openClass !== 'string' ||
        typeof this.options.closeClass !== 'string' ||
        typeof this.options.animationDuration !== 'number') {
      throw new Error('Invalid animation options');
    }

    // Initialize animation state
    this.isOpen = false;
  }

  /**
   * Opens the gift.
   * 
   * @memberof GiftOpeningAnimation
   */
  open() {
    if (this.isOpen) return;

    // Add open class
    this.giftElement.classList.add(this.options.openClass);

    // Remove close class
    this.giftElement.classList.remove(this.options.closeClass);

    // Trigger animation
    this.giftElement.style.transition = `all ${this.options.animationDuration}ms`;
    this.giftElement.style.transform = 'scale(1)';

    // Update animation state
    this.isOpen = true;

    // Clean up after animation
    setTimeout(() => {
      this.giftElement.style.transition = '';
    }, this.options.animationDuration);
  }

  /**
   * Closes the gift.
   * 
   * @memberof GiftOpeningAnimation
   */
  close() {
    if (!this.isOpen) return;

    // Add close class
    this.giftElement.classList.add(this.options.closeClass);

    // Remove open class
    this.giftElement.classList.remove(this.options.openClass);

    // Trigger animation
    this.giftElement.style.transition = `all ${this.options.animationDuration}ms`;
    this.giftElement.style.transform = 'scale(0.5)';

    // Update animation state
    this.isOpen = false;

    // Clean up after animation
    setTimeout(() => {
      this.giftElement.style.transition = '';
    }, this.options.animationDuration);
  }

  /**
   * Toggles the gift.
   * 
   * @memberof GiftOpeningAnimation
   */
  toggle() {
    if (this.isOpen) {
      this.close();
    } else {
      this.open();
    }
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  const giftElement = document.getElementById('gift');
  const animation = new GiftOpeningAnimation(giftElement, {
    openClass: 'gift-open',
    closeClass: 'gift-close',
    animationDuration: 1000,
  });

  // Open gift on click
  giftElement.addEventListener('click', () => {
    animation.toggle();
  });
});
```
