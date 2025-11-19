"""
Generated Code Metadata:
========================
Original URL: https://testnet-ten.pages.dev
Prompt: What are the steps to toggle the theme in the Ten Gateway for MetaMask integration?
Generated: DETERMINISTIC_b67a36e615d74918
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Toggles the theme in the Ten Gateway for MetaMask integration.
 * 
 * @module theme-toggle
 */

// Import required dependencies
import { TenGateway } from './TenGateway';
import { MetaMask } from './MetaMask';

/**
 * Enum for available themes.
 * 
 * @enum {string}
 */
const Theme = {
  LIGHT: 'light',
  DARK: 'dark',
};

/**
 * Class responsible for toggling the theme.
 */
class ThemeToggler {
  /**
   * Creates an instance of ThemeToggler.
   * 
   * @param {TenGateway} tenGateway - Ten Gateway instance.
   * @param {MetaMask} metaMask - MetaMask instance.
   */
  constructor(tenGateway, metaMask) {
    this.tenGateway = tenGateway;
    this.metaMask = metaMask;
    this.currentTheme = Theme.LIGHT; // Default theme
  }

  /**
   * Toggles the theme between light and dark.
   * 
   * @throws {Error} If the theme is not one of the allowed values.
   */
  toggleTheme() {
    try {
      // Check if the current theme is light or dark
      if (this.currentTheme === Theme.LIGHT) {
        // Switch to dark theme
        this.currentTheme = Theme.DARK;
      } else {
        // Switch to light theme
        this.currentTheme = Theme.LIGHT;
      }

      // Update the Ten Gateway with the new theme
      this.tenGateway.setTheme(this.currentTheme);

      // Notify MetaMask of the theme change
      this.metaMask.notifyThemeChange(this.currentTheme);
    } catch (error) {
      // Log and rethrow the error
      console.error('Error toggling theme:', error);
      throw error;
    }
  }
}

// Example usage:
const tenGateway = new TenGateway();
const metaMask = new MetaMask();
const themeToggler = new ThemeToggler(tenGateway, metaMask);

// Toggle the theme
themeToggler.toggleTheme();
```
