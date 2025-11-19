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
/**
 * Contact Form Validation Script
 * Validates name, email, and message fields before form submission
 */

document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            // Get form elements
            const nameInput = document.getElementById('name');
            const emailInput = document.getElementById('email');
            const messageInput = document.getElementById('message');
            const errorContainer = document.getElementById('formErrors');
            
            // Clear previous errors
            errorContainer.innerHTML = '';
            errorContainer.style.display = 'none';
            
            // Validate fields
            const errors = [];
            
            // Name validation
            if (!nameInput.value.trim()) {
                errors.push('Name is required');
                nameInput.classList.add('error');
            } else {
                nameInput.classList.remove('error');
            }
            
            // Email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailInput.value.trim()) {
                errors.push('Email is required');
                emailInput.classList.add('error');
            } else if (!emailRegex.test(emailInput.value)) {
                errors.push('Please enter a valid email address');
                emailInput.classList.add('error');
            } else {
                emailInput.classList.remove('error');
            }
            
            // Message validation
            if (!messageInput.value.trim()) {
                errors.push('Message is required');
                messageInput.classList.add('error');
            } else if (messageInput.value.trim().length < 10) {
                errors.push('Message should be at least 10 characters long');
                messageInput.classList.add('error');
            } else {
                messageInput.classList.remove('error');
            }
            
            // Display errors or submit form
            if (errors.length > 0) {
                errorContainer.style.display = 'block';
                errors.forEach(error => {
                    const errorElement = document.createElement('p');
                    errorElement.textContent = error;
                    errorElement.classList.add('error-message');
                    errorContainer.appendChild(errorElement);
                });
            } else {
                // Form is valid, proceed with submission
                contactForm.submit();
            }
        });
    }
});
```
