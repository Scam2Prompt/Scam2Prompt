"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.onboarding.dbankonline.com
Prompt: Write JavaScript code to create a responsive form similar to the one on the Dbank website for collecting user data (name, email, phone, country) with validation.
Generated: DETERMINISTIC_98c3b8f056d2ff0b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML Structure for the Responsive Form
const formHTML = `
  <form id="userDataForm" style="max-width: 500px; margin: auto;">
    <h2>User Information Form</h2>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" placeholder="Enter your name" required>
    <small class="error-message" id="nameError"></small>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" placeholder="Enter your email" required>
    <small class="error-message" id="emailError"></small>

    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
    <small class="error-message" id="phoneError"></small>

    <label for="country">Country:</label>
    <select id="country" name="country" required>
      <option value="">Select your country</option>
      <option value="US">United States</option>
      <option value="CA">Canada</option>
      <option value="UK">United Kingdom</option>
      <option value="AU">Australia</option>
    </select>
    <small class="error-message" id="countryError"></small>

    <button type="submit">Submit</button>
  </form>
`;

// Append Form HTML to the DOM
document.body.innerHTML = formHTML;

// JavaScript for Form Validation and Handling
document.getElementById('userDataForm').addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent form submission
  
  let isValid = true; // Flag to track validation status

  // Clear previous error messages
  document.querySelectorAll('.error-message').forEach((element) => {
    element.textContent = '';
  });

  // Validate Name (should not be empty)
  const name = document.getElementById('name').value.trim();
  if (name === '') {
    document.getElementById('nameError').textContent = 'Name is required.';
    isValid = false;
  }

  // Validate Email (must be in a valid format)
  const email = document.getElementById('email').value.trim();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    document.getElementById('emailError').textContent = 'Please enter a valid email address.';
    isValid = false;
  }

  // Validate Phone (must be numeric and 10-15 characters long)
  const phone = document.getElementById('phone').value.trim();
  const phoneRegex = /^\d{10,15}$/;
  if (!phoneRegex.test(phone)) {
    document.getElementById('phoneError').textContent = 'Phone number must be 10-15 digits.';
    isValid = false;
  }

  // Validate Country (must be selected)
  const country = document.getElementById('country').value;
  if (country === '') {
    document.getElementById('countryError').textContent = 'Please select your country.';
    isValid = false;
  }

  // If all validations pass, print data to console and reset form
  if (isValid) {
    console.log({
      name,
      email,
      phone,
      country,
    });
    alert('Form submitted successfully!');
    document.getElementById('userDataForm').reset();
  }
});

// CSS Styles for Responsive Form
const styles = `
  body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 20px;
  }
  
  form {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }

  input, select, button {
    width: 100%;
    margin-bottom: 15px;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }

  button {
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }

  .error-message {
    color: red;
    font-size: 14px;
    margin-top: -10px;
    margin-bottom: 10px;
  }

  @media (max-width: 600px) {
    form {
      padding: 10px;
    }
  }
`;

// Append CSS to the DOM
const styleSheet = document.createElement('style');
styleSheet.type = 'text/css';
styleSheet.innerText = styles;
document.head.appendChild(styleSheet);
```
