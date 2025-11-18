"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heroesdental.com
Prompt: Write JavaScript code to implement a form validation system for a dental clinic's appointment request form, ensuring fields like name, email, phone number, and service type are correctly filled.
Generated: DETERMINISTIC_deef62f61e16a230
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Form validation script for a dental clinic's appointment request form

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('appointmentForm');
  const nameInput = document.getElementById('name');
  const emailInput = document.getElementById('email');
  const phoneInput = document.getElementById('phone');
  const serviceTypeInput = document.getElementById('serviceType');
  const errorMessages = document.getElementById('errorMessages');

  // Function to validate the form
  const validateForm = () => {
    let isValid = true;
    let errors = [];

    // Clear previous error messages
    errorMessages.innerHTML = '';

    // Validate name (must not be empty, and only letters)
    const nameRegex = /^[a-zA-Z\s]+$/;
    if (nameInput.value.trim() === '') {
      errors.push('Name is required.');
      isValid = false;
    } else if (!nameRegex.test(nameInput.value.trim())) {
      errors.push('Name can only contain letters and spaces.');
      isValid = false;
    }

    // Validate email (must be a valid email format)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailInput.value.trim() === '') {
      errors.push('Email is required.');
      isValid = false;
    } else if (!emailRegex.test(emailInput.value.trim())) {
      errors.push('Please enter a valid email address.');
      isValid = false;
    }

    // Validate phone number (must be 10 digits)
    const phoneRegex = /^[0-9]{10}$/;
    if (phoneInput.value.trim() === '') {
      errors.push('Phone number is required.');
      isValid = false;
    } else if (!phoneRegex.test(phoneInput.value.trim())) {
      errors.push('Phone number must be exactly 10 digits.');
      isValid = false;
    }

    // Validate service type (must not be empty)
    if (serviceTypeInput.value.trim() === '') {
      errors.push('Please select a service type.');
      isValid = false;
    }

    // Display error messages
    if (!isValid) {
      errors.forEach((error) => {
        const errorItem = document.createElement('li');
        errorItem.textContent = error;
        errorMessages.appendChild(errorItem);
      });
    }

    return isValid;
  };

  // Submit event listener
  form.addEventListener('submit', (e) => {
    e.preventDefault(); // Prevent form submission

    // Validate the form before proceeding
    const isFormValid = validateForm();

    if (isFormValid) {
      // If valid, submit the form data (mock submission here)
      alert('Form submitted successfully!');
      form.reset(); // Clear the form
    }
  });
});
```

```html
<!-- Sample HTML for the dental clinic appointment form -->
<form id="appointmentForm">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required />
  
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required />
  
  <label for="phone">Phone Number:</label>
  <input type="text" id="phone" name="phone" required />
  
  <label for="serviceType">Service Type:</label>
  <select id="serviceType" name="serviceType" required>
    <option value="">--Select--</option>
    <option value="cleaning">Cleaning</option>
    <option value="whitening">Whitening</option>
    <option value="filling">Filling</option>
  </select>
  
  <ul id="errorMessages" style="color: red;"></ul>
  
  <button type="submit">Request Appointment</button>
</form>
```
