"""
Generated Code Metadata:
========================
Original URL: https://debnicakaszubska.eu
Prompt: Generate a code snippet in JavaScript to implement an accessibility feature similar to the "Dostosuj stronę www" (Adjust the website) toolbar on the Gmina Dębnica Kaszubska website, allowing users to customize text size, contrast, and readability.
Generated: DETERMINISTIC_d81613ec9358870b
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Accessibility Toolbar for Website Customization
 * Features:
 * - Adjust text size
 * - Toggle high contrast mode
 * - Improve readability (line height and letter spacing)
 */

class AccessibilityToolbar {
  constructor() {
    this.textSize = 1; // Default text size multiplier
    this.highContrast = false;
    this.readabilityMode = false;
    this.storageKey = 'accessibilitySettings';
    this.init();
  }

  /**
   * Initialize the toolbar and load saved settings
   */
  init() {
    this.loadSettings();
    this.createToolbar();
    this.applySettings();
    this.setupEventListeners();
  }

  /**
   * Create the toolbar DOM elements
   */
  createToolbar() {
    const toolbar = document.createElement('div');
    toolbar.className = 'accessibility-toolbar';
    toolbar.setAttribute('role', 'toolbar');
    toolbar.setAttribute('aria-label', 'Accessibility Options');

    toolbar.innerHTML = `
      <div class="toolbar-section">
        <button class="toolbar-btn" id="decreaseText" aria-label="Decrease text size">A-</button>
        <span class="toolbar-label" aria-hidden="true">Text Size</span>
        <button class="toolbar-btn" id="increaseText" aria-label="Increase text size">A+</button>
      </div>
      <div class="toolbar-section">
        <button class="toolbar-btn" id="toggleContrast" aria-label="Toggle high contrast mode">
          High Contrast
        </button>
      </div>
      <div class="toolbar-section">
        <button class="toolbar-btn" id="toggleReadability" aria-label="Toggle readability mode">
          Readability
        </button>
      </div>
      <div class="toolbar-section">
        <button class="toolbar-btn" id="resetSettings" aria-label="Reset all settings">
          Reset
        </button>
      </div>
    `;

    document.body.insertBefore(toolbar, document.body.firstChild);
    this.addStyles();
  }

  /**
   * Add necessary CSS styles for the toolbar
   */
  addStyles() {
    const style = document.createElement('style');
    style.textContent = `
      .accessibility-toolbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background: #f5f5f5;
        padding: 10px;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        z-index: 9999;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
      }
      .toolbar-section {
        display: flex;
        align-items: center;
        gap: 5px;
      }
      .toolbar-btn {
        padding: 5px 10px;
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 4px;
        cursor: pointer;
      }
      .toolbar-btn:hover {
        background: #eee;
      }
      .toolbar-label {
        font-size: 14px;
      }
      .high-contrast {
        filter: contrast(120%);
        background-color: #000 !important;
        color: #fff !important;
      }
      .high-contrast * {
        background-color: inherit !important;
        color: inherit !important;
      }
      .readability-mode {
        line-height: 1.6 !important;
        letter-spacing: 0.5px !important;
      }
    `;
    document.head.appendChild(style);
  }

  /**
   * Set up event listeners for toolbar buttons
   */
  setupEventListeners() {
    document.getElementById('increaseText').addEventListener('click', () => {
      this.textSize = Math.min(this.textSize + 0.1, 2.0);
      this.applySettings();
    });

    document.getElementById('decreaseText').addEventListener('click', () => {
      this.textSize = Math.max(this.textSize - 0.1, 0.8);
      this.applySettings();
    });

    document.getElementById('toggleContrast').addEventListener('click', () => {
      this.highContrast = !this.highContrast;
      this.applySettings();
    });

    document.getElementById('toggleReadability').addEventListener('click', () => {
      this.readabilityMode = !this.readabilityMode;
      this.applySettings();
    });

    document.getElementById('resetSettings').addEventListener('click', () => {
      this.textSize = 1;
      this.highContrast = false;
      this.readabilityMode = false;
      this.applySettings();
    });
  }

  /**
   * Apply all current accessibility settings to the page
   */
  applySettings() {
    document.body.style.fontSize = `${this.textSize}rem`;
    
    if (this.highContrast) {
      document.body.classList.add('high-contrast');
    } else {
      document.body.classList.remove('high-contrast');
    }
    
    if (this.readabilityMode) {
      document.body.classList.add('readability-mode');
    } else {
      document.body.classList.remove('readability-mode');
    }

    this.saveSettings();
  }

  /**
   * Save settings to localStorage
   */
  saveSettings() {
    try {
      const settings = {
        textSize: this.textSize,
        highContrast: this.highContrast,
        readabilityMode: this.readabilityMode
      };
      localStorage.setItem(this.storageKey, JSON.stringify(settings));
    } catch (e) {
      console.error('Failed to save accessibility settings:', e);
    }
  }

  /**
   * Load settings from localStorage
   */
  loadSettings() {
    try {
      const settings = localStorage.getItem(this.storageKey);
      if (settings) {
        const parsed = JSON.parse(settings);
        this.textSize = parsed.textSize || 1;
        this.highContrast = parsed.highContrast || false;
        this.readabilityMode = parsed.readabilityMode || false;
      }
    } catch (e) {
      console.error('Failed to load accessibility settings:', e);
    }
  }
}

// Initialize the toolbar when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new AccessibilityToolbar();
});
```
