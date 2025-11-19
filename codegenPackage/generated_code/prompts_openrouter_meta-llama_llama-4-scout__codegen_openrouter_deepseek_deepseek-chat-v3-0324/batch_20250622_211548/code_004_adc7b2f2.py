"""
Generated Code Metadata:
========================
Original URL: https://centralseedandchem.co.nz
Prompt: Create a JavaScript function to validate a contact form submission like the one on the Central Seed & Chemical website, handling errors and sending a confirmation message.
Generated: DETERMINISTIC_adc7b2f29c1848ad
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates and handles a contact form submission.
 * @param {Event} event - The form submission event.
 * @returns {void}
 */
function handleContactFormSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form elements
    const form = event.target;
    const nameInput = form.querySelector('input[name="name"]');
    const emailInput = form.querySelector('input[name="email"]');
    const phoneInput = form.querySelector('input[name="phone"]');
    const messageInput = form.querySelector('textarea[name="message"]');
    const errorContainer = form.querySelector('.error-message');
    const successContainer = form.querySelector('.success-message');

    // Clear previous messages
    errorContainer.textContent = '';
    successContainer.textContent = '';

    // Validate inputs
    const errors = [];

    if (!nameInput.value.trim()) {
        errors.push('Name is required');
    }

    if (!emailInput.value.trim()) {
        errors.push('Email is required');
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value)) {
        errors.push('Please enter a valid email address');
    }

    if (phoneInput.value && !/^[\d\s\-()+]+$/.test(phoneInput.value)) {
        errors.push('Please enter a valid phone number');
    }

    if (!messageInput.value.trim()) {
        errors.push('Message is required');
    }

    // Display errors if any
    if (errors.length > 0) {
        errorContainer.textContent = errors.join('. ') + '.';
        return;
    }

    // Prepare form data for submission
    const formData = new FormData(form);

    // Simulate form submission (replace with actual AJAX call in production)
    setTimeout(() => {
        // In a real implementation, you would use fetch() or XMLHttpRequest
        console.log('Form submitted with data:', Object.fromEntries(formData));
        
        // Show success message
        successContainer.textContent = 'Thank you for your message! We will get back to you soon.';
        
        // Reset form
        form.reset();
    }, 1000);
}

// Add event listener when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', handleContactFormSubmit);
    }
});
```

HTML structure for reference (not part of the JS code):
```html
<form id="contact-form">
    <div class="form-group">
        <label for="name">Name*</label>
        <input type="text" name="name" id="name" required>
    </div>
    <div class="form-group">
        <label for="email">Email*</label>
        <input type="email" name="email" id="email" required>
    </div>
    <div class="form-group">
        <label for="phone">Phone</label>
        <input type="tel" name="phone" id="phone">
    </div>
    <div class="form-group">
        <label for="message">Message*</label>
        <textarea name="message" id="message" required></textarea>
    </div>
    <div class="error-message" style="color: red;"></div>
    <div class="success-message" style="color: green;"></div>
    <button type="submit">Submit</button>
</form>
```
