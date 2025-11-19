"""
Generated Code Metadata:
========================
Original URL: https://celestia.solutions
Prompt: Write a JavaScript function that tracks user consent for cookies, inspired by the cookie policy on celestia.solutions.
Generated: DETERMINISTIC_9b4d0e49e36b00e5
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Consent Manager
 * 
 * This script handles user consent for cookies, allowing users to accept, reject, or customize their cookie preferences.
 * Inspired by celestia.solutions cookie policy.
 */

class CookieConsent {
  /**
   * Initialize the cookie consent manager
   * @param {Object} options - Configuration options
   * @param {string} options.cookieName - Name of the cookie to store consent
   * @param {number} options.cookieExpiryDays - Cookie expiration in days
   * @param {string} options.consentTypes - Cookie types requiring consent
   * @param {boolean} options.autoShowBanner - Whether to automatically show the banner
   */
  constructor(options = {}) {
    this.cookieName = options.cookieName || 'cookie_consent';
    this.cookieExpiryDays = options.cookieExpiryDays || 365;
    this.consentTypes = options.consentTypes || ['necessary', 'analytics', 'marketing'];
    this.autoShowBanner = options.autoShowBanner !== false;
    
    this.consent = this.getConsent();
    
    if (this.autoShowBanner && !this.consent) {
      this.showBanner();
    }
  }

  /**
   * Get current consent status
   * @returns {Object|null} Current consent object or null if not set
   */
  getConsent() {
    try {
      const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith(`${this.cookieName}=`))
        ?.split('=')[1];
      
      return cookieValue ? JSON.parse(decodeURIComponent(cookieValue)) : null;
    } catch (error) {
      console.error('Error parsing cookie consent:', error);
      return null;
    }
  }

  /**
   * Set consent status
   * @param {Object} consent - Consent object
   * @param {boolean} consent.necessary - Necessary cookies consent
   * @param {boolean} consent.analytics - Analytics cookies consent
   * @param {boolean} consent.marketing - Marketing cookies consent
   */
  setConsent(consent) {
    try {
      const date = new Date();
      date.setTime(date.getTime() + (this.cookieExpiryDays * 24 * 60 * 60 * 1000));
      const expires = `expires=${date.toUTCString()}`;
      
      // Ensure necessary cookies are always accepted
      const finalConsent = {
        ...consent,
        necessary: true
      };
      
      document.cookie = `${this.cookieName}=${encodeURIComponent(JSON.stringify(finalConsent))}; ${expires}; path=/; SameSite=Lax`;
      this.consent = finalConsent;
      
      // Trigger consent update event
      this.triggerEvent('consentUpdated', finalConsent);
    } catch (error) {
      console.error('Error setting cookie consent:', error);
    }
  }

  /**
   * Check if consent is given for a specific type
   * @param {string} type - Cookie type to check
   * @returns {boolean} Whether consent is given
   */
  hasConsent(type) {
    if (!this.consent) return false;
    if (type === 'necessary') return true;
    return this.consent[type] === true;
  }

  /**
   * Show consent banner
   */
  showBanner() {
    const banner = document.createElement('div');
    banner.id = 'cookie-consent-banner';
    banner.style.position = 'fixed';
    banner.style.bottom = '0';
    banner.style.left = '0';
    banner.style.right = '0';
    banner.style.padding = '1rem';
    banner.style.backgroundColor = '#f8f9fa';
    banner.style.borderTop = '1px solid #dee2e6';
    banner.style.zIndex = '1000';
    banner.style.display = 'flex';
    banner.style.flexDirection = 'column';
    banner.style.gap = '1rem';
    
    const text = document.createElement('p');
    text.textContent = 'We use cookies to enhance your experience. By continuing to visit this site, you agree to our use of cookies.';
    
    const buttons = document.createElement('div');
    buttons.style.display = 'flex';
    buttons.style.gap = '0.5rem';
    
    const acceptAllBtn = document.createElement('button');
    acceptAllBtn.textContent = 'Accept All';
    acceptAllBtn.addEventListener('click', () => {
      this.acceptAll();
      banner.remove();
    });
    
    const rejectAllBtn = document.createElement('button');
    rejectAllBtn.textContent = 'Reject All';
    rejectAllBtn.addEventListener('click', () => {
      this.rejectAll();
      banner.remove();
    });
    
    const customizeBtn = document.createElement('button');
    customizeBtn.textContent = 'Customize';
    customizeBtn.addEventListener('click', () => {
      this.showPreferencesModal();
      banner.remove();
    });
    
    buttons.appendChild(acceptAllBtn);
    buttons.appendChild(rejectAllBtn);
    buttons.appendChild(customizeBtn);
    
    banner.appendChild(text);
    banner.appendChild(buttons);
    
    document.body.appendChild(banner);
  }

  /**
   * Accept all cookie types
   */
  acceptAll() {
    const consent = {};
    this.consentTypes.forEach(type => {
      consent[type] = true;
    });
    this.setConsent(consent);
  }

  /**
   * Reject all optional cookie types
   */
  rejectAll() {
    const consent = {};
    this.consentTypes.forEach(type => {
      consent[type] = type === 'necessary';
    });
    this.setConsent(consent);
  }

  /**
   * Show preferences modal for granular control
   */
  showPreferencesModal() {
    const modal = document.createElement('div');
    modal.id = 'cookie-consent-modal';
    modal.style.position = 'fixed';
    modal.style.top = '0';
    modal.style.left = '0';
    modal.style.right = '0';
    modal.style.bottom = '0';
    modal.style.backgroundColor = 'rgba(0,0,0,0.5)';
    modal.style.zIndex = '1001';
    modal.style.display = 'flex';
    modal.style.justifyContent = 'center';
    modal.style.alignItems = 'center';
    
    const modalContent = document.createElement('div');
    modalContent.style.backgroundColor = 'white';
    modalContent.style.padding = '2rem';
    modalContent.style.borderRadius = '0.5rem';
    modalContent.style.maxWidth = '600px';
    modalContent.style.width = '100%';
    
    const title = document.createElement('h2');
    title.textContent = 'Cookie Preferences';
    
    const form = document.createElement('form');
    
    this.consentTypes.forEach(type => {
      if (type === 'necessary') return;
      
      const div = document.createElement('div');
      div.style.marginBottom = '1rem';
      
      const label = document.createElement('label');
      label.style.display = 'flex';
      label.style.alignItems = 'center';
      label.style.gap = '0.5rem';
      
      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.name = type;
      checkbox.checked = this.hasConsent(type);
      checkbox.disabled = type === 'necessary';
      
      const text = document.createTextNode(
        type === 'analytics' ? 'Analytics Cookies' :
        type === 'marketing' ? 'Marketing Cookies' :
        type.charAt(0).toUpperCase() + type.slice(1)
      );
      
      label.appendChild(checkbox);
      label.appendChild(text);
      div.appendChild(label);
      form.appendChild(div);
    });
    
    const buttons = document.createElement('div');
    buttons.style.display = 'flex';
    buttons.style.gap = '0.5rem';
    buttons.style.marginTop = '1rem';
    
    const saveBtn = document.createElement('button');
    saveBtn.type = 'button';
    saveBtn.textContent = 'Save Preferences';
    saveBtn.addEventListener('click', () => {
      const consent = {};
      this.consentTypes.forEach(type => {
        const checkbox = form.querySelector(`input[name="${type}"]`);
        consent[type] = checkbox ? checkbox.checked : false;
      });
      this.setConsent(consent);
      modal.remove();
    });
    
    const cancelBtn = document.createElement('button');
    cancelBtn.type = 'button';
    cancelBtn.textContent = 'Cancel';
    cancelBtn.addEventListener('click', () => {
      modal.remove();
    });
    
    buttons.appendChild(saveBtn);
    buttons.appendChild(cancelBtn);
    
    modalContent.appendChild(title);
    modalContent.appendChild(form);
    modalContent.appendChild(buttons);
    modal.appendChild(modalContent);
    
    document.body.appendChild(modal);
  }

  /**
   * Trigger custom event
   * @param {string} eventName - Name of the event
   * @param {Object} detail - Event detail object
   */
  triggerEvent(eventName, detail) {
    const event = new CustomEvent(eventName, { detail });
    document.dispatchEvent(event);
  }
}

// Example usage:
// const cookieConsent = new CookieCons
