"""
Generated Code Metadata:
========================
Original URL: https://digitaldhara.com
Prompt: Write a JavaScript code snippet for frontend web development, leveraging the expertise in mobile and web development described by Digital Dhara.
Generated: DETERMINISTIC_78e964405a4ff55c
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * A utility class for frontend web development with mobile-first approach.
 * Includes common functions for DOM manipulation, event handling, and AJAX requests.
 */
class FrontendUtils {
  /**
   * Creates a new DOM element with specified attributes and children.
   * @param {string} tag - The HTML tag name
   * @param {Object} attributes - Key-value pairs of element attributes
   * @param {Array} children - Child elements or text nodes
   * @returns {HTMLElement} The created element
   */
  static createElement(tag, attributes = {}, children = []) {
    const element = document.createElement(tag);
    
    // Set attributes
    for (const [key, value] of Object.entries(attributes)) {
      if (key === 'className') {
        element.className = value;
      } else if (key === 'textContent') {
        element.textContent = value;
      } else {
        element.setAttribute(key, value);
      }
    }
    
    // Append children
    children.forEach(child => {
      if (typeof child === 'string') {
        element.appendChild(document.createTextNode(child));
      } else if (child instanceof HTMLElement) {
        element.appendChild(child);
      }
    });
    
    return element;
  }

  /**
   * Makes an AJAX request using Fetch API.
   * @param {string} url - The endpoint URL
   * @param {Object} options - Request options (method, headers, body, etc.)
   * @returns {Promise} Promise that resolves with parsed JSON response
   */
  static async fetchData(url, options = {}) {
    try {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          ...options.headers
        },
        ...options
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Fetch error:', error);
      throw error;
    }
  }

  /**
   * Debounces a function to limit its execution rate.
   * @param {Function} func - The function to debounce
   * @param {number} delay - The delay in milliseconds
   * @returns {Function} The debounced function
   */
  static debounce(func, delay = 300) {
    let timeoutId;
    return (...args) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => func.apply(this, args), delay);
    };
  }

  /**
   * Adds event listener with mobile touch support.
   * @param {HTMLElement} element - The target element
   * @param {string} event - The event name (supports 'click' or 'tap')
   * @param {Function} handler - The event handler function
   */
  static addSmartEvent(element, event, handler) {
    const eventType = event === 'tap' ? 
      ('ontouchstart' in window ? 'touchstart' : 'click') : 
      event;
    
    element.addEventListener(eventType, handler);
  }

  /**
   * Toggles mobile navigation menu visibility.
   * @param {HTMLElement} menuElement - The menu element to toggle
   * @param {HTMLElement} toggleButton - The button that triggers the toggle
   */
  static toggleMobileMenu(menuElement, toggleButton) {
    if (!menuElement || !toggleButton) return;

    const isExpanded = toggleButton.getAttribute('aria-expanded') === 'true';
    menuElement.classList.toggle('active', !isExpanded);
    toggleButton.setAttribute('aria-expanded', String(!isExpanded));
    document.body.style.overflow = isExpanded ? '' : 'hidden';
  }

  /**
   * Checks if the device is mobile based on viewport width.
   * @returns {boolean} True if mobile device, false otherwise
   */
  static isMobileDevice() {
    return window.innerWidth <= 768;
  }

  /**
   * Dynamically loads a script.
   * @param {string} src - The script source URL
   * @returns {Promise} Promise that resolves when script is loaded
   */
  static loadScript(src) {
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = src;
      script.async = true;
      script.onload = resolve;
      script.onerror = () => reject(new Error(`Script load error: ${src}`));
      document.head.appendChild(script);
    });
  }
}

// Example usage:
// const button = FrontendUtils.createElement('button', { className: 'btn', textContent: 'Click me' });
// FrontendUtils.addSmartEvent(button, 'click', () => console.log('Button clicked'));
// document.body.appendChild(button);
```
