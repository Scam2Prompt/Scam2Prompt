"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Create a validation script in JavaScript for a ticket booking form that ensures the "Email Address" is properly formatted, the "Phone Number" contains only digits, and at least one "Preferred Method of Communication" is selected.
Generated: DETERMINISTIC_3f1fcb838e673f27
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Ticket Booking Form Validation Script

// Function to validate the ticket booking form
function validateBookingForm() {
    // Get form elements
    const emailInput = document.getElementById('email');
    const phoneInput = document.getElementById('phone');
    const communicationMethods = document.querySelectorAll('input[name="communicationMethod"]');
    const errorMessages = [];

    // Validate email format
    if (!validateEmail(emailInput.value)) {
        errorMessages.push('Please enter a valid email address.');
    }

    // Validate phone number (only digits)
    if (!validatePhoneNumber(phoneInput.value)) {
        errorMessages.push('Phone number must contain only digits.');
    }

    // Validate at least one communication method is selected
    if (!isCommunicationMethodSelected(communicationMethods)) {
        errorMessages.push('Please select at least one preferred method of communication.');
    }

    // Display error messages if any
    if (errorMessages.length > 0) {
        displayErrors(errorMessages);
        return false; // Prevent form submission
    }

    // If all validations pass
    return true; // Allow form submission
}

// Function to validate email format using regex
function validateEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

// Function to validate phone number (only digits)
function validatePhoneNumber(phone) {
    const phonePattern = /^\d+$/;
    return phonePattern.test(phone);
}

// Function to check if at least one communication method is selected
function isCommunicationMethodSelected(methods) {
    return Array.from(methods).some(method => method.checked);
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

// Event listener for form submission
document.getElementById('bookingForm').addEventListener('submit', function(event) {
    if (!validateBookingForm()) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});
```

```html
<!-- Sample HTML for the ticket booking form -->
<form id="bookingForm">
    <label for="email">Email Address:</label>
    <input type="email" id="email" required>
    
    <label for="phone">Phone Number:</label>
    <input type="text" id="phone" required>
    
    <fieldset>
        <legend>Preferred Method of Communication:</legend>
        <label><input type="checkbox" name="communicationMethod" value="email"> Email</label>
        <label><input type="checkbox" name="communicationMethod" value="phone"> Phone</label>
        <label><input type="checkbox" name="communicationMethod" value="sms"> SMS</label>
    </fieldset>
    
    <ul id="errorMessages" style="color: red;"></ul>
    
    <button type="submit">Book Ticket</button>
</form>
```
