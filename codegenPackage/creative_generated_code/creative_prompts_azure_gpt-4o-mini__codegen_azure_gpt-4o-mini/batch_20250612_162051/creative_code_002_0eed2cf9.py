"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.getaconsulenze.it
Prompt: Create a code snippet in JavaScript that validates user input for the Certificazione di alfabetizzazione digitale (CIAD) registration form mentioned on Geta Consulenze's site.
Generated: DETERMINISTIC_0eed2cf9f68a82b7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CIAD Registration Form Validation

// Function to validate the registration form inputs
function validateCIADForm(form) {
    // Get input values from the form
    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const age = form.age.value.trim();
    const phone = form.phone.value.trim();

    // Regular expressions for validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phonePattern = /^\+?[1-9]\d{1,14}$/; // E.164 format for phone numbers

    // Check if the name is not empty and contains only letters
    if (!name || !/^[a-zA-Z\s]+$/.test(name)) {
        alert("Please enter a valid name using only letters.");
        return false;
    }

    // Check if the email is valid
    if (!email || !emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    // Check if the age is a number and within the valid range (18-99)
    const ageNumber = Number(age);
    if (isNaN(ageNumber) || ageNumber < 18 || ageNumber > 99) {
        alert("Please enter a valid age between 18 and 99.");
        return false;
    }

    // Check if the phone number is valid
    if (!phone || !phonePattern.test(phone)) {
        alert("Please enter a valid phone number.");
        return false;
    }

    // All validations passed, return true
    return true;
}

// Event listener for form submission
document.getElementById('ciadRegistrationForm').addEventListener('submit', function(event) {
    // Prevent form submission if validation fails
    if (!validateCIADForm(this)) {
        event.preventDefault();
    }
});
```

```html
<!-- Sample HTML Form for CIAD Registration -->
<form id="ciadRegistrationForm">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required />

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required />

    <label for="age">Age:</label>
    <input type="number" id="age" name="age" required />

    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone" required />

    <button type="submit">Register</button>
</form>
```
