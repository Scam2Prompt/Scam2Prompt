"""
Generated Code Metadata:
========================
Original URL: https://bafybeie4pmtgef2aky2kufa62lr3cskoycrmadlj4vrwrv3xsddb7pdqbi.ipfs.dweb.link
Prompt: Create a JavaScript function that updates the UI of a webpage to reflect a limited-time offer, similar to the Moonbirds Universe registration page, showing a countdown and a registration form.
Generated: DETERMINISTIC_d7a3b5ad46ee1333
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// limitedTimeOffer.js

class LimitedTimeOffer {
  /**
   * Constructor for LimitedTimeOffer
   * @param {Object} config - Configuration object
   * @param {String} config.offerEndDate - End date of the offer in ISO format
   * @param {String} config.formSelector - CSS selector for the registration form
   * @param {String} config.countdownSelector - CSS selector for the countdown element
   */
  constructor(config) {
    this.config = config;
    this.offerEndDate = new Date(config.offerEndDate);
    this.formSelector = config.formSelector;
    this.countdownSelector = config.countdownSelector;
    this.form = document.querySelector(this.formSelector);
    this.countdownElement = document.querySelector(this.countdownSelector);

    // Check if elements exist
    if (!this.form) {
      throw new Error(`Registration form not found: ${this.formSelector}`);
    }
    if (!this.countdownElement) {
      throw new Error(`Countdown element not found: ${this.countdownSelector}`);
    }

    // Bind event listeners
    this.form.addEventListener('submit', this.handleFormSubmit.bind(this));
    this.updateCountdown();
    this.intervalId = setInterval(this.updateCountdown.bind(this), 1000);
  }

  /**
   * Updates the countdown UI
   */
  updateCountdown() {
    const now = new Date();
    const timeLeft = this.offerEndDate.getTime() - now.getTime();

    if (timeLeft <= 0) {
      // Offer has expired, clear interval and update UI
      clearInterval(this.intervalId);
      this.countdownElement.textContent = 'Offer has expired';
      this.form.disabled = true;
      return;
    }

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    this.countdownElement.textContent = `
      ${days}d ${hours}h ${minutes}m ${seconds}s
    `;
  }

  /**
   * Handles form submission
   * @param {Event} event - Form submission event
   */
  handleFormSubmit(event) {
    event.preventDefault();
    const formData = new FormData(this.form);

    // Example: Send form data to server
    fetch('/register', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  }
}

// Example usage
const config = {
  offerEndDate: '2024-09-20T14:30:00.000Z',
  formSelector: '#registration-form',
  countdownSelector: '#countdown',
};

const limitedTimeOffer = new LimitedTimeOffer(config);
```
