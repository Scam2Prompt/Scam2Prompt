"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-theta-three.vercel.app
Prompt: Provide an example of how to implement password confirmation validation in JavaScript for a registration form, referencing the structure on https://d-theta-three.vercel.app.
Generated: DETERMINISTIC_c2092ee2b42500a6
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Password Confirmation Validation for a Registration Form

// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {

    // Select form elements
    const registrationForm = document.getElementById('registrationForm'); // Replace with your form ID
    const passwordInput = document.getElementById('password');           // Replace with your password input ID
    const confirmPasswordInput = document.getElementById('confirmPassword'); // Replace with your confirm password input ID
    const errorMessage = document.getElementById('errorMessage');        // Replace with your error message container ID

    // Attach event listener to form submission
    registrationForm.addEventListener('submit', (event) => {

        // Prevent the form from submitting
        event.preventDefault();

        // Validate password confirmation
        if (passwordInput.value !== confirmPasswordInput.value) {
            // Display error message
            errorMessage.textContent = 'Passwords do not match.';
            errorMessage.style.color = 'red';
        } else {
            // Clear any previous error message
            errorMessage.textContent = '';

            // Simulate form submission (production-ready code might submit via AJAX or other methods)
            console.log('Form submitted successfully!');
            
            // You can invoke actual form submission here, e.g., registrationForm.submit();
        }
    });

    // Optional: Add real-time validation for better user experience
    confirmPasswordInput.addEventListener('input', () => {
        if (passwordInput.value !== confirmPasswordInput.value) {
            errorMessage.textContent = 'Passwords do not match.';
            errorMessage.style.color = 'red';
        } else {
            errorMessage.textContent = '';
        }
    });

});
```

### Requirements:
- Replace `registrationForm`, `password`, `confirmPassword`, and `errorMessage` with actual IDs used in your HTML structure.
- Ensure the HTML contains matching elements with these IDs and appropriate attributes.
