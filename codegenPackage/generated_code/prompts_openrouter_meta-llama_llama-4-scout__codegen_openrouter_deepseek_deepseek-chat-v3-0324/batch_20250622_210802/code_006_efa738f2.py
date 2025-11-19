"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: What is an efficient way to categorize and manage different types of cookies (necessary, functional, analytics, advertisement) on a website, and how can this be implemented in code?
Generated: DETERMINISTIC_efa738f26ee857b3
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieManager.js - A class to handle cookie categorization and management

class CookieManager {
  constructor() {
    this.cookieCategories = {
      necessary: {
        enabled: true, // Necessary cookies cannot be disabled
        name: 'necessary',
        description: 'Essential cookies for website functionality'
      },
      functional: {
        enabled: false,
        name: 'functional',
        description: 'Cookies that enhance user experience'
      },
      analytics: {
        enabled: false,
        name: 'analytics',
        description: 'Cookies for website analytics'
      },
      advertisement: {
        enabled: false,
        name: 'advertisement',
        description: 'Cookies for personalized ads'
      }
    };
    this.consentCookieName = 'cookie_consent';
    this.loadConsent();
  }

  // Load saved consent preferences from cookie
  loadConsent() {
    try {
      const consentData = this.getCookie(this.consentCookieName);
      if (consentData) {
        const parsedData = JSON.parse(consentData);
        for (const category in parsedData) {
          if (this.cookieCategories[category] && category !== 'necessary') {
            this.cookieCategories[category].enabled = parsedData[category];
          }
        }
      }
    } catch (error) {
      console.error('Error loading cookie consent:', error);
    }
  }

  // Save current consent preferences to cookie
  saveConsent() {
    try {
      const consentData = {};
      for (const category in this.cookieCategories) {
        consentData[category] = this.cookieCategories[category].enabled;
      }
      const expiryDate = new Date();
      expiryDate.setFullYear(expiryDate.getFullYear() + 1);
      
      document.cookie = `${this.consentCookieName}=${JSON.stringify(consentData)}; expires=${expiryDate.toUTCString()}; path=/; SameSite=Lax`;
    } catch (error) {
      console.error('Error saving cookie consent:', error);
    }
  }

  // Set a cookie with proper category checking
  setCookie(name, value, days, category) {
    try {
      if (!this.isCategoryEnabled(category)) {
        console.warn(`Cannot set cookie ${name} - category ${category} is disabled`);
        return false;
      }

      let expires = '';
      if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = '; expires=' + date.toUTCString();
      }
      
      document.cookie = `${name}=${value}${expires}; path=/; SameSite=Lax`;
      return true;
    } catch (error) {
      console.error(`Error setting cookie ${name}:`, error);
      return false;
    }
  }

  // Get cookie value by name
  getCookie(name) {
    try {
      const nameEQ = name + '=';
      const ca = document.cookie.split(';');
      for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length);
      }
      return null;
    } catch (error) {
      console.error(`Error getting cookie ${name}:`, error);
      return null;
    }
  }

  // Delete cookie by name
  deleteCookie(name) {
    try {
      document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    } catch (error) {
      console.error(`Error deleting cookie ${name}:`, error);
    }
  }

  // Check if a cookie category is enabled
  isCategoryEnabled(category) {
    if (!this.cookieCategories[category]) {
      console.warn(`Unknown cookie category: ${category}`);
      return false;
    }
    return this.cookieCategories[category].enabled;
  }

  // Set category enabled state
  setCategoryEnabled(category, enabled) {
    if (category === 'necessary') {
      console.warn('Cannot disable necessary cookies');
      return false;
    }

    if (!this.cookieCategories[category]) {
      console.warn(`Unknown cookie category: ${category}`);
      return false;
    }

    this.cookieCategories[category].enabled = enabled;
    this.saveConsent();
    return true;
  }

  // Get all categories with their current state
  getCategories() {
    return JSON.parse(JSON.stringify(this.cookieCategories));
  }
}

// Example usage:
// const cookieManager = new CookieManager();
// cookieManager.setCookie('user_preference', 'dark_mode', 30, 'functional');
// cookieManager.setCategoryEnabled('analytics', true);
```
