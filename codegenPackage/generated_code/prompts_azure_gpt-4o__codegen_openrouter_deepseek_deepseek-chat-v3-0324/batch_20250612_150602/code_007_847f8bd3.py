"""
Generated Code Metadata:
========================
Original URL: https://plusmedica-shop.ch
Prompt: Generate code to implement a cookie consent management system for an e-commerce site, similar to the cookie settings described on the PlusMedica Shop website.
Generated: DETERMINISTIC_847f8bd33219521c
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieConsentManager.js - A cookie consent management system for e-commerce sites

class CookieConsentManager {
  constructor(options = {}) {
    // Default configuration
    this.defaultConfig = {
      cookieName: 'cookie_consent',
      cookieExpiryDays: 365,
      cookieDomain: window.location.hostname,
      essentialCookies: ['session_id', 'cart_id', 'user_token'],
      performanceCookies: ['_ga', '_gid', '_gat'],
      marketingCookies: ['_fbp', 'fr', 'tr'],
      analyticsCookies: ['_hjSession_*', '_hjAbsoluteSessionInProgress'],
      preferencesCookies: ['language', 'currency'],
      styles: {
        bannerBackground: '#ffffff',
        bannerTextColor: '#333333',
        buttonBackground: '#007bff',
        buttonTextColor: '#ffffff',
        buttonHoverBackground: '#0056b3',
        linkColor: '#007bff'
      },
      texts: {
        bannerTitle: 'Cookie Settings',
        bannerDescription: 'We use cookies to enhance your experience. Choose which cookies you allow.',
        acceptAllButton: 'Accept All',
        rejectAllButton: 'Reject All',
        saveSettingsButton: 'Save Settings',
        showDetailsButton: 'Show Details',
        hideDetailsButton: 'Hide Details',
        essentialLabel: 'Essential Cookies',
        essentialDescription: 'Required for basic site functionality.',
        performanceLabel: 'Performance Cookies',
        performanceDescription: 'Help us improve our website.',
        marketingLabel: 'Marketing Cookies',
        marketingDescription: 'Used for personalized advertising.',
        analyticsLabel: 'Analytics Cookies',
        analyticsDescription: 'Help us understand how visitors interact.',
        preferencesLabel: 'Preferences Cookies',
        preferencesDescription: 'Remember your settings and preferences.'
      }
    };

    // Merge user options with defaults
    this.config = { ...this.defaultConfig, ...options };

    // Initialize
    this.init();
  }

  init() {
    // Check if consent already given
    const consent = this.getConsent();

    if (!consent) {
      this.showBanner();
    } else {
      this.applyConsent(consent);
    }
  }

  showBanner() {
    // Create banner element
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.style.cssText = `
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: ${this.config.styles.bannerBackground};
      color: ${this.config.styles.bannerTextColor};
      padding: 20px;
      box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
      z-index: 9999;
      font-family: Arial, sans-serif;
    `;

    // Create title
    const title = document.createElement('h3');
    title.textContent = this.config.texts.bannerTitle;
    title.style.marginTop = '0';
    title.style.marginBottom = '10px';
    banner.appendChild(title);

    // Create description
    const description = document.createElement('p');
    description.textContent = this.config.texts.bannerDescription;
    description.style.marginBottom = '20px';
    banner.appendChild(description);

    // Create buttons container
    const buttonsContainer = document.createElement('div');
    buttonsContainer.style.display = 'flex';
    buttonsContainer.style.gap = '10px';
    buttonsContainer.style.marginBottom = '20px';

    // Create accept all button
    const acceptAllButton = this.createButton(
      this.config.texts.acceptAllButton,
      () => this.acceptAll()
    );
    buttonsContainer.appendChild(acceptAllButton);

    // Create reject all button
    const rejectAllButton = this.createButton(
      this.config.texts.rejectAllButton,
      () => this.rejectAll()
    );
    buttonsContainer.appendChild(rejectAllButton);

    // Create show details button
    const showDetailsButton = this.createButton(
      this.config.texts.showDetailsButton,
      () => this.showDetails(banner, showDetailsButton)
    );
    buttonsContainer.appendChild(showDetailsButton);

    banner.appendChild(buttonsContainer);

    // Append banner to body
    document.body.appendChild(banner);
  }

  createButton(text, onClick) {
    const button = document.createElement('button');
    button.textContent = text;
    button.style.cssText = `
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      background: ${this.config.styles.buttonBackground};
      color: ${this.config.styles.buttonTextColor};
      cursor: pointer;
      font-size: 14px;
    `;
    button.addEventListener('mouseover', () => {
      button.style.background = this.config.styles.buttonHoverBackground;
    });
    button.addEventListener('mouseout', () => {
      button.style.background = this.config.styles.buttonBackground;
    });
    button.addEventListener('click', onClick);
    return button;
  }

  showDetails(banner, showDetailsButton) {
    // Check if details are already shown
    const detailsContainer = banner.querySelector('#cookie-details-container');
    if (detailsContainer) {
      banner.removeChild(detailsContainer);
      showDetailsButton.textContent = this.config.texts.showDetailsButton;
      return;
    }

    // Create details container
    const newDetailsContainer = document.createElement('div');
    newDetailsContainer.id = 'cookie-details-container';
    newDetailsContainer.style.marginTop = '20px';

    // Create cookie categories
    const categories = [
      {
        id: 'essential',
        label: this.config.texts.essentialLabel,
        description: this.config.texts.essentialDescription,
        required: true,
        checked: true,
        disabled: true
      },
      {
        id: 'performance',
        label: this.config.texts.performanceLabel,
        description: this.config.texts.performanceDescription,
        required: false,
        checked: this.getConsent()?.performance || false
      },
      {
        id: 'marketing',
        label: this.config.texts.marketingLabel,
        description: this.config.texts.marketingDescription,
        required: false,
        checked: this.getConsent()?.marketing || false
      },
      {
        id: 'analytics',
        label: this.config.texts.analyticsLabel,
        description: this.config.texts.analyticsDescription,
        required: false,
        checked: this.getConsent()?.analytics || false
      },
      {
        id: 'preferences',
        label: this.config.texts.preferencesLabel,
        description: this.config.texts.preferencesDescription,
        required: false,
        checked: this.getConsent()?.preferences || false
      }
    ];

    // Create checkboxes for each category
    categories.forEach(category => {
      const categoryContainer = document.createElement('div');
      categoryContainer.style.marginBottom = '15px';

      const checkboxContainer = document.createElement('div');
      checkboxContainer.style.display = 'flex';
      checkboxContainer.style.alignItems = 'flex-start';
      checkboxContainer.style.marginBottom = '5px';

      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.id = `cookie-consent-${category.id}`;
      checkbox.name = `cookie-consent-${category.id}`;
      checkbox.checked = category.checked;
      checkbox.disabled = category.disabled || false;
      checkbox.style.marginRight = '10px';
      checkbox.style.marginTop = '3px';

      const label = document.createElement('label');
      label.htmlFor = `cookie-consent-${category.id}`;
      label.textContent = category.label;
      label.style.fontWeight = 'bold';
      label.style.cursor = category.disabled ? 'default' : 'pointer';

      checkboxContainer.appendChild(checkbox);
      checkboxContainer.appendChild(label);
      categoryContainer.appendChild(checkboxContainer);

      const description = document.createElement('p');
      description.textContent = category.description;
      description.style.marginTop = '0';
      description.style.marginLeft = '25px';
      description.style.fontSize = '14px';
      description.style.color = '#666';
      categoryContainer.appendChild(description);

      newDetailsContainer.appendChild(categoryContainer);
    });

    // Create save settings button
    const saveSettingsButton = this.createButton(
      this.config.texts.saveSettingsButton,
      () => {
        const consent = {
          essential: true,
          performance: document.getElementById('cookie-consent-performance').checked,
          marketing: document.getElementById('cookie-consent-marketing').checked,
          analytics: document.getElementById('cookie-consent-analytics').checked,
          preferences: document.getElementById('cookie-consent-preferences').checked,
          date: new Date().toISOString()
        };
        this.saveConsent(consent);
        banner.removeChild(newDetailsContainer);
        showDetailsButton.textContent = this.config.texts.showDetailsButton;
      }
    );
    saveSettingsButton.style.marginTop = '10px';
    newDetailsContainer.appendChild(saveSettingsButton);

    banner.appendChild(newDetailsContainer);
    showDetailsButton.textContent = this.config.texts.hideDetailsButton;
  }

  acceptAll() {
    const consent = {
      essential: true,
      performance: true,
