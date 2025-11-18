"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99pancakes.help
Prompt: Generate JavaScript code to add client-side validation for a WordPress help desk login form, ensuring all fields are filled before submission.
Generated: DETERMINISTIC_b9bdcd4a146c22f4
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Client-side validation for the WordPress help desk login form

// Function to validate the login form
function validateLoginForm(event) {
    // Prevent the default form submission behavior
    event.preventDefault();
    
    // Get the form element
    const form = document.getElementById('loginForm');
    
    // Get the input fields
    const username = form.querySelector('input[name="username"]');
    const password = form.querySelector('input[name="password"]');
    
    // Clear previous error messages
    clearErrorMessages();

    // Check if the username field is empty
    if (username.value.trim() === '') {
        displayErrorMessage(username, 'Username is required.');
        return false;
    }

    // Check if the password field is empty
    if (password.value.trim() === '') {
        displayErrorMessage(password, 'Password is required.');
        return false;
    }

    // If no errors, submit the form
    form.submit();
}

// Function to display error messages
function displayErrorMessage(inputField, message) {
    // Create a new span element for the error message
    const errorSpan = document.createElement('span');
    errorSpan.className = 'error-message';
    errorSpan.textContent = message;

    // Insert the error message after the input field
    inputField.parentNode.insertBefore(errorSpan, inputField.nextSibling);
}

// Function to clear existing error messages
function clearErrorMessages() {
    // Select all error messages and remove them
    const errorMessages = document.querySelectorAll('.error-message');
    errorMessages.forEach(function(errorMessage) {
        errorMessage.remove();
    });
}

// Attach the validation function to the form's submit event
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('loginForm');
    if (form) {
        form.addEventListener('submit', validateLoginForm);
    }
});
```

**HTML Example for Reference:**
```html
<form id="loginForm">
    <label for="username">Username:</label>
    <input type="text" name="username" id="username" required>
    
    <label for="password">Password:</label>
    <input type="password" name="password" id="password" required>
    
    <button type="submit">Login</button>
</form>
```
