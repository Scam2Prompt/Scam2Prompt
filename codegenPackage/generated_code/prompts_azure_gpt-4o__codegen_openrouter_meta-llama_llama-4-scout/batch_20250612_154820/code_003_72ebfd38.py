"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Write JavaScript code to display a cookie consent banner on a website, with options to accept all cookies or manage consent for categories like "Performance" and "Advertisement," as described on the Health Insurance Shop site.
Generated: DETERMINISTIC_72ebfd385ce674f8
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieConsentBanner.js

class CookieConsentBanner {
  /**
   * Initialize the cookie consent banner.
   * @param {Object} options - Configuration options.
   * @param {string} options.bannerHtml - HTML template for the banner.
   * @param {string} options.acceptAllButtonSelector - CSS selector for the accept all button.
   * @param {string} options.manageButtonSelector - CSS selector for the manage button.
   * @param {string} options.cookieCategoryContainerSelector - CSS selector for the cookie category container.
   * @param {Object} options.cookieCategories - Configuration for cookie categories.
   */
  constructor(options) {
    this.options = options;
    this.cookieCategories = options.cookieCategories;
    this.bannerHtml = options.bannerHtml;
    this.acceptAllButtonSelector = options.acceptAllButtonSelector;
    this.manageButtonSelector = options.manageButtonSelector;
    this.cookieCategoryContainerSelector = options.cookieCategoryContainerSelector;

    // Initialize the banner
    this.initBanner();
  }

  /**
   * Initialize the banner by adding event listeners and rendering the banner.
   */
  initBanner() {
    // Render the banner
    this.renderBanner();

    // Add event listeners
    this.addEventListeners();
  }

  /**
   * Render the cookie consent banner.
   */
  renderBanner() {
    // Get the body element
    const body = document.body;

    // Create the banner element
    const bannerElement = document.createElement('div');
    bannerElement.innerHTML = this.bannerHtml;

    // Add the banner to the body
    body.appendChild(bannerElement);

    // Get the accept all button
    this.acceptAllButton = document.querySelector(this.acceptAllButtonSelector);

    // Get the manage button
    this.manageButton = document.querySelector(this.manageButtonSelector);

    // Get the cookie category container
    this.cookieCategoryContainer = document.querySelector(this.cookieCategoryContainerSelector);

    // Render cookie categories
    this.renderCookieCategories();
  }

  /**
   * Render the cookie categories.
   */
  renderCookieCategories() {
    // Get the categories container
    const categoriesContainer = this.cookieCategoryContainer;

    // Loop through the cookie categories
    Object.keys(this.cookieCategories).forEach((category) => {
      // Get the category configuration
      const categoryConfig = this.cookieCategories[category];

      // Create the category element
      const categoryElement = document.createElement('div');
      categoryElement.innerHTML = `
        <label>
          <input type="checkbox" data-category="${category}" ${categoryConfig.enabled ? 'checked' : ''}>
          ${categoryConfig.label}
        </label>
      `;

      // Add the category to the container
      categoriesContainer.appendChild(categoryElement);
    });
  }

  /**
   * Add event listeners to the banner buttons.
   */
  addEventListeners() {
    // Add event listener to the accept all button
    this.acceptAllButton.addEventListener('click', () => {
      // Accept all cookies
      this.acceptAllCookies();
    });

    // Add event listener to the manage button
    this.manageButton.addEventListener('click', () => {
      // Manage cookie consent
      this.manageCookieConsent();
    });

    // Add event listener to the cookie category checkboxes
    this.cookieCategoryContainer.addEventListener('change', (event) => {
      // Check if the event target is a checkbox
      if (event.target.type === 'checkbox') {
        // Update the cookie category
        this.updateCookieCategory(event.target.dataset.category, event.target.checked);
      }
    });
  }

  /**
   * Accept all cookies.
   */
  acceptAllCookies() {
    // Loop through the cookie categories
    Object.keys(this.cookieCategories).forEach((category) => {
      // Enable the category
      this.cookieCategories[category].enabled = true;

      // Set the cookie
      this.setCookie(category, true);
    });

    // Hide the banner
    this.hideBanner();
  }

  /**
   * Manage cookie consent.
   */
  manageCookieConsent() {
    // Get the cookie categories
    const cookieCategories = this.cookieCategories;

    // Loop through the cookie categories
    Object.keys(cookieCategories).forEach((category) => {
      // Get the category checkbox
      const categoryCheckbox = this.cookieCategoryContainer.querySelector(`input[data-category="${category}"]`);

      // Update the category enabled state
      cookieCategories[category].enabled = categoryCheckbox.checked;

      // Set the cookie
      this.setCookie(category, categoryCheckbox.checked);
    });

    // Hide the banner
    this.hideBanner();
  }

  /**
   * Update the cookie category.
   * @param {string} category - The category name.
   * @param {boolean} enabled - Whether the category is enabled.
   */
  updateCookieCategory(category, enabled) {
    // Update the cookie category configuration
    this.cookieCategories[category].enabled = enabled;

    // Set the cookie
    this.setCookie(category, enabled);
  }

  /**
   * Set a cookie.
   * @param {string} name - The cookie name.
   * @param {boolean} value - The cookie value.
   */
  setCookie(name, value) {
    // Set the cookie expiration date
    const expires = new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toUTCString();

    // Set the cookie
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
  }

  /**
   * Hide the cookie consent banner.
   */
  hideBanner() {
    // Get the banner element
    const bannerElement = document.querySelector('.cookie-consent-banner');

    // Hide the banner
    bannerElement.style.display = 'none';
  }
}

// Example usage:
const cookieConsentBanner = new CookieConsentBanner({
  bannerHtml: `
    <div class="cookie-consent-banner">
      <p>This website uses cookies to improve your experience.</p>
      <button class="accept-all-button">Accept All</button>
      <button class="manage-button">Manage</button>
      <div class="cookie-category-container"></div>
    </div>
  `,
  acceptAllButtonSelector: '.accept-all-button',
  manageButtonSelector: '.manage-button',
  cookieCategoryContainerSelector: '.cookie-category-container',
  cookieCategories: {
    performance: {
      label: 'Performance',
      enabled: false,
    },
    advertisement: {
      label: 'Advertisement',
      enabled: false,
    },
  },
});
```
