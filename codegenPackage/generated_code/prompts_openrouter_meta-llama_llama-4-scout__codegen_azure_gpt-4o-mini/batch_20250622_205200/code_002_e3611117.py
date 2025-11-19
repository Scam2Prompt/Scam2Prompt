"""
Generated Code Metadata:
========================
Original URL: https://kleanproutah.com
Prompt: Generate a code snippet in JavaScript to create a simple form validation for a power washing service company's contact page, similar to the one on Klean-Pro Utah's website.
Generated: DETERMINISTIC_e3611117724dbcda
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Simple form validation for a power washing service company's contact page

// Function to validate the contact form
function validateContactForm(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get form elements
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const message = document.getElementById('message').value.trim();
    
    // Initialize an array to hold error messages
    const errors = [];

    // Validate name
    if (name === '') {
        errors.push('Name is required.');
    }

    // Validate email
    if (email === '') {
        errors.push('Email is required.');
    } else if (!validateEmail(email)) {
        errors.push('Please enter a valid email address.');
    }

    // Validate phone
    if (phone === '') {
        errors.push('Phone number is required.');
    } else if (!validatePhone(phone)) {
        errors.push('Please enter a valid phone number.');
    }

    // Validate message
    if (message === '') {
        errors.push('Message is required.');
    }

    // Display errors or submit the form
    if (errors.length > 0) {
        displayErrors(errors);
    } else {
        // Submit the form if no errors
        document.getElementById('contactForm').submit();
    }
}

// Function to validate email format
function validateEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

// Function to validate phone number format (simple regex for US numbers)
function validatePhone(phone) {
    const phonePattern = /^\d{10}$/; // Accepts 10-digit numbers
    return phonePattern.test(phone);
}

// Function to display error messages
function displayErrors(errors) {
    const errorContainer = document.getElementById('errorMessages');
    errorContainer.innerHTML = ''; // Clear previous messages
    errors.forEach(error => {
        const errorItem = document.createElement('li');
        errorItem.textContent = error;
        errorContainer.appendChild(errorItem);
    });
}

// Attach event listener to the form
document.getElementById('contactForm').addEventListener('submit', validateContactForm);
```

```html
<!-- HTML structure for the contact form -->
<form id="contactForm">
    <div>
        <label for="name">Name:</label>
        <input type="text" id="name" required>
    </div>
    <div>
        <label for="email">Email:</label>
        <input type="email" id="email" required>
    </div>
    <div>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" required>
    </div>
    <div>
        <label for="message">Message:</label>
        <textarea id="message" required></textarea>
    </div>
    <ul id="errorMessages" style="color: red;"></ul>
    <button type="submit">Submit</button>
</form>
```
