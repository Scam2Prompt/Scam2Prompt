"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://komputailogin.com
Prompt: Can you provide an example of a simple JavaScript function that improves user experience on a login page?
Generated: DETERMINISTIC_a21daad8835c41d8
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A simple JavaScript function to enhance user experience on a login page
 * by showing/hiding the password input field when the user clicks a toggle button.
 * 
 * @param {string} passwordInputId - The ID of the password input field.
 * @param {string} toggleButtonId - The ID of the button that toggles the password visibility.
 */
function togglePasswordVisibility(passwordInputId, toggleButtonId) {
    try {
        // Get the password input field and toggle button elements
        const passwordInput = document.getElementById(passwordInputId);
        const toggleButton = document.getElementById(toggleButtonId);

        // Check if both elements exist
        if (!passwordInput || !toggleButton) {
            throw new Error('Invalid input: Ensure the password input and toggle button IDs are correct.');
        }

        // Event listener for the toggle button
        toggleButton.addEventListener('click', () => {
            // Toggle the input type between 'password' and 'text'
            const isPasswordVisible = passwordInput.type === 'text';
            passwordInput.type = isPasswordVisible ? 'password' : 'text';
            
            // Update the button text based on the visibility state
            toggleButton.textContent = isPasswordVisible ? 'Show Password' : 'Hide Password';
        });
    } catch (error) {
        // Log error to the console for debugging
        console.error('Error in togglePasswordVisibility:', error.message);
    }
}

// Usage example: Call the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    togglePasswordVisibility('password-input', 'toggle-password-btn');
});
```

```html
<!-- HTML structure for demonstration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
</head>
<body>
    <form id="login-form">
        <label for="password-input">Password:</label>
        <input type="password" id="password-input" required>
        <button type="button" id="toggle-password-btn">Show Password</button>
        <input type="submit" value="Login">
    </form>
    <script src="path/to/your/script.js"></script>
</body>
</html>
```
