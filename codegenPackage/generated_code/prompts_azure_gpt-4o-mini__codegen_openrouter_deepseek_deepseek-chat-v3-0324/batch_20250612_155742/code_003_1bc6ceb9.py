"""
Generated Code Metadata:
========================
Original URL: https://dcsprayfoamsolutions.com
Prompt: Develop a JavaScript function that dynamically displays customer testimonials for spray foam insulation services on a webpage.
Generated: DETERMINISTIC_1bc6ceb9b8db0566
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * TestimonialSlider - A dynamic testimonial display component for spray foam insulation services.
 * Features:
 * - Rotates testimonials at a set interval
 * - Allows manual navigation
 * - Responsive design
 * - Smooth transitions
 */

class TestimonialSlider {
  /**
   * @param {Object} config - Configuration object
   * @param {string} config.containerSelector - CSS selector for the testimonial container
   * @param {number} [config.rotationInterval=5000] - Time between rotations in ms
   * @param {boolean} [config.autoRotate=true] - Whether to auto-rotate testimonials
   */
  constructor(config) {
    // Validate required configuration
    if (!config || !config.containerSelector) {
      throw new Error('containerSelector is required');
    }

    // Initialize properties
    this.container = document.querySelector(config.containerSelector);
    this.testimonials = [];
    this.currentIndex = 0;
    this.rotationInterval = config.rotationInterval || 5000;
    this.autoRotate = config.autoRotate !== false;
    this.rotationTimer = null;

    // Check if container exists
    if (!this.container) {
      throw new Error(`Container not found with selector: ${config.containerSelector}`);
    }

    // Initialize the slider
    this._initialize();
  }

  /**
   * Initialize the testimonial slider
   * @private
   */
  _initialize() {
    // Gather testimonials from the container
    this.testimonials = Array.from(this.container.querySelectorAll('.testimonial'));
    
    // Check if we have testimonials
    if (this.testimonials.length === 0) {
      console.warn('No testimonials found in container');
      return;
    }

    // Hide all testimonials except the first one
    this.testimonials.forEach((testimonial, index) => {
      testimonial.style.display = index === 0 ? 'block' : 'none';
    });

    // Create navigation controls if more than one testimonial
    if (this.testimonials.length > 1) {
      this._createNavigation();
      if (this.autoRotate) {
        this._startRotation();
      }
    }
  }

  /**
   * Create navigation controls
   * @private
   */
  _createNavigation() {
    const navContainer = document.createElement('div');
    navContainer.className = 'testimonial-nav';

    // Previous button
    const prevButton = document.createElement('button');
    prevButton.className = 'testimonial-nav-prev';
    prevButton.innerHTML = '&lt;';
    prevButton.addEventListener('click', () => this._showPrevious());

    // Next button
    const nextButton = document.createElement('button');
    nextButton.className = 'testimonial-nav-next';
    nextButton.innerHTML = '&gt;';
    nextButton.addEventListener('click', () => this._showNext());

    // Indicator dots
    const dotsContainer = document.createElement('div');
    dotsContainer.className = 'testimonial-dots';

    this.testimonials.forEach((_, index) => {
      const dot = document.createElement('button');
      dot.className = `testimonial-dot ${index === 0 ? 'active' : ''}`;
      dot.addEventListener('click', () => this._showTestimonial(index));
      dotsContainer.appendChild(dot);
    });

    // Assemble navigation
    navContainer.appendChild(prevButton);
    navContainer.appendChild(dotsContainer);
    navContainer.appendChild(nextButton);

    // Add to DOM
    this.container.appendChild(navContainer);
  }

  /**
   * Show the next testimonial
   * @private
   */
  _showNext() {
    this._resetRotationTimer();
    const nextIndex = (this.currentIndex + 1) % this.testimonials.length;
    this._showTestimonial(nextIndex);
  }

  /**
   * Show the previous testimonial
   * @private
   */
  _showPrevious() {
    this._resetRotationTimer();
    const prevIndex = (this.currentIndex - 1 + this.testimonials.length) % this.testimonials.length;
    this._showTestimonial(prevIndex);
  }

  /**
   * Show testimonial at specific index
   * @param {number} index - Index of testimonial to show
   * @private
   */
  _showTestimonial(index) {
    // Validate index
    if (index < 0 || index >= this.testimonials.length) {
      console.error('Invalid testimonial index');
      return;
    }

    // Hide current testimonial
    this.testimonials[this.currentIndex].style.display = 'none';
    
    // Show new testimonial
    this.testimonials[index].style.display = 'block';
    this.currentIndex = index;

    // Update active dot
    const dots = this.container.querySelectorAll('.testimonial-dot');
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === index);
    });
  }

  /**
   * Start auto-rotation of testimonials
   * @private
   */
  _startRotation() {
    this.rotationTimer = setInterval(() => this._showNext(), this.rotationInterval);
  }

  /**
   * Reset the rotation timer
   * @private
   */
  _resetRotationTimer() {
    if (this.autoRotate) {
      clearInterval(this.rotationTimer);
      this._startRotation();
    }
  }

  /**
   * Destroy the testimonial slider and clean up
   */
  destroy() {
    if (this.rotationTimer) {
      clearInterval(this.rotationTimer);
    }
    
    const nav = this.container.querySelector('.testimonial-nav');
    if (nav) {
      this.container.removeChild(nav);
    }
  }
}

// Example usage:
// document.addEventListener('DOMContentLoaded', () => {
//   const testimonialSlider = new TestimonialSlider({
//     containerSelector: '#testimonials-container',
//     rotationInterval: 7000,
//     autoRotate: true
//   });
// });
```
