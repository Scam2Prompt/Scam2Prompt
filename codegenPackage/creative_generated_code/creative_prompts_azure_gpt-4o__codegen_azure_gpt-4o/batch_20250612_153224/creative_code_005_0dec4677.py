"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://churchproweb.com
Prompt: Create a JavaScript function for a "Prayer Request" form that validates user input and sends the data to a backend service for processing, inspired by ChurchProWeb's website features.
Generated: DETERMINISTIC_0dec467785800781
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to validate and send "Prayer Request" form data to the backend service.
 * This function assumes the form has fields: name, email, and prayerRequest.
 * It performs validation on user input and sends data to the server via a POST request.
 */

// Function to handle the prayer request form submission
async function handlePrayerRequestFormSubmission(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Get form elements
    const form = event.target;
    const name = form.name.value.trim();
    const email = form.email.value.trim();
    const prayerRequest = form.prayerRequest.value.trim();

    // Validate user input
    const errors = validateFormInput(name, email, prayerRequest);
    if (errors.length > 0) {
        displayErrors(errors);
        return;
    }

    // Prepare data to send to the backend
    const requestData = { name, email, prayerRequest };

    try {
        // Send data to the backend via a POST request
        const response = await fetch('/api/prayer-request', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData),
        });

        // Handle server response
        if (!response.ok) {
            throw new Error(`Server responded with a ${response.status} status.`);
        }

        const responseData = await response.json();
        handleSuccess(responseData);
    } catch (error) {
        handleError(error.message);
    }
}

// Function to validate form input
function validateFormInput(name, email, prayerRequest) {
    const errors = [];

    // Validate name
    if (!name) {
        errors.push('Name field cannot be empty.');
    } else if (name.length < 2 || name.length > 50) {
        errors.push('Name must be between 2 and 50 characters.');
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex
    if (!email) {
        errors.push('Email field cannot be empty.');
    } else if (!emailRegex.test(email)) {
        errors.push('Please provide a valid email address.');
    }

    // Validate prayer request
    if (!prayerRequest) {
        errors.push('Prayer request field cannot be empty.');
    } else if (prayerRequest.length < 10 || prayerRequest.length > 500) {
        errors.push('Prayer request must be between 10 and 500 characters.');
    }

    return errors;
}

// Function to display validation errors
function displayErrors(errors) {
    const errorContainer = document.getElementById('form-errors');
    errorContainer.innerHTML = '';
    errors.forEach((error) => {
        const errorElement = document.createElement('p');
        errorElement.textContent = error;
        errorElement.style.color = 'red';
        errorContainer.appendChild(errorElement);
    });
}

// Function to handle successful form submission
function handleSuccess(responseData) {
    const successMessage = document.getElementById('form-success');
    successMessage.textContent = 'Your prayer request has been submitted successfully!';
    successMessage.style.color = 'green';
}

// Function to handle errors during form submission
function handleError(errorMessage) {
    const errorContainer = document.getElementById('form-errors');
    errorContainer.innerHTML = '';
    const errorElement = document.createElement('p');
    errorElement.textContent = `Error: ${errorMessage}`;
    errorElement.style.color = 'red';
    errorContainer.appendChild(errorElement);
}

// Attach event listener to the form
document.getElementById('prayer-request-form').addEventListener('submit', handlePrayerRequestFormSubmission);
```

This code assumes you have an HTML form with the ID `prayer-request-form` and containers with IDs `form-errors` and `form-success` for displaying error and success messages, respectively.
