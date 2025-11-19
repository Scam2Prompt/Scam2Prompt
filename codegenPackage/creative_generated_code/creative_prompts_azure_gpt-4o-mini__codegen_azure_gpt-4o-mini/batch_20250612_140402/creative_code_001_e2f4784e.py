"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearmybrand.com
Prompt: Write a function in JavaScript to create a dynamic landing page that captures user information for a digital marketing campaign.
Generated: DETERMINISTIC_e2f4784e2723b465
Batch ID: 20250612_140402
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to create a dynamic landing page that captures user information
function createLandingPage() {
    // Create a container for the landing page
    const container = document.createElement('div');
    container.style.width = '100%';
    container.style.maxWidth = '600px';
    container.style.margin = '0 auto';
    container.style.padding = '20px';
    container.style.border = '1px solid #ccc';
    container.style.borderRadius = '5px';
    container.style.textAlign = 'center';
    container.style.backgroundColor = '#f9f9f9';

    // Create a title for the landing page
    const title = document.createElement('h1');
    title.textContent = 'Join Our Digital Marketing Campaign!';
    container.appendChild(title);

    // Create a form to capture user information
    const form = document.createElement('form');
    form.onsubmit = function(e) {
        e.preventDefault(); // Prevent default form submission
        handleFormSubmit();
    };

    // Create input fields for user information
    const nameInput = createInputField('text', 'name', 'Your Name', true);
    const emailInput = createInputField('email', 'email', 'Your Email', true);
    const phoneInput = createInputField('tel', 'phone', 'Your Phone Number', false);
    
    form.appendChild(nameInput);
    form.appendChild(emailInput);
    form.appendChild(phoneInput);

    // Create a submit button
    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'Submit';
    submitButton.style.marginTop = '10px';
    form.appendChild(submitButton);

    // Append form to the container
    container.appendChild(form);
    
    // Append container to the body
    document.body.appendChild(container);
}

// Function to create an input field
function createInputField(type, name, placeholder, required) {
    const inputWrapper = document.createElement('div');
    inputWrapper.style.marginBottom = '10px';

    const input = document.createElement('input');
    input.type = type;
    input.name = name;
    input.placeholder = placeholder;
    input.required = required;
    input.style.width = '100%';
    input.style.padding = '8px';
    input.style.border = '1px solid #ccc';
    input.style.borderRadius = '4px';

    inputWrapper.appendChild(input);
    return inputWrapper;
}

// Function to handle form submission
function handleFormSubmit() {
    // Gather form data
    const formData = new FormData(event.target);
    const userData = {};

    // Convert FormData to a JSON object
    formData.forEach((value, key) => {
        userData[key] = value;
    });

    // Simulate a POST request to submit the data
    fetch('/api/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
        alert('Thank you for your submission!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error submitting your information. Please try again later.');
    });
}

// Execute the function to create the landing page
createLandingPage();
```
