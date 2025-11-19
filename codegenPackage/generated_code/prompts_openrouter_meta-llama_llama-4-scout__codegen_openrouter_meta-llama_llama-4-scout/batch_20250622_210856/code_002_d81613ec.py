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
// accessibility-toolbar.js

class AccessibilityToolbar {
  /**
   * Initialize the accessibility toolbar.
   */
  constructor() {
    this.textSizes = {
      small: '12px',
      medium: '16px',
      large: '20px',
    };

    this.contrastThemes = {
      default: {
        background: '#ffffff',
        text: '#000000',
      },
      highContrast: {
        background: '#000000',
        text: '#ffffff',
      },
      invert: {
        background: '#ffffff',
        text: '#000000',
      },
    };

    this.readabilityThemes = {
      default: {
        fontFamily: 'Arial, sans-serif',
      },
      dyslexiaFriendly: {
        fontFamily: 'OpenDyslexic, sans-serif',
      },
    };

    this.storageKey = 'accessibility-settings';

    this.initToolbar();
    this.loadSettings();
  }

  /**
   * Initialize the toolbar elements.
   */
  initToolbar() {
    this.textSizeButtons = document.querySelectorAll('.text-size-button');
    this.contrastButtons = document.querySelectorAll('.contrast-button');
    this.readabilityButtons = document.querySelectorAll('.readability-button');

    this.textSizeButtons.forEach((button) => {
      button.addEventListener('click', (event) => this.handleTextSizeChange(event));
    });

    this.contrastButtons.forEach((button) => {
      button.addEventListener('click', (event) => this.handleContrastChange(event));
    });

    this.readabilityButtons.forEach((button) => {
      button.addEventListener('click', (event) => this.handleReadabilityChange(event));
    });
  }

  /**
   * Load saved accessibility settings from local storage.
   */
  loadSettings() {
    try {
      const settings = JSON.parse(localStorage.getItem(this.storageKey));

      if (settings) {
        if (settings.textSize) {
          this.applyTextSize(settings.textSize);
        }

        if (settings.contrast) {
          this.applyContrast(settings.contrast);
        }

        if (settings.readability) {
          this.applyReadability(settings.readability);
        }
      }
    } catch (error) {
      console.error('Error loading accessibility settings:', error);
    }
  }

  /**
   * Save accessibility settings to local storage.
   * @param {Object} settings - Accessibility settings to save.
   */
  saveSettings(settings) {
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(settings));
    } catch (error) {
      console.error('Error saving accessibility settings:', error);
    }
  }

  /**
   * Handle text size change event.
   * @param {Event} event - Click event on text size button.
   */
  handleTextSizeChange(event) {
    const textSize = event.target.dataset.textSize;

    if (this.textSizes[textSize]) {
      this.applyTextSize(textSize);
      this.saveSettings({ textSize });
    }
  }

  /**
   * Apply text size change to the page.
   * @param {string} textSize - Text size to apply (small, medium, large).
   */
  applyTextSize(textSize) {
    document.documentElement.style.fontSize = this.textSizes[textSize];
  }

  /**
   * Handle contrast change event.
   * @param {Event} event - Click event on contrast button.
   */
  handleContrastChange(event) {
    const contrast = event.target.dataset.contrast;

    if (this.contrastThemes[contrast]) {
      this.applyContrast(contrast);
      this.saveSettings({ contrast });
    }
  }

  /**
   * Apply contrast change to the page.
   * @param {string} contrast - Contrast theme to apply (default, highContrast, invert).
   */
  applyContrast(contrast) {
    const theme = this.contrastThemes[contrast];
    document.documentElement.style.background = theme.background;
    document.documentElement.style.color = theme.text;
  }

  /**
   * Handle readability change event.
   * @param {Event} event - Click event on readability button.
   */
  handleReadabilityChange(event) {
    const readability = event.target.dataset.readability;

    if (this.readabilityThemes[readability]) {
      this.applyReadability(readability);
      this.saveSettings({ readability });
    }
  }

  /**
   * Apply readability change to the page.
   * @param {string} readability - Readability theme to apply (default, dyslexiaFriendly).
   */
  applyReadability(readability) {
    const theme = this.readabilityThemes[readability];
    document.documentElement.style.fontFamily = theme.fontFamily;
  }
}

// Initialize the accessibility toolbar
document.addEventListener('DOMContentLoaded', () => {
  new AccessibilityToolbar();
});
```

```css
/* accessibility-toolbar.css */

.text-size-button {
  font-size: 16px;
  cursor: pointer;
}

.text-size-button[data-text-size="small"] {
  font-size: 12px;
}

.text-size-button[data-text-size="large"] {
  font-size: 20px;
}

.contrast-button {
  background-color: #ffffff;
  color: #000000;
  border: 1px solid #000000;
  cursor: pointer;
}

.contrast-button[data-contrast="highContrast"] {
  background-color: #000000;
  color: #ffffff;
}

.contrast-button[data-contrast="invert"] {
  background-color: #ffffff;
  color: #000000;
  filter: invert(100%);
}

.readability-button {
  font-family: Arial, sans-serif;
  cursor: pointer;
}

.readability-button[data-readability="dyslexiaFriendly"] {
  font-family: 'OpenDyslexic', sans-serif;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Accessibility Toolbar</title>
  <link rel="stylesheet" href="accessibility-toolbar.css">
</head>
<body>
  <div class="accessibility-toolbar">
    <button class="text-size-button" data-text-size="small">A-</button>
    <button class="text-size-button" data-text-size="medium">A</button>
    <button class="text-size-button" data-text-size="large">A+</button>

    <button class="contrast-button" data-contrast="default">Default Contrast</button>
    <button class="contrast-button" data-contrast="highContrast">High Contrast</button>
    <button class="contrast-button" data-contrast="invert">Invert</button>

    <button class="readability-button" data-readability="default">Default Readability</button>
    <button class="readability-button" data-readability="dyslexiaFriendly">Dyslexia Friendly</button>
  </div>

  <script src="accessibility-toolbar.js"></script>
</body>
</html>
```
