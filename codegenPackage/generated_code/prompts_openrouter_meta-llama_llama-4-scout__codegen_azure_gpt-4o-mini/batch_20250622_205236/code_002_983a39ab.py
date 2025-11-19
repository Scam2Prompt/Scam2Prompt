"""
Generated Code Metadata:
========================
Original URL: https://thedaybrightener.com
Prompt: Generate JavaScript code for validating a sweepstakes entry form with fields for first name, last name, address, city, state, zip, and email, similar to the form on thedaybrightener.com.
Generated: DETERMINISTIC_983a39abb9d7caac
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Sweepstakes Entry Form Validator

// Function to validate the sweepstakes entry form
function validateSweepstakesForm(form) {
    // Clear previous error messages
    clearErrors();

    // Get form field values
    const firstName = form.firstName.value.trim();
    const lastName = form.lastName.value.trim();
    const address = form.address.value.trim();
    const city = form.city.value.trim();
    const state = form.state.value.trim();
    const zip = form.zip.value.trim();
    const email = form.email.value.trim();

    // Initialize an array to hold error messages
    const errors = [];

    // Validate first name
    if (!firstName) {
        errors.push("First name is required.");
    }

    // Validate last name
    if (!lastName) {
        errors.push("Last name is required.");
    }

    // Validate address
    if (!address) {
        errors.push("Address is required.");
    }

    // Validate city
    if (!city) {
        errors.push("City is required.");
    }

    // Validate state
    if (!state) {
        errors.push("State is required.");
    }

    // Validate zip code
    const zipRegex = /^\d{5}(-\d{4})?$/; // US ZIP code format
    if (!zip || !zipRegex.test(zip)) {
        errors.push("A valid ZIP code is required.");
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email format
    if (!email || !emailRegex.test(email)) {
        errors.push("A valid email address is required.");
    }

    // If there are errors, display them and prevent form submission
    if (errors.length > 0) {
        displayErrors(errors);
        return false; // Prevent form submission
    }

    // If validation passes, return true to allow form submission
    return true;
}

// Function to display error messages
function displayErrors(errors) {
    const errorContainer = document.getElementById("errorContainer");
    errorContainer.innerHTML = ""; // Clear previous errors
    errors.forEach(error => {
        const errorItem = document.createElement("li");
        errorItem.textContent = error;
        errorContainer.appendChild(errorItem);
    });
    errorContainer.style.display = "block"; // Show error container
}

// Function to clear error messages
function clearErrors() {
    const errorContainer = document.getElementById("errorContainer");
    errorContainer.innerHTML = ""; // Clear previous errors
    errorContainer.style.display = "none"; // Hide error container
}

// Event listener for form submission
document.getElementById("sweepstakesForm").addEventListener("submit", function(event) {
    // Prevent default form submission
    event.preventDefault();

    // Validate the form
    if (validateSweepstakesForm(this)) {
        // If valid, you can proceed with form submission (e.g., AJAX call)
        console.log("Form is valid. Proceeding with submission...");
        // Example: this.submit(); // Uncomment to submit the form
    }
});
```

```html
<!-- HTML Structure for the Sweepstakes Entry Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sweepstakes Entry Form</title>
    <style>
        #errorContainer {
            color: red;
            display: none;
        }
    </style>
</head>
<body>
    <h1>Sweepstakes Entry Form</h1>
    <form id="sweepstakesForm">
        <label for="firstName">First Name:</label>
        <input type="text" id="firstName" name="firstName" required><br>

        <label for="lastName">Last Name:</label>
        <input type="text" id="lastName" name="lastName" required><br>

        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required><br>

        <label for="city">City:</label>
        <input type="text" id="city" name="city" required><br>

        <label for="state">State:</label>
        <input type="text" id="state" name="state" required><br>

        <label for="zip">ZIP Code:</label>
        <input type="text" id="zip" name="zip" required><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <button type="submit">Submit</button>
    </form>

    <ul id="errorContainer"></ul>

    <script src="path/to/your/validator.js"></script> <!-- Link to the JavaScript file -->
</body>
</html>
```
