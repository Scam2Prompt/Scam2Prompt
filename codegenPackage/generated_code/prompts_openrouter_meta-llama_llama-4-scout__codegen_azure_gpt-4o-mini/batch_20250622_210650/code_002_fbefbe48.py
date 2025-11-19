"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Generate a sample code snippet in JavaScript for a basic contact form validation, similar to the one on the textcounsellingonline.com.au website, ensuring that fields such as name, email, and message are properly validated before submission.
Generated: DETERMINISTIC_fbefbe48ef075cf5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Contact Form Validation Script

// Function to validate the contact form
function validateContactForm(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get form fields
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Initialize an array to hold error messages
    const errors = [];

    // Validate name
    if (name === '') {
        errors.push('Name is required.');
    } else if (name.length < 2) {
        errors.push('Name must be at least 2 characters long.');
    }

    // Validate email
    if (email === '') {
        errors.push('Email is required.');
    } else if (!isValidEmail(email)) {
        errors.push('Please enter a valid email address.');
    }

    // Validate message
    if (message === '') {
        errors.push('Message is required.');
    } else if (message.length < 10) {
        errors.push('Message must be at least 10 characters long.');
    }

    // Display errors or submit the form
    if (errors.length > 0) {
        displayErrors(errors);
    } else {
        // If no errors, submit the form (this is where you would handle the form submission)
        console.log('Form submitted successfully!');
        // You can use AJAX or fetch to send the data to the server here
    }
}

// Function to validate email format
function isValidEmail(email) {
    // Regular expression for validating email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

// Function to display error messages
function displayErrors(errors) {
    const errorContainer = document.getElementById('error-messages');
    errorContainer.innerHTML = ''; // Clear previous errors

    // Create a list of error messages
    const errorList = document.createElement('ul');
    errors.forEach(error => {
        const listItem = document.createElement('li');
        listItem.textContent = error;
        errorList.appendChild(listItem);
    });

    // Append the error list to the error container
    errorContainer.appendChild(errorList);
}

// Attach the validation function to the form's submit event
document.getElementById('contact-form').addEventListener('submit', validateContactForm);
```

```html
<!-- Sample HTML for the contact form -->
<form id="contact-form">
    <div>
        <label for="name">Name:</label>
        <input type="text" id="name" required>
    </div>
    <div>
        <label for="email">Email:</label>
        <input type="email" id="email" required>
    </div>
    <div>
        <label for="message">Message:</label>
        <textarea id="message" required></textarea>
    </div>
    <div id="error-messages" style="color: red;"></div>
    <button type="submit">Submit</button>
</form>
```
