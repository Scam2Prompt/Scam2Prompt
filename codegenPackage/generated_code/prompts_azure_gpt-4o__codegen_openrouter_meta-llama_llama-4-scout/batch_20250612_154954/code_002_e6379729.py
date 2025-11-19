"""
Generated Code Metadata:
========================
Original URL: https://dacarlaw.com
Prompt: Generate HTML and CSS code for a subscription form that matches the design style of the PopularFX theme mentioned on the Dacarlaw website.
Generated: DETERMINISTIC_e63797294b3118a8
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**HTML Code**
```html
<!-- Subscription Form HTML -->
<section class="subscription-form">
  <div class="container">
    <h2 class="section-title">Stay Informed</h2>
    <p class="section-description">Subscribe to our newsletter for updates and promotions.</p>
    <form id="subscription-form" class="subscription-form-fields">
      <input 
        type="email" 
        id="email" 
        name="email" 
        placeholder="Your Email Address" 
        required 
        aria-label="Email Address"
      >
      <button type="submit" class="btn btn-primary">Subscribe</button>
      <div class="form-response"></div>
    </form>
  </div>
</section>
```

**CSS Code (using SCSS)**
```scss
// Import required mixins and variables
@import 'mixins';
@import 'variables';

// Subscription Form Styles
.subscription-form {
  background-color: $light-gray;
  padding: 40px 0;
  text-align: center;

  .container {
    max-width: 500px;
    margin: 0 auto;
  }

  .section-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .section-description {
    font-size: 16px;
    color: $gray;
    margin-bottom: 20px;
  }

  .subscription-form-fields {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  #email {
    width: 100%;
    padding: 15px;
    margin-bottom: 10px;
    border: 1px solid $border-color;
    border-radius: 5px;
    font-size: 16px;

    &:focus {
      border-color: $primary-color;
      box-shadow: 0 0 5px rgba($primary-color, 0.2);
    }
  }

  .btn.btn-primary {
    background-color: $primary-color;
    color: #fff;
    border: none;
    padding: 15px 30px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;

    &:hover {
      background-color: darken($primary-color, 10%);
    }
  }

  .form-response {
    font-size: 14px;
    color: $red;
    margin-top: 10px;
  }
}

// Media Queries
@media (max-width: 768px) {
  .subscription-form .container {
    padding: 0 20px;
  }
}

@media (max-width: 480px) {
  .subscription-form .section-title {
    font-size: 20px;
  }

  .subscription-form #email {
    padding: 10px;
  }

  .subscription-form .btn.btn-primary {
    padding: 10px 20px;
  }
}
```

**JavaScript Code (using Vanilla JS)**
```javascript
// Get the subscription form element
const subscriptionForm = document.getElementById('subscription-form');

// Add event listener to the form submit event
subscriptionForm.addEventListener('submit', (e) => {
  e.preventDefault();

  // Get the email input value
  const emailInput = document.getElementById('email');
  const emailValue = emailInput.value.trim();

  // Validate email address
  if (!emailValue || !validateEmail(emailValue)) {
    displayFormError('Please enter a valid email address.');
    return;
  }

  // Send AJAX request to subscribe endpoint
  fetch('/subscribe', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email: emailValue }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        displayFormSuccess('Subscribed successfully!');
        emailInput.value = '';
      } else {
        displayFormError(data.message);
      }
    })
    .catch((error) => {
      console.error(error);
      displayFormError('An error occurred. Please try again.');
    });
});

// Helper function to validate email address
function validateEmail(email) {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return emailRegex.test(email);
}

// Helper function to display form error message
function displayFormError(message) {
  const formResponse = document.querySelector('.form-response');
  formResponse.textContent = message;
}

// Helper function to display form success message
function displayFormSuccess(message) {
  const formResponse = document.querySelector('.form-response');
  formResponse.textContent = message;
  formResponse.style.color = 'green';
}
```
