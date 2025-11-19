"""
Generated Code Metadata:
========================
Original URL: https://blur.si
Prompt: "Generate JavaScript code to conditionally enable or disable blur effects on webpage elements, similar to blur.si's approach."
Generated: DETERMINISTIC_2ccd951830b359d6
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * BlurEffectManager - A utility to conditionally enable/disable blur effects on webpage elements.
 * Inspired by blur.si's approach.
 */
class BlurEffectManager {
  /**
   * @param {Object} options - Configuration options
   * @param {string} options.blurClass - CSS class to apply blur effect
   * @param {string} options.blurIntensity - CSS blur value (e.g., '5px')
   * @param {boolean} options.enableOnLoad - Whether to enable blur on load
   * @param {string} options.storageKey - Key for localStorage persistence
   */
  constructor(options = {}) {
    this.config = {
      blurClass: options.blurClass || 'blur-effect',
      blurIntensity: options.blurIntensity || '5px',
      enableOnLoad: options.enableOnLoad ?? true,
      storageKey: options.storageKey || 'blurEffectEnabled',
      ...options
    };

    this.isEnabled = this.config.enableOnLoad;
    this.loadState();
    this.initStyles();
  }

  /**
   * Initialize necessary styles in the document head
   */
  initStyles() {
    if (!document.getElementById('blur-effect-styles')) {
      const style = document.createElement('style');
      style.id = 'blur-effect-styles';
      style.textContent = `
        .${this.config.blurClass} {
          filter: blur(${this.config.blurIntensity});
          transition: filter 0.3s ease;
        }
        .${this.config.blurClass}-disabled {
          filter: none !important;
        }
      `;
      document.head.appendChild(style);
    }
  }

  /**
   * Load blur state from localStorage
   */
  loadState() {
    try {
      const savedState = localStorage.getItem(this.config.storageKey);
      if (savedState !== null) {
        this.isEnabled = savedState === 'true';
      }
    } catch (e) {
      console.error('Failed to load blur state:', e);
    }
  }

  /**
   * Save current blur state to localStorage
   */
  saveState() {
    try {
      localStorage.setItem(this.config.storageKey, this.isEnabled.toString());
    } catch (e) {
      console.error('Failed to save blur state:', e);
    }
  }

  /**
   * Toggle blur effect on elements with the specified class
   * @param {boolean} [state] - Optional state to set (true/false)
   */
  toggleBlur(state) {
    this.isEnabled = typeof state === 'boolean' ? state : !this.isEnabled;
    
    const elements = document.querySelectorAll(`.${this.config.blurClass}`);
    elements.forEach(el => {
      if (this.isEnabled) {
        el.classList.remove(`${this.config.blurClass}-disabled`);
      } else {
        el.classList.add(`${this.config.blurClass}-disabled`);
      }
    });

    this.saveState();
    return this.isEnabled;
  }

  /**
   * Apply blur effect to specific elements
   * @param {string|Element|NodeList} elements - Selector, element or NodeList to apply blur to
   */
  applyToElements(elements) {
    let targetElements;
    
    if (typeof elements === 'string') {
      targetElements = document.querySelectorAll(elements);
    } else if (elements instanceof NodeList || Array.isArray(elements)) {
      targetElements = elements;
    } else if (elements instanceof Element) {
      targetElements = [elements];
    } else {
      throw new Error('Invalid elements parameter');
    }

    targetElements.forEach(el => {
      el.classList.add(this.config.blurClass);
      if (!this.isEnabled) {
        el.classList.add(`${this.config.blurClass}-disabled`);
      }
    });
  }
}

// Example usage:
// const blurManager = new BlurEffectManager({
//   blurClass: 'custom-blur',
//   blurIntensity: '8px',
//   enableOnLoad: false
// });
// blurManager.applyToElements('.sensitive-content');
// document.getElementById('toggleBtn').addEventListener('click', () => blurManager.toggleBlur());
```
