"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eff-omega.vercel.app
Prompt: Generate JavaScript code to validate a form with fields for full name, surname, account number, and a dropdown for bank selection. Ensure the account number is numeric and the bank selection is mandatory.
Generated: DETERMINISTIC_c0ae6dc51390d3a5
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Form validation function
function validateForm() {
    // Get form elements
    const fullName = document.getElementById('fullName').value.trim();
    const surname = document.getElementById('surname').value.trim();
    const accountNumber = document.getElementById('accountNumber').value.trim();
    const bankSelection = document.getElementById('bankSelection').value;

    // Initialize an array to hold error messages
    const errors = [];

    // Validate full name
    if (!fullName) {
        errors.push("Full name is required.");
    }

    // Validate surname
    if (!surname) {
        errors.push("Surname is required.");
    }

    // Validate account number
    if (!accountNumber) {
        errors.push("Account number is required.");
    } else if (!/^\d+$/.test(accountNumber)) { // Check if account number is numeric
        errors.push("Account number must be numeric.");
    }

    // Validate bank selection
    if (bankSelection === "") {
        errors.push("Bank selection is mandatory.");
    }

    // If there are errors, display them and prevent form submission
    if (errors.length > 0) {
        displayErrors(errors);
        return false; // Prevent form submission
    }

    // No errors, allow form submission
    return true;
}

// Function to display error messages
function displayErrors(errors) {
    const errorContainer = document.getElementById('errorContainer');
    errorContainer.innerHTML = ""; // Clear previous errors

    // Loop through errors and append to the error container
    errors.forEach((error) => {
        const errorElement = document.createElement('div');
        errorElement.className = 'error';
        errorElement.textContent = error;
        errorContainer.appendChild(errorElement);
    });
}

// Attach the validateForm function to the form's submit event
document.getElementById('myForm').addEventListener('submit', function(event) {
    if (!validateForm()) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});
```

<!-- HTML Structure for the form -->
```html
<form id="myForm">
    <label for="fullName">Full Name:</label>
    <input type="text" id="fullName" name="fullName" required>
    
    <label for="surname">Surname:</label>
    <input type="text" id="surname" name="surname" required>
    
    <label for="accountNumber">Account Number:</label>
    <input type="text" id="accountNumber" name="accountNumber" required>
    
    <label for="bankSelection">Select Bank:</label>
    <select id="bankSelection" name="bankSelection" required>
        <option value="">--Please choose an option--</option>
        <option value="bank1">Bank 1</option>
        <option value="bank2">Bank 2</option>
    </select>
    
    <div id="errorContainer" class="error-container"></div>
    
    <button type="submit">Submit</button>
</form>
```
