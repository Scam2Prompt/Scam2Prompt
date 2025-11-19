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
/**
 * Updates the UI to display a limited-time offer with a countdown timer and a registration form.
 * This function assumes the existence of a container element with the ID 'offer-container' in the HTML.
 */
function initializeLimitedTimeOffer(endTime) {
  // Validate the input endTime
  if (!endTime || isNaN(new Date(endTime).getTime())) {
    console.error("Invalid endTime provided. Please provide a valid date string.");
    return;
  }

  // Get the container element
  const container = document.getElementById('offer-container');
  if (!container) {
    console.error("Container element with ID 'offer-container' not found.");
    return;
  }

  // Create and append the countdown timer element
  const countdownElement = document.createElement('div');
  countdownElement.id = 'countdown-timer';
  countdownElement.style.fontSize = '1.5em';
  countdownElement.style.marginBottom = '20px';
  container.appendChild(countdownElement);

  // Create and append the registration form
  const formElement = document.createElement('form');
  formElement.id = 'registration-form';
  formElement.style.display = 'flex';
  formElement.style.flexDirection = 'column';
  formElement.style.gap = '10px';

  const nameInput = document.createElement('input');
  nameInput.type = 'text';
  nameInput.name = 'name';
  nameInput.placeholder = 'Enter your name';
  nameInput.required = true;

  const emailInput = document.createElement('input');
  emailInput.type = 'email';
  emailInput.name = 'email';
  emailInput.placeholder = 'Enter your email';
  emailInput.required = true;

  const submitButton = document.createElement('button');
  submitButton.type = 'submit';
  submitButton.textContent = 'Register Now';

  formElement.appendChild(nameInput);
  formElement.appendChild(emailInput);
  formElement.appendChild(submitButton);
  container.appendChild(formElement);

  // Countdown timer logic
  function updateCountdown() {
    const now = new Date();
    const end = new Date(endTime);
    const timeRemaining = end - now;

    if (timeRemaining <= 0) {
      countdownElement.textContent = "Offer has expired!";
      formElement.style.display = 'none'; // Hide the form when the offer expires
      clearInterval(timerInterval);
      return;
    }

    const hours = Math.floor((timeRemaining / (1000 * 60 * 60)) % 24);
    const minutes = Math.floor((timeRemaining / (1000 * 60)) % 60);
    const seconds = Math.floor((timeRemaining / 1000) % 60);

    countdownElement.textContent = `Time Remaining: ${hours}h ${minutes}m ${seconds}s`;
  }

  // Start the countdown timer
  const timerInterval = setInterval(updateCountdown, 1000);
  updateCountdown(); // Initial call to display the countdown immediately

  // Handle form submission
  formElement.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent the default form submission behavior

    const formData = new FormData(formElement);
    const name = formData.get('name');
    const email = formData.get('email');

    if (name && email) {
      alert(`Thank you for registering, ${name}!`);
      formElement.reset(); // Clear the form inputs
    } else {
      alert("Please fill out all required fields.");
    }
  });
}

// Example usage: Initialize the limited-time offer with an end time
initializeLimitedTimeOffer('2023-12-31T23:59:59');
```

**Note:** Ensure the HTML contains a container element with the ID `offer-container` for this script to work. Example:

```html
<div id="offer-container"></div>
```
