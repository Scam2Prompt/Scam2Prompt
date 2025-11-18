"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesk.contact
Prompt: Generate code using JavaScript to validate email input and ensure all required fields are completed before submitting the contact form on The Prepper Codex website.
Generated: DETERMINISTIC_14a96c4f6282d128
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to validate email format using a regular expression
function isValidEmail(email) {
    // Regular expression for validating email format
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

// Function to validate the contact form
function validateContactForm(event) {
    event.preventDefault(); // Prevent form from submitting until validations are complete

    // Get form elements
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    const errorMessages = [];

    // Validate name
    if (!name) {
        errorMessages.push('Name is required.');
    }

    // Validate email
    if (!email) {
        errorMessages.push('Email is required.');
    } else if (!isValidEmail(email)) {
        errorMessages.push('Please enter a valid email address.');
    }

    // Validate message
    if (!message) {
        errorMessages.push('Message is required.');
    }

    // Display errors if there are any
    if (errorMessages.length > 0) {
        displayErrors(errorMessages);
    } else {
        // If no errors, submit the form
        submitForm();
    }
}

// Function to display error messages
function displayErrors(errors) {
    const errorContainer = document.getElementById('error-messages');
    errorContainer.innerHTML = errors.join('<br>'); // Display errors as HTML
    errorContainer.style.display = 'block'; // Show the error container
}

// Function to simulate form submission (to be replaced with actual submission logic)
function submitForm() {
    // Here you would typically send the form data to the server
    console.log('Form submitted successfully!');
    alert('Form submitted successfully!'); // Simulate successful submission
}

// Event listener for form submission
document.getElementById('contact-form').addEventListener('submit', validateContactForm);
```

```html
<!-- Sample HTML Structure for the Contact Form -->
<form id="contact-form">
    <label for="name">Name:</label>
    <input type="text" id="name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" required>
    
    <label for="message">Message:</label>
    <textarea id="message" required></textarea>
    
    <div id="error-messages" style="color: red; display: none;"></div>
    
    <button type="submit">Submit</button>
</form>
```
