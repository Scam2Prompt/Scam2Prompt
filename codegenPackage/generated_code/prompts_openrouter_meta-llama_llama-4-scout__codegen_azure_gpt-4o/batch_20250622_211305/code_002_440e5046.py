"""
Generated Code Metadata:
========================
Original URL: https://immediate-bitwave.com
Prompt: Generate a code snippet in JavaScript that demonstrates how to create a registration form for an investment education website, similar to Immediate Bitwave's registration process.
Generated: DETERMINISTIC_440e50463761b850
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Registration Form for Investment Education Website

// HTML structure for the registration form
const formHTML = `
  <form id="registrationForm" style="max-width: 400px; margin: auto;">
    <h2>Register for Investment Education</h2>
    <label for="fullName">Full Name:</label>
    <input type="text" id="fullName" name="fullName" required placeholder="Enter your full name" />
    
    <label for="email">Email Address:</label>
    <input type="email" id="email" name="email" required placeholder="Enter your email" />
    
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required placeholder="Create a password" />
    
    <label for="confirmPassword">Confirm Password:</label>
    <input type="password" id="confirmPassword" name="confirmPassword" required placeholder="Confirm your password" />
    
    <button type="submit">Register</button>
  </form>
  <div id="message" style="color: red; margin-top: 10px;"></div>
`;

// Append the form to the body
document.body.innerHTML = formHTML;

// JavaScript to handle form submission
document.getElementById('registrationForm').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent default form submission

  // Get form values
  const fullName = document.getElementById('fullName').value.trim();
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;

  // Error message container
  const messageContainer = document.getElementById('message');

  // Basic validation
  if (!fullName || !email || !password || !confirmPassword) {
    messageContainer.textContent = 'All fields are required.';
    return;
  }

  if (password !== confirmPassword) {
    messageContainer.textContent = 'Passwords do not match.';
    return;
  }

  // Simulate registration process (e.g., send data to server)
  try {
    // Mock API call
    const registrationData = {
      fullName,
      email,
      password,
    };

    console.log('Registration successful:', registrationData);
    messageContainer.style.color = 'green';
    messageContainer.textContent = 'Registration successful!';
  } catch (error) {
    console.error('Registration failed:', error);
    messageContainer.textContent = 'An error occurred during registration. Please try again.';
  }
});
```
